---
title: Equivariant Filters
---

> **Date:** April 25th, 2026    
> **Authors:** Rohan Bansal, Jennifer Oum, Frank Dellaert   

In earlier posts, we looked at several filters in GTSAM's hierarchy:

- `ManifoldEKF`
- `LieGroupEKF`
- `InvariantEKF`
- `LeftLinearEKF`

Now we can add one more: `EquivariantFilter`, which inherits from `ManifoldEKF`.

This post is a gentle introduction to what an equivariant filter is, why it is useful, and what the GTSAM implementation is buying us. We will refer to equivariant filters as "EqFs" for the rest of the blog post for brevity!

If you want the original paper, this post is based on [Equivariant Filter (EqF)](https://arxiv.org/abs/2010.14666) by van Goor, Hamel, and Mahony.

## A Simple Example

Imagine a robot carrying a gyroscope and a magnetometer. We want to estimate the direction of the magnetic field in the robot's body frame. That direction is a unit vector

$$
\eta \in \mathbb{S}^2,
$$

with dynamics

$$
\dot{\eta} = -\Omega^\times \eta,
$$

and measurement

$$
y = c_m \eta.
$$

Here, $\Omega$ is the angular velocity measured by the gyroscope. The matrix $\Omega^\times$ is the cross-product matrix, so the dynamics say that the magnetic-field direction appears to rotate in the robot's body frame as the robot turns. The measurement equation says the magnetometer observes that same direction, scaled by a constant magnetic-field strength $c_m$.


You may be able to see that the state is not a vector in plain Euclidean space, as it lives on the sphere. A standard EKF can still be used, but it usually means doing one of two things:

1. choose local coordinates on the sphere, or
2. embed the sphere in $\mathbb{R}^3$ and enforce the unit-length constraint separately

Both are possible, but neither are elegant or feel especially natural. The EqF starts from a different question:

> what symmetry does this problem already have?

In this case, the symmetry is rotation. Rotations in `SO(3)` move one direction on the sphere to another. The EqF uses that symmetry to define the estimation error!

## Manifolds, Groups, and Group Actions

To understand the EqF, here's a brief refresher on the three key geometric ideas.

A **manifold** is a state space that may be curved globally, even if it looks flat locally. If you use GTSAM, you have already seen manifolds (`Rot3`, `Pose3`, `Unit3`). The sphere $\mathbb{S}^2$ is a manifold, and so is the space of 3D rotations.

A **group** is a set of transformations that you can compose, invert, and compare to an identity. For this post, the important example is `SO(3)`: the group of 3D rotations.

A **group action** is a rule for how a transformation moves a state. In a simple example:

- the group is `SO(3)`
- the state is a direction on the sphere
- a rotation acts on that direction by rotating it

This gives us a way to move around the whole state space using rotations. More importantly for filtering, it gives us a way to compare the true state and the estimated state by asking which rotation would line them up. The EqF is about using that action to define an error in a smarter way.

## Main EqF Theory

The shortest possible summary of an equivariant filter is that it is *an error-state Kalman filter where the error is chosen using symmetry*.

Instead of storing the estimate directly as a state $\hat{\xi}$ on the manifold, EqF stores a group element $\hat{X}$ and applies it to a fixed reference state $\xi^\circ$:

$$
\hat{\xi} = \phi(\hat{X}, \xi^\circ).
$$

Here, $\phi$ is just the action of the group on the state space.

This gives a natural error:

$$
e = \phi(\hat{X}^{-1}, \xi).
$$

If the estimate is correct, that error lands back at the fixed reference point:

$$
e = \xi^\circ.
$$

This is the whole trick: instead of linearizing arbitrary coordinates around the current estimate, the EqF defines a geometry-aware error and linearizes that error around a fixed origin.

The process still looks like an EKF though, so the EqF is not throwing away any Kalman filtering, it is essentially just choosing a better error coordinate system:

- propagate the estimate
- propagate the covariance
- linearize the error dynamics
- apply a gain-based correction

## Predict and Update

As mentioned in the previous section, the runtime loop still feels like an EKF: predict the state, propagate covariance, compare predicted and observed measurements, compute a Kalman gain, and apply a correction.

The EqF difference is where the estimate and correction live. In the attitude example, the physical state is a direction on the sphere, but the filter stores a group element `g` and recovers the direction by applying `g` to `xi_ref`. During prediction, the **lift** converts the gyroscope motion into a small motion in the group. In this simple `Unit3` / `Rot3` case, that lift is almost trivial because small rotations are represented by 3-vectors, so the measured angular velocity can update `g` directly.

During update, GTSAM still forms the usual residual, Kalman gain, and small correction. The EqF-specific step is applying that correction through the group: the correction is mapped into a small update to `g`, then the state is recovered again from the group action. This keeps the normal EKF machinery while respecting the geometry of the sphere.

## How Do I Know When To Use It?

You may wish to pick a previously discussed filter like the IEKF in scenarios where the state itself is a Lie group, such as `Rot3` or `Pose3`.

However, the EqF can be more general because it also works when the state is not a Lie group. The important condition is that **some symmetry group must still act on the state**. Without that action, there is no special equivariant error to exploit, and the filter essentially reduces to an ordinary manifold EKF.

For example, in the direction-estimation scenario posited earlier:

- the state is on $\mathbb{S}^2$
- the symmetry group is `SO(3)`

The sphere is not a Lie group, but rotations still act on it, which is what the EqF is built to take advantage of.

## What It Looks Like in GTSAM

In GTSAM, the generic implementation lives in `gtsam/navigation/EquivariantFilter.h`.

It is templated on:

- a manifold state type `M`
- a symmetry functor `Symmetry`

and it inherits from `ManifoldEKF<M>`.

That design is important. GTSAM is not implementing EqF as some completely separate filter stack. It reuses the same manifold-EKF machinery and adds the symmetry-specific pieces on top.

The generic class stores two especially important objects:

- `xi_ref`, the fixed reference state
- `g`, the lifted group estimate

The current state estimate is recovered by applying the group action to `xi_ref`.

So the abstract EqF picture becomes very concrete in code:

- the fixed origin becomes `xi_ref`
- the lifted estimate becomes `g`
- the group action turns `g` into the current state estimate

The implementation also computes the linear map that takes a small correction on the manifold side and lifts it back to the group side. You do not need to understand the full differential-geometry machinery to use it. The main point is that GTSAM handles this bookkeeping inside the filter.

## Where the Richer Example Fits

Once the simple example makes sense, the next step is the ABC filter in:

- `gtsam_unstable/geometry/ABCEquivariantFilter.h`
- `examples/AbcEquivariantFilterExample.cpp`

That wrapper takes the generic EqF machinery and turns it into a friendlier application-specific API with methods like:

- `predict(omega, inputCovariance, dt)`
- `update(y, d, R, cal_idx)`

along with accessors for attitude, bias, and calibration.

That is a great second example. But it is easier to appreciate after the simpler `Unit3` / `Rot3` picture is already in place.

## Takeaway

Essentially, the EqF is an EKF that uses the natural transformations of the problem to define the error. It builds directly on `ManifoldEKF`, keeps the geometry explicit, and works naturally in cases where the state is more general than a Lie group.

As a GTSAM user, uou only need provide the model-specific ingredients; once you define:

- the state manifold
- the symmetry action
- the lift from physical dynamics to group motion
- the measurement model

the rest of the EKF machinery is already there. You do not need to rewrite Kalman gains, covariance propagation, or Joseph updates. The beauty of the equivariant filter is that the local model is built from the problem's natural symmetry instead of from a less natural choice of coordinates.

## Further Reading

- [Equivariant Filter (EqF) paper on arXiv](https://arxiv.org/abs/2010.14666)
- More complicated ABC EqF example in GTSAM: [Example](https://github.com/borglab/gtsam/blob/develop/examples/AbcEquivariantFilterExample.cpp), [Filter](https://github.com/borglab/gtsam/blob/develop/gtsam_unstable/geometry/ABCEquivariantFilter.h)