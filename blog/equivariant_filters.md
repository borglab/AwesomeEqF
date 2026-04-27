---
title: Equivariant Filters
---

> **Date:** April 25th, 2026    
> **Authors:** Rohan Bansal, Jennifer Oum, Frank Dellaert   

In previous blog posts, we have discussed the following filters in GTSAM's hierarchy:
- `ManifoldEKF`
- `LieGroupEKF`
- `InvariantEKF`
- `LeftLinearEKF`

Recently, we have integrated a new `EquivariantFilter` into the library, inheriting from `ManifoldEKF`. In this blog post, we will dive into the theory of equivariant filters and how they can be used in GTSAM.

If you would like to read the original paper this is based on: [Equivariant Filter (EqF)](https://arxiv.org/abs/2010.14666) by van Goor, Hamel, and Mahony.

## A Representative Example

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

In this toy problem, the state lives on the sphere, not in Euclidean space. A standard EKF can still be made to work, but only by choosing local coordinates or embedding the sphere in $\mathbb{R}^3$ and enforcing a constraint.

The equivariant filter takes a cleaner route. Rather than embedding the sphere in $\mathbb{R}^3$ and correcting constraint violations, it exploits the rotational symmetry of the problem. The estimation error is defined through the action of `SO(3)` on $\mathbb{S}^2$, making the error intrinsic to the geometry of the state space. The filter then linearizes this symmetry-based error dynamics in the appropriate tangent space.

`<TODO: insert figure here>`

## The Theory

The EqF is easiest to think of as an error-state Kalman filter where the error is chosen by symmetry.

The ingredients are:

- a Lie group $G$ acting on the state space $\mathcal{M}$
- dynamics that transform compatibly with that action
- a lift of the dynamics into the Lie algebra

For the direction-estimation example:

- the state space is $\mathbb{S}^2$
- the symmetry group is $\mathrm{SO}(3)$
- rotations move one direction on the sphere to another

In our example, the state space is not itself a Lie group, but it comes with a transitive group action. This is where EqF goes beyond the IEKF: it keeps the symmetry-first philosophy, but it works even when the state is not a Lie group.

The central construction of an EqF is:

1. Pick a fixed reference point $\xi^\circ \in \mathcal{M}$.
2. Represent the estimate with a group element $\hat{X} \in G$.
3. Recover the manifold estimate by acting on the reference point:

$$
\hat{\xi} = \phi(\hat{X}, \xi^\circ).
$$

This gives a geometric error

$$
e = \phi(\hat{X}^{-1}, \xi).
$$

When the estimate is correct, the error lands at the fixed origin:

$$
e = \xi^\circ.
$$

EqFs do not linearize arbitrary state coordinates around the current estimate. They linearize a symmetry-induced error around a fixed reference point. In local coordinates, the result still looks Kalman-like:

1. propagate the estimate
2. propagate the covariance
3. linearize the error dynamics
4. apply a gain-based correction

Essentially the EqF is building on top of the EKF, and choosing better error coordinates due to the symmetry of the situation.

## What does it look like in GTSAM?

In GTSAM, the generic implementation lives in `gtsam/navigation/EquivariantFilter.h`.

The class is templated on a manifold state type `M`, a symmetry functor `Symmetry`, and it inherits from `ManifoldEKF<M>`. Rather than treating EqF as a separate special-purpose filter, GTSAM keeps it within the existing family of filters to leverage base-class functionality.

The generic class stores two important objects:

- a reference state `xi_ref`, which is the fixed EqF origin
- a group estimate `g`, which is the lifted state

The current manifold estimate is obtained by applying the group action to `xi_ref`. That is the implementation version of

$$
\hat{\xi} = \phi(\hat{X}, \xi^\circ).
$$

The class also computes the differential of the action at the identity and its pseudoinverse. That pseudoinverse is the **innovation lift** used to map a correction in manifold error coordinates back to the group. `TODO: explain this more, maybe have a figure`

## Rohan-notes for things to add to this post

- Once you provide the manifold, the symmetry, the lift, and the measurement model, the EKF machinery is already there. You do not need to reimplement Kalman gains, Joseph updates, or covariance propagation each time.
- 

## Further Reading

- [Equivariant Filter (EqF) paper on arXiv](https://arxiv.org/abs/2010.14666)
- [Papers and Reading](../papers.md)
- [Notebooks](../notebooks.md)
