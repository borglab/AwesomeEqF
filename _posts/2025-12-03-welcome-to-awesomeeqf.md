---
layout: post
title: "Welcome to AwesomeEqF!"
date: 2025-12-03
categories: announcement
author: AwesomeEqF Team
excerpt: "Introducing a curated collection of resources on invariant and equivariant filtering for state estimation on manifolds and Lie groups."
---

We're excited to launch **Awesome Invariant and Equivariant Filtering** (AwesomeEqF), a community-driven resource for researchers, engineers, and students interested in advanced state estimation techniques on manifolds and Lie groups.

## Why AwesomeEqF?

Traditional Extended Kalman Filters (EKF) have been the workhorse of state estimation for decades. However, when dealing with systems that evolve on manifolds—such as rotations (SO(3)), poses (SE(3)), or other Lie groups—standard EKF approaches can suffer from:

- **Inconsistency**: The linearization may not respect the geometric structure
- **Poor convergence**: Especially far from the operating point
- **Loss of physical meaning**: Errors defined in ambient space rather than on the manifold

Invariant and Equivariant filtering methods address these challenges by:

1. **Exploiting System Symmetries**: Using the natural geometric structure of the problem
2. **Invariant Error Metrics**: Defining errors that respect the manifold geometry
3. **Improved Linearization**: Leveraging equivariance for better local approximations

## What You'll Find Here

### 📚 Curated Paper List
Our [GitHub repository](https://github.com/borglab/AwesomeEqF) contains a carefully curated list of:
- Foundational papers on IEKF and EqF
- Recent advances in the field
- Application-specific work (SLAM, VIO, navigation)

### 💻 Software Resources
We track implementations across multiple platforms:
- **GTSAM**: C++ library with production-ready EKF variants
- **Python/Julia**: Educational and research implementations
- **Open-source projects**: Real-world applications

### 📓 Interactive Notebooks
Learn by doing with our Jupyter notebooks:
- Introduction to IEKF concepts
- Step-by-step EqF implementation
- Real-world application examples

### ✍️ Blog Posts
Regular articles covering:
- Theoretical insights
- Practical implementation tips
- Tutorial walkthroughs
- Research highlights

## Getting Started

If you're new to invariant and equivariant filtering, we recommend:

1. **Read the basics**: Start with the [GTSAM EKF Variants documentation](https://borglab.github.io/gtsam/ekf-variants/)
2. **Understand the math**: Check out [Ethan Eade's Lie Groups primer](https://ethaneade.com/lie.pdf)
3. **Try an example**: Run our [Introduction to IEKF notebook](/AwesomeEqF/notebooks/)
4. **Dive deeper**: Read the foundational papers by Bonnabel and van Goor

## Key Papers to Start With

### For Invariant EKF:
- **Bonnabel (2009)**: [Invariant Extended Kalman Filter: theory and application to a velocity-aided attitude estimation problem](http://www.silvere-bonnabel.com/pdf/CDC2009IEKF.pdf)

This seminal paper introduced the IEKF and showed how exploiting system symmetries leads to improved filter consistency.

### For Equivariant Filters:
- **van Goor et al. (2021)**: [Equivariant Filter (EqF)](https://arxiv.org/abs/2010.14666)

A general framework for filter design on homogeneous spaces, unifying and extending previous approaches.

## Community

This project is **GTSAM-biased** (we love the [GTSAM library](https://github.com/borglab/gtsam)!) but welcomes all approaches and perspectives. We believe in:

- **Open collaboration**: All resources are freely available
- **Quality over quantity**: Curated, not comprehensive
- **Practical focus**: Theory meets implementation
- **Active maintenance**: Regular updates and improvements

## How to Contribute

We welcome contributions from the community:

- **Add papers**: Found a great paper? Submit a PR!
- **Share code**: Implemented an algorithm? Let us know!
- **Write tutorials**: Help others learn
- **Report issues**: Keep our resources up-to-date

Check our [Contributing Guide](https://github.com/borglab/AwesomeEqF/blob/main/CONTRIBUTING.md) for details.

## What's Next?

We have exciting plans for AwesomeEqF:

- 📝 More blog posts on advanced topics
- 📓 Additional notebooks covering diverse applications
- 🎥 Video tutorials and talks
- 🔗 Integration with other awesome lists
- 🤝 Community contributions and collaborations

## Stay Updated

- ⭐ Star the [GitHub repository](https://github.com/borglab/AwesomeEqF)
- 👀 Watch for updates
- 💬 Join discussions in Issues
- 🐦 Follow GTSAM updates

Thank you for being part of this community. Together, we'll make invariant and equivariant filtering more accessible and widely adopted!

---

*Have questions or feedback? Open an issue on [GitHub](https://github.com/borglab/AwesomeEqF/issues) or contribute directly!*
