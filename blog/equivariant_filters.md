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

This post is a gentle introduction to what an equivariant filter is, why it is useful, and what the GTSAM implementation is buying us.

If you want the original paper, this post is based on [Equivariant Filter (EqF)](https://arxiv.org/abs/2010.14666) by van Goor, Hamel, and Mahony.

## Start With a Simple Example

The cleanest example is the same one used in the paper and in GTSAM's simple attitude-only test.

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

This is already enough to motivate EqF.

The state is not a vector in plain Euclidean space. It lives on the sphere. A standard EKF can still be used, but it usually means doing one of two things:

1. choose local coordinates on the sphere, or
2. embed the sphere in $\mathbb{R}^3$ and enforce the unit-length constraint separately

Both are workable. Neither feels especially natural.

EqF starts from a different question:

> what symmetry does this problem already have?

In this case, the symmetry is rotation. Rotations in `SO(3)` move one direction on the sphere to another. EqF uses that symmetry to define the estimation error.

## Three Ideas, Gently

To understand EqF, we only need three geometric ideas.

### 1. A manifold

A **manifold** is just a state space that may be curved globally, even if it looks flat locally.

If you use GTSAM, you have already seen manifolds:

- `Rot3`
- `Pose3`
- `Unit3`

The sphere $\mathbb{S}^2$ is a manifold. So is the space of 3D rotations.

### 2. A group

A **group** is a set of transformations that you can compose, invert, and compare to an identity.

For this post, the important example is `SO(3)`: the group of 3D rotations.

### 3. A group action

A **group action** is just a rule for how a transformation moves a state.

That phrase can sound abstract, but here it is very simple:

- the group is `SO(3)`
- the state is a direction on the sphere
- a rotation acts on that direction by rotating it

That is all we need. EqF is about using that action to define an error in a smarter way.

## The Main EqF Idea

The easiest short description is:

> EqF is an error-state Kalman filter where the error is chosen using symmetry.

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

This is the whole trick. EqF does not linearize arbitrary coordinates around the current estimate. It defines a geometry-aware error and linearizes that error around a fixed origin.

The result still looks like an EKF:

- propagate the estimate
- propagate the covariance
- linearize the error dynamics
- apply a gain-based correction

So EqF is not throwing away Kalman filtering. It is choosing a better error coordinate system.

## Why This Is Different From the IEKF

The IEKF is most natural when the state itself is a Lie group, such as `Rot3` or `Pose3`.

EqF is more general. It also works when the state is not a Lie group, but still has a symmetry group acting on it.

That is exactly what happens in the direction-estimation example:

- the state is on $\mathbb{S}^2$
- the symmetry group is `SO(3)`

The sphere is not a Lie group, but rotations still act on it. EqF is built to take advantage of that.

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

## Why This Is Useful for GTSAM Users

There are three practical benefits.

### 1. The geometry stays explicit

EqF is really about geometry, so it is a good fit for a library that already has types like `Rot3`, `Pose3`, and `Unit3`. You can write the filter in terms of geometric objects instead of flattening everything into anonymous matrices.

### 2. You only provide the model-specific ingredients

Once you define:

- the state manifold
- the symmetry action
- the lift
- the measurement model

the rest of the EKF machinery is already there. You do not need to rewrite Kalman gains, covariance propagation, or Joseph updates.

### 3. There is a clean learning path

The simplest place to start is the attitude-only `Unit3` / `Rot3` example in `gtsam/navigation/tests/testEquivariantFilter.cpp`.

That example is valuable because it keeps the focus on the central EqF idea:

- a state on a manifold
- a group acting on that state
- an error defined through the action

without introducing extra state components too early.

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

If you know GTSAM but do not spend your day thinking about manifolds and group actions, the right mental model is:

> EqF is an EKF that uses the natural transformations of the problem to define the error.

That is why it belongs in GTSAM's hierarchy. It builds directly on `ManifoldEKF`, keeps the geometry explicit, and works naturally in cases where the state is more general than a Lie group.

## Further Reading

- [Equivariant Filter (EqF) paper on arXiv](https://arxiv.org/abs/2010.14666)
- [Papers and Reading](../papers.md)
- [Notebooks](../notebooks.md)
