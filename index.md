---
layout: default
title: Home
---

# Awesome Invariant and Equivariant Filtering

Welcome to the community hub for invariant and equivariant filtering! This site hosts educational resources, blog posts, and interactive notebooks to help you understand and apply these powerful state estimation techniques.

## 🎯 What is Invariant and Equivariant Filtering?

Invariant and Equivariant filtering methods revolutionize state estimation for systems on manifolds and Lie groups. These techniques:

- **Exploit geometric structure** to improve accuracy
- **Preserve system symmetries** for better consistency
- **Reduce linearization errors** in nonlinear systems
- **Enhance stability** for navigation and robotics applications

## 📚 Quick Start

- **New to the field?** Check out the [GTSAM EKF Variants Tutorial](https://borglab.github.io/gtsam/ekf-variants/)
- **Looking for papers?** Browse our [curated list on GitHub](https://github.com/borglab/AwesomeEqF)
- **Want hands-on experience?** Explore our [example notebooks](/AwesomeEqF/notebooks/)
- **Latest updates?** Read our [blog posts](/AwesomeEqF/blog/)

## 📖 Latest Blog Posts

{% for post in site.posts limit:3 %}
  <div class="post-preview">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p class="post-meta">{{ post.date | date: "%B %d, %Y" }} {% if post.author %} • {{ post.author }}{% endif %}</p>
    <p>{{ post.excerpt }}</p>
  </div>
{% endfor %}

[View all posts →](/AwesomeEqF/blog/)

## 🔬 Featured Topics

### Invariant Extended Kalman Filter (IEKF)
The IEKF uses invariant error metrics that respect the geometry of the state space, leading to improved consistency and convergence for attitude and navigation estimation.

### Equivariant Filter (EqF)
The EqF leverages system equivariance properties to design observers with reduced linearization errors, particularly effective for systems on homogeneous spaces.

### Applications
- Visual-Inertial Odometry (VIO)
- SLAM and Navigation
- Attitude Estimation
- IMU Integration
- Robotics State Estimation

## 💻 Software

The [GTSAM library](https://github.com/borglab/gtsam) provides production-ready implementations of multiple EKF variants:
- ManifoldEKF
- LieGroupEKF
- InvariantEKF
- NavStateImuEKF

## 🤝 Community

This is a community-driven resource! Contributions are welcome:

- **Add resources**: Submit papers, libraries, or tutorials via [pull request](https://github.com/borglab/AwesomeEqF/pulls)
- **Share knowledge**: Write blog posts or create notebooks
- **Report issues**: Help us maintain quality via [GitHub issues](https://github.com/borglab/AwesomeEqF/issues)

See our [Contributing Guide](https://github.com/borglab/AwesomeEqF/blob/main/CONTRIBUTING.md) for details.

## 🔗 Related Resources

- [GTSAM EKF Variants Documentation](https://borglab.github.io/gtsam/ekf-variants/)
- [GTSAM GitHub Repository](https://github.com/borglab/gtsam)
- [Awesome SLAM](https://github.com/youngguncho/awesome-slam)

---

## 👥 Contributors

This project originated at **Georgia Tech** and is maintained by the GTSAM community.

**Core Contributors:**
- **Rohan Madan** - Initial curation and project setup
- **Frank Dellaert** - Project guidance and oversight

---

<div style="text-align: center; margin-top: 3em; padding-top: 2em; border-top: 1px solid #ddd;">
  <p>Originated at Georgia Tech | Maintained by the GTSAM community | <a href="https://github.com/borglab/AwesomeEqF">View on GitHub</a></p>
</div>
