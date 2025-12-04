---
layout: default
title: "Introduction to Equivariant Filters"
date: 2025-12-12
categories: tutorial
author: AwesomeEqF Contributors
excerpt: "Exploring the Equivariant Filter (EqF) framework, a general approach to observer design on homogeneous spaces that unifies and extends invariant filtering methods."
---

# Introduction to Equivariant Filters

Following our [previous post on IEKF](/AwesomeEqF/blog/2024/11/15/understanding-iekf/), let's explore the Equivariant Filter (EqF)—a powerful generalization that takes invariant filtering to the next level.

## Beyond Invariant Filters

The Invariant Extended Kalman Filter (IEKF) works beautifully for systems on Lie groups, but what about systems on more general spaces? Enter the **Equivariant Filter**.

### What is Equivariance?

A system is **equivariant** if its behavior respects a group action. Formally, for a system with state x and output y:

```
If x → g·x (apply group action g)
Then y → ρ(g)·y (output transforms predictably)
```

This is a weaker condition than full invariance, making it applicable to a broader class of systems.

## The EqF Framework

Developed by Pieter van Goor, Tarek Hamel, and Robert Mahony, the EqF provides a systematic way to design observers for equivariant systems on homogeneous spaces.

### Key Concepts

1. **Homogeneous Spaces**: Spaces where a group G acts transitively
   - Examples: Spheres, projective spaces, Grassmannians
   - SE(3)/SO(3) (positions with translations)

2. **Equivariant Dynamics**: The system dynamics commute with group actions
   
3. **Lifted Coordinates**: Represent the state on a Lie group covering the space

## Why EqF?

The equivariant approach offers several advantages:

### 1. Reduced Linearization Error
By exploiting system symmetries, the EqF achieves linearization that's valid over larger regions of the state space.

### 2. Natural Observer Design
The framework provides a systematic recipe for designing observers, removing much of the guesswork.

### 3. Unified Theory
EqF unifies several existing approaches:
- Invariant observers
- Group affine systems
- Symmetry-preserving observers

## EqF vs IEKF

How do they compare?

| Aspect | IEKF | EqF |
|--------|------|-----|
| State space | Lie groups | Homogeneous spaces |
| System class | Invariant systems | Equivariant systems |
| Error definition | Invariant | Equivariant |
| Complexity | Moderate | Higher |
| Flexibility | Good | Excellent |

The EqF is more general, but IEKF may be simpler when applicable.

## Mathematical Framework

### System Model

Consider a system on a homogeneous space X = G/H:

**Dynamics:**
```
ẋ = f(x, u, w)
```

**Output:**
```
y = h(x, v)
```

### Equivariance Conditions

The system is equivariant if:

```
f(g·x, u, w) = g·f(x, u, w)  for all g ∈ G
h(g·x, v) = ρ(g)·h(x, v)    for all g ∈ G
```

### EqF Design

The EqF design involves:

1. **Lift to Lie group**: Find A ∈ G such that π(A) = x
2. **Define equivariant error**: E = A₀⁻¹ · Â
3. **Design innovation**: Uses equivariant output error
4. **Gain tuning**: Similar to standard EKF

## Example: Visual-Inertial Odometry

VIO is a perfect application for EqF:

- **State**: Position, velocity, rotation (lives on R³ × R³ × SO(3))
- **Dynamics**: Constant velocity + gravity + IMU
- **Measurements**: Visual features + IMU

The EqF naturally handles:
- Unknown scale in monocular vision
- Mixed discrete/continuous measurements
- Varying number of features

## Implementation Considerations

### 1. Identify Symmetries
First, determine the group G acting on your state space. Common choices:
- SE(3): Poses in 3D
- SIM(3): Poses with scale
- Extended pose groups

### 2. Verify Equivariance
Check that your system dynamics satisfy the equivariance condition. This might require reformulation.

### 3. Choose Lifted Coordinates
Select a representation on the Lie group. This choice affects computational efficiency.

### 4. Design Innovation
The innovation must respect the equivariant structure. The EqF paper provides explicit formulas.

## Practical Benefits

Studies show EqF provides:

- **Better Consistency**: Particularly for visual-inertial systems
- **Improved Convergence**: Faster than standard EKF
- **Robustness**: More robust to poor initialization
- **Flexibility**: Handles varying measurements naturally

## Software

Several implementations exist:

- **[EqF-VIO](https://github.com/pvangoor/eqf_vio)**: Visual-inertial odometry using EqF
- **GTSAM**: Working on EqF integration
- **Research code**: Available from paper authors

## When to Use EqF

The EqF shines when:

- System has natural symmetries
- State lives on homogeneous space
- IEKF structure doesn't quite fit
- You need maximum flexibility

## Limitations

However, EqF also has challenges:

- More complex mathematics
- Requires identifying symmetries
- Higher implementation complexity
- May be overkill for simple problems

## Learning Path

To master EqF:

1. **Foundation**: Understand IEKF first
2. **Theory**: Read the [EqF paper](https://arxiv.org/abs/2010.14666)
3. **Practice**: Study EqF-VIO implementation
4. **Apply**: Try on your own system

## Advanced Topics

### Iterated EqF
Recent work introduces iteration and covariance resets for improved performance in tightly coupled systems.

### EqF with Bias States
Handling IMU biases and other slowly varying parameters within the EqF framework.

### Equivariant SLAM
Applying EqF principles to simultaneous localization and mapping.

## Comparison: Real-World Performance

In visual-inertial odometry benchmarks:

- **EqF**: Best consistency and convergence
- **IEKF**: Good performance, simpler
- **Standard EKF**: Adequate but less consistent

The choice depends on your application's requirements and complexity budget.

## The Future

The equivariant approach is still actively developing:

- Integration with machine learning
- Extension to discrete-time systems
- Application to new domains
- Computational optimizations

## Conclusion

The Equivariant Filter represents a significant advancement in state estimation theory. While more complex than IEKF, it provides unmatched flexibility and performance for systems with rich symmetry structure.

For most robotics applications, especially visual-inertial odometry and SLAM, the EqF is becoming the method of choice.

## Resources

- **Paper**: [Equivariant Filter (EqF)](https://arxiv.org/abs/2010.14666)
- **Code**: [EqF-VIO](https://github.com/pvangoor/eqf_vio)
- **Tutorial**: [GTSAM EKF Variants](https://borglab.github.io/gtsam/ekf-variants/)
- **Notebooks**: Work through our [EqF examples](/AwesomeEqF/notebooks/)

## Coming Up

In our next post, we'll dive into **practical implementation tips** for both IEKF and EqF, including common pitfalls and debugging strategies.

---

*Questions? Join the discussion on [GitHub](https://github.com/borglab/AwesomeEqF/issues)!*
