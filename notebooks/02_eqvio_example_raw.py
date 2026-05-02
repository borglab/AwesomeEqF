"""
Python replay example for the unstable EqVIO filter wrapper.

This mirrors the C++ EqVIOFilterExample flow:
1. load the bundled replay CSV,
2. initialize from first IMU sample,
3. run buffered IMU propagation between vision frames,
4. apply visual updates and print a compact terminal summary.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import csv
import math
from typing import Dict, List, Optional

import numpy as np
import gtsam
import gtsam_unstable


@dataclass
class ReplayEvent:
    kind: str
    seq: int
    t_abs: float
    frame_idx: int = -1
    imu: Optional[gtsam_unstable.eqvio.IMUInput] = None
    vision: Dict[int, np.ndarray] = field(default_factory=dict)


@dataclass
class ReplayLog:
    metadata: Dict[str, str]
    events: List[ReplayEvent]


@dataclass
class BufferedImuPropagation:
    imu_inputs: List[gtsam_unstable.eqvio.IMUInput] = field(default_factory=list)
    dts: List[float] = field(default_factory=list)
    propagated_time: float = 0.0
    trim_count: int = 0


@dataclass
class TimestampedImu:
    t_abs: float
    imu: gtsam_unstable.eqvio.IMUInput


def _parse_float(text: str, fallback: float = 0.0) -> float:
    if text is None or text == "":
        return fallback
    return float(text)


def _parse_int(text: str, fallback: int = 0) -> int:
    if text is None or text == "":
        return fallback
    return int(text)


def _metadata_finite_float(metadata: Dict[str, str], key: str, fallback: float) -> float:
    if key not in metadata or metadata[key] == "":
        return fallback
    try:
        value = float(metadata[key])
        return value if math.isfinite(value) else fallback
    except ValueError:
        return fallback


def _camera_offset_from_metadata(metadata: Dict[str, str]) -> Optional[gtsam.Pose3]:
    keys = ["T_ci_tx", "T_ci_ty", "T_ci_tz", "T_ci_qw", "T_ci_qx", "T_ci_qy", "T_ci_qz"]
    if any(k not in metadata or metadata[k] == "" for k in keys):
        return None

    tx = float(metadata["T_ci_tx"])
    ty = float(metadata["T_ci_ty"])
    tz = float(metadata["T_ci_tz"])
    qw = float(metadata["T_ci_qw"])
    qx = float(metadata["T_ci_qx"])
    qy = float(metadata["T_ci_qy"])
    qz = float(metadata["T_ci_qz"])

    norm = math.sqrt(qw * qw + qx * qx + qy * qy + qz * qz)
    if norm <= 1e-12:
        return None
    qw /= norm
    qx /= norm
    qy /= norm
    qz /= norm

    return gtsam.Pose3(gtsam.Rot3.Quaternion(qw, qx, qy, qz), np.array([tx, ty, tz]))


def _required_columns() -> List[str]:
    return [
        "row_type",
        "t_abs",
        "seq",
        "frame_idx",
        "landmark_id",
        "gx",
        "gy",
        "gz",
        "ax",
        "ay",
        "az",
        "bgx",
        "bgy",
        "bgz",
        "bax",
        "bay",
        "baz",
        "u_norm",
        "v_norm",
        "key",
        "value",
    ]


def read_replay_csv(csv_path: str) -> ReplayLog:
    metadata: Dict[str, str] = {}
    events: List[ReplayEvent] = []
    seq_to_vision_event: Dict[int, int] = {}

    with open(csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"EqVIOFilterExample: empty file: {csv_path}")

        for key in _required_columns():
            if key not in reader.fieldnames:
                raise ValueError(f"EqVIOFilterExample: missing required column: {key}")

        for row in reader:
            row_type = (row.get("row_type") or "").strip()
            if row_type == "":
                continue

            if row_type == "meta":
                key = (row.get("key") or "").strip()
                if key:
                    metadata[key] = (row.get("value") or "").strip()
                continue

            seq = _parse_int(row.get("seq"), 0)
            t_abs = _parse_float(row.get("t_abs"), 0.0)

            if row_type == "imu":
                imu = gtsam_unstable.eqvio.IMUInput()
                imu.stamp = t_abs
                imu.gyr = np.array(
                    [
                        _parse_float(row.get("gx")),
                        _parse_float(row.get("gy")),
                        _parse_float(row.get("gz")),
                    ]
                )
                imu.acc = np.array(
                    [
                        _parse_float(row.get("ax")),
                        _parse_float(row.get("ay")),
                        _parse_float(row.get("az")),
                    ]
                )
                imu.gyrBiasVel = np.array(
                    [
                        _parse_float(row.get("bgx")),
                        _parse_float(row.get("bgy")),
                        _parse_float(row.get("bgz")),
                    ]
                )
                imu.accBiasVel = np.array(
                    [
                        _parse_float(row.get("bax")),
                        _parse_float(row.get("bay")),
                        _parse_float(row.get("baz")),
                    ]
                )
                events.append(ReplayEvent(kind="imu", seq=seq, t_abs=t_abs, imu=imu))
                continue

            if row_type == "vision_feature":
                frame_idx = _parse_int(row.get("frame_idx"), -1)
                landmark_id = _parse_int(row.get("landmark_id"), 0)
                u_norm = _parse_float(row.get("u_norm"), 0.0)
                v_norm = _parse_float(row.get("v_norm"), 0.0)

                if seq not in seq_to_vision_event:
                    event = ReplayEvent(
                        kind="vision",
                        seq=seq,
                        t_abs=t_abs,
                        frame_idx=frame_idx,
                        vision={landmark_id: np.array([u_norm, v_norm])},
                    )
                    seq_to_vision_event[seq] = len(events)
                    events.append(event)
                else:
                    event = events[seq_to_vision_event[seq]]
                    if event.frame_idx != frame_idx:
                        raise ValueError(
                            f"EqVIOFilterExample: inconsistent frame_idx for vision seq={seq}"
                        )
                    if abs(event.t_abs - t_abs) > 1e-9:
                        raise ValueError(
                            f"EqVIOFilterExample: inconsistent t_abs for vision seq={seq}"
                        )
                    event.vision[landmark_id] = np.array([u_norm, v_norm])
                continue

            raise ValueError(f"EqVIOFilterExample: unknown row_type: {row_type}")

    events.sort(key=lambda event: event.seq)
    return ReplayLog(metadata=metadata, events=events)


def make_buffered_imu_propagation(
    imu_buffer: List[TimestampedImu], current_time: float, target_time: float
) -> BufferedImuPropagation:
    out = BufferedImuPropagation()
    if not imu_buffer or target_time <= current_time:
        return out

    t_ref = current_time
    for i, sample in enumerate(imu_buffer):
        t0 = max(sample.t_abs, t_ref)
        t1 = min(imu_buffer[i + 1].t_abs, target_time) if i + 1 < len(imu_buffer) else target_time
        dt = max(t1 - t0, 0.0)
        if dt <= 0.0:
            continue
        out.imu_inputs.append(sample.imu)
        out.dts.append(dt)
        out.propagated_time += dt

    first_ge_target = None
    for i, sample in enumerate(imu_buffer):
        if sample.t_abs >= target_time:
            first_ge_target = i
            break
    idx = len(imu_buffer) if first_ge_target is None else first_ge_target
    if idx != 0:
        out.trim_count = idx - 1

    return out


def _initial_covariance_from_metadata(metadata: Dict[str, str]) -> np.ndarray:
    Sigma0 = np.eye(21)

    def set_initial_variance_block(idx: int, key: str, fallback: float) -> None:
        Sigma0[idx : idx + 3, idx : idx + 3] *= _metadata_finite_float(
            metadata, key, fallback
        )

    set_initial_variance_block(0, "eqf.initial_var_bias_omega", 0.1)
    set_initial_variance_block(3, "eqf.initial_var_bias_accel", 0.1)
    set_initial_variance_block(6, "eqf.initial_var_attitude", 1e-4)
    set_initial_variance_block(9, "eqf.initial_var_position", 1e-4)
    set_initial_variance_block(12, "eqf.initial_var_velocity", 1e-2)
    set_initial_variance_block(15, "eqf.initial_var_cam_attitude", 1e-5)
    set_initial_variance_block(18, "eqf.initial_var_cam_position", 1e-4)
    return Sigma0


def _params_from_metadata(
    metadata: Dict[str, str],
) -> gtsam_unstable.eqvio.EqVIOFilterParams:
    params = gtsam_unstable.eqvio.EqVIOFilterParams()
    params.initialPointDepth = _metadata_finite_float(metadata, "eqf.initial_point_depth", 10.0)
    params.initialPointVariance = _metadata_finite_float(
        metadata, "eqf.initial_point_variance", 1.0
    )
    outlier_threshold_abs = _metadata_finite_float(metadata, "eqf.outlier_threshold_abs", 1e8)
    outlier_threshold_abs = _metadata_finite_float(
        metadata, "eqf.outlier_threshold_abs_norm", outlier_threshold_abs
    )
    params.outlierThresholdAbs = outlier_threshold_abs
    params.featureRetention = _metadata_finite_float(metadata, "eqf.feature_retention", 0.3)
    params.biasOmegaProcessVariance = _metadata_finite_float(
        metadata, "eqf.process_var_bias_omega", 0.001
    )
    params.biasAccelProcessVariance = _metadata_finite_float(
        metadata, "eqf.process_var_bias_accel", 0.001
    )
    params.attitudeProcessVariance = _metadata_finite_float(
        metadata, "eqf.process_var_attitude", 0.001
    )
    params.positionProcessVariance = _metadata_finite_float(
        metadata, "eqf.process_var_position", 0.001
    )
    params.velocityProcessVariance = _metadata_finite_float(
        metadata, "eqf.process_var_velocity", 0.001
    )
    params.cameraAttitudeProcessVariance = _metadata_finite_float(
        metadata, "eqf.process_var_cam_attitude", 0.001
    )
    params.cameraPositionProcessVariance = _metadata_finite_float(
        metadata, "eqf.process_var_cam_position", 0.001
    )
    params.pointProcessVariance = _metadata_finite_float(
        metadata, "eqf.process_var_point", 0.001
    )

    input_noise = np.zeros((12, 12))
    input_variances = {
        0: _metadata_finite_float(metadata, "eqf.input_var_gyr", 1e-3),
        3: _metadata_finite_float(metadata, "eqf.input_var_acc", 1e-3),
        6: _metadata_finite_float(metadata, "eqf.input_var_gyr_bias_walk", 1e-3),
        9: _metadata_finite_float(metadata, "eqf.input_var_acc_bias_walk", 1e-3),
    }
    for idx, variance in input_variances.items():
        input_noise[idx : idx + 3, idx : idx + 3] = np.eye(3) * variance
    params.inputNoise = input_noise
    return params


def main() -> None:
    csv_path = "/Users/apollo/Downloads/eqvio_processed_60s_withgt.csv"
    log = read_replay_csv(csv_path)

    camera_offset = _camera_offset_from_metadata(log.metadata)
    initial_covariance = _initial_covariance_from_metadata(log.metadata)
    params = _params_from_metadata(log.metadata)
    measurement_noise_variance = _metadata_finite_float(
        log.metadata, "eqf.measurement_noise_variance_norm", 1e-4
    )
    xi_ref = gtsam_unstable.eqvio.State()
    if camera_offset is not None:
        xi_ref.cameraOffset = camera_offset

    filter_eqf: Optional[gtsam_unstable.eqvio.EqVIOFilter] = None
    camera = gtsam.PinholeCameraCal3_S2(
        gtsam.Pose3(), gtsam.Cal3_S2(1.0, 1.0, 0.0, 0.0, 0.0)
    )
    imu_buffer: List[TimestampedImu] = []
    gravity_initialized = False
    current_time = -1.0

    imu_count = 0
    vision_frame_count = 0
    vision_feature_count = 0

    for event in log.events:
        if event.kind == "imu":
            if filter_eqf is None:
                filter_eqf = gtsam_unstable.eqvio.EqVIOFilter(
                    xi_ref, initial_covariance, gtsam.KeyVector(), params
                )
            if not gravity_initialized and event.imu is not None:
                filter_eqf.initializeFromIMU(event.imu)
                current_time = event.t_abs
                gravity_initialized = True
            if event.imu is not None:
                imu_buffer.append(TimestampedImu(t_abs=event.t_abs, imu=event.imu))
                imu_count += 1
            continue

        vision_frame_count += 1
        vision_feature_count += len(event.vision)
        if not gravity_initialized or filter_eqf is None:
            continue

        step = make_buffered_imu_propagation(imu_buffer, current_time, event.t_abs)
        for imu_in, dt in zip(step.imu_inputs, step.dts):
            filter_eqf.predict(imu_in, dt)
        if step.imu_inputs:
            current_time += step.propagated_time
        if step.trim_count > 0:
            imu_buffer = imu_buffer[step.trim_count:]

        R = np.eye(2 * len(event.vision)) * measurement_noise_variance
        filter_eqf.update(event.vision, camera, R)

    print("CSV replay complete.")
    print(
        f"Events: {imu_count + vision_frame_count}, IMU: {imu_count}, "
        f"vision frames: {vision_frame_count}, vision features: {vision_feature_count}"
    )
    print(f"Measurement noise variance (normalized): {measurement_noise_variance}")
    print(f"Filter time: {current_time:.16f}")

    if filter_eqf is None:
        return

    position = np.asarray(filter_eqf.position()).reshape(3)
    velocity = np.asarray(filter_eqf.velocity()).reshape(3)
    print(f"Landmarks: {filter_eqf.landmarkCount()}")
    print(f"Pose translation: {position[0]: .10f} {position[1]: .10f} {position[2]: .10f}")
    print("GT pose translation:  1.68803 2.19695 0.645814")
    print(f"Velocity: {velocity[0]: .10f} {velocity[1]: .10f} {velocity[2]: .10f}")
    print("GT velocity:  -0.015025 0.536785 0.0378963")


if __name__ == "__main__":
    main()