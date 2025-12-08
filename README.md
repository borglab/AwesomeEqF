# Awesome Invariant and Equivariant Filtering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of resources and research papers related to Invariant and Equivariant filtering for state estimation on manifolds and Lie groups. GTSAM-biased but welcoming to all approaches! 🔬

> **Note**: For a comprehensive overview of EKF variants implemented in GTSAM, check out the [GTSAM EKF Variants documentation](https://borglab.github.io/gtsam/ekf-variants/).

## 📚 Table of Contents

- [Introduction](#introduction)
- [Foundational Papers](#foundational-papers)
  - [Invariant Extended Kalman Filter (IEKF)](#invariant-extended-kalman-filter-iekf)
  - [Equivariant Filter (EqF)](#equivariant-filter-eqf)
- [Recent Advances](#recent-advances)
- [Software and Libraries](#software-and-libraries)
- [Tutorials and Talks](#tutorials-and-talks)
- [Applications](#applications)
- [Related Resources](#related-resources)
- [Contributing](#contributing)

## 🎯 Introduction

Invariant and Equivariant filtering methods address the challenges of state estimation for systems evolving on manifolds and Lie groups. Unlike traditional Extended Kalman Filters (EKF), these approaches:

- **Exploit geometric structure** and system symmetries
- **Improve consistency** and convergence properties
- **Reduce linearization errors** through equivariant design
- **Provide better stability** for attitude and navigation estimation

**Key Concepts:**

- **Invariant Filters**: Use invariant error metrics that respect the geometry of the state space
- **Equivariant Filters**: Leverage system equivariance properties for improved observer design
- **Lie Groups**: Mathematical structures (e.g., SO(3), SE(3)) naturally representing rotations and poses

## 📖 Foundational Papers

### Invariant Extended Kalman Filter (IEKF)

- **[Invariant Extended Kalman Filter: theory and application to a velocity-aided attitude estimation problem](http://www.silvere-bonnabel.com/pdf/CDC2009IEKF.pdf)** (2009)  
  _Silvère Bonnabel, Philippe Martin, Pierre Rouchon_  
  The seminal paper introducing the IEKF, showing improved consistency for attitude estimation.

- **[The Invariant Extended Kalman Filter as a Stable Observer](https://arxiv.org/abs/1410.1465)** (2016)  
  _Axel Barrau, Silvère Bonnabel_  
  Rigorous stability analysis of the IEKF, establishing conditions for local asymptotic stability.

- **[Symmetry-preserving observers](https://ieeexplore.ieee.org/document/1339919)** (2004)  
  _A. Saccon, A. P. Aguiar, A. M. Pascoal_  
  Early work on observer design that preserves system symmetries.

- **[Non-linear state error based extended Kalman filters with applications to navigation](https://theses.hal.science/tel-01344622/)** (2013)  
  _Axel Barrau_  
  Comprehensive PhD thesis on IEKF theory and applications.

- **[Equivariant Filter Design for Kinematic Systems on Lie Groups](https://www.sciencedirect.com/science/article/pii/S240589632100642X)** (2021)  
  _Alessandro Saccon et al._  
  Framework for embedding kinematic systems on Lie groups into equivariant systems.

### Equivariant Filter (EqF)

- **[Nonlinear Complementary Filters on the Special Orthogonal Group](https://arxiv.org/abs/0806.0620)** (2008)  
  _Robert Mahony, Tarek Hamel, Jean-Michel Pflimlin_  
  Early nonlinear complementary filter on SO(3) that strongly influenced later invariant and equivariant attitude observers.

- **[Equivariant Filter (EqF)](https://arxiv.org/abs/2010.14666)** (2021)  
  _Pieter van Goor, Tarek Hamel, Robert Mahony_  
  The foundational paper on equivariant filtering for systems on homogeneous spaces.

- **[EQUIVARIANT FILTER (EQF): A GENERAL FILTER DESIGN FOR SYSTEMS ON HOMOGENEOUS SPACES](https://arxiv.org/pdf/2107.05193)** (2021)  
  _Pieter van Goor, Tarek Hamel, Robert Mahony_  
  Extended version with detailed theoretical development.

- **[Observer Design on the Special Euclidean Group SE(3)](https://ieeexplore.ieee.org/document/6160453)** (2011)  
  _Robert Mahony, Tarek Hamel_  
  Early work on observer design for pose estimation on SE(3).

## 🚀 Recent Advances

- **[An Iterated Equivariant Filter and Its Application in Tightly Coupled GNSS/INS](https://ieeexplore.ieee.org/document/10979539)** (2024)  
  _Various Authors_  
  Combines covariance reset steps for improved performance in tightly coupled systems.

- **[The Difference between the Left and Right Invariant Extended Kalman Filter](https://arxiv.org/abs/2507.04568)** (2024)  
  Shows that left and right IEKF variants yield identical performance with proper reset steps.

- **[Equivariant Systems Theory and Observer Design](https://arxiv.org/abs/2006.08276)** (2020)  
  _Pieter van Goor, Robert Mahony_  
  Unified framework connecting invariant and equivariant approaches.

- **[Invariant Kalman Filtering for Visual-Inertial SLAM](https://ieeexplore.ieee.org/document/8455807)** (2018)  
  Application of IEKF to visual-inertial odometry and SLAM.

## 💻 Software and Libraries

### GTSAM (Georgia Tech Smoothing and Mapping)

- **[GTSAM](https://github.com/borglab/gtsam)** - C++ library with multiple EKF variants
  - ManifoldEKF: EKF for states on differentiable manifolds
  - LieGroupEKF: For states on Lie groups with state-dependent dynamics
  - InvariantEKF: For states on Lie groups with group composition dynamics
  - leftLinearEKF & NavStateImuEKF: Extensions for left-linear observers and IMU integration
  - **[EKF Variants Documentation](https://borglab.github.io/gtsam/ekf-variants/)** - Comprehensive guide to GTSAM's EKF implementations

### Other Libraries

- **[EqF-VIO](https://github.com/pvangoor/eqf_vio)** - Equivariant Filter for Visual-Inertial Odometry
- **[IEKF-SLAM](https://github.com/CAOR-MINES-ParisTech/ukfm)** - Unscented Kalman Filter on Manifolds

## 🎓 Tutorials and Talks

- **[GTSAM EKF Variants Tutorial](https://borglab.github.io/gtsam/ekf-variants/)** - Interactive documentation with examples
<!-- - **[Invariant Filtering Tutorial](https://www.youtube.com/watch?v=nJgW3pL5Qgw)** - Video introduction to invariant filtering -->
- **[Lie Groups for 2D and 3D Transformations](https://ethaneade.com/lie.pdf)** - Primer on Lie groups in robotics by Ethan Eade

## 🔬 Applications

### Navigation and IMU Integration

- Dead reckoning and INS/GNSS fusion
- Attitude estimation for aerospace applications
- Underwater vehicle navigation

### Visual-Inertial Odometry (VIO)

- SLAM and visual odometry
- Camera-IMU sensor fusion
- Pose tracking for AR/VR

### Robotics

- Legged robot state estimation
- Aerial vehicle control
- Manipulation and motion planning

## 🌐 Related Resources

- **[Awesome invariant-and-equivariant filter-and-observer](https://github.com/LYRen1900/Awesome-invariant-and-equivariant-filter-and-observer)** - Another curated list with additional resources
- **[Awesome Visual SLAM](https://github.com/tzutalin/awesome-visual-slam)** - Visual SLAM resources
- **[Awesome Robotics](https://github.com/kiloreux/awesome-robotics)** - General robotics resources

## 🖥️ Local Development

To preview the website locally:

### Prerequisites

- Ruby (version 2.7 or higher recommended)
- Bundler gem

### Setup and Run

```bash
# Install dependencies
bundle install

# Serve the site locally using the development configuration
bundle exec jekyll serve --config _config_dev.yml

# Visit http://localhost:4000 in your browser
```

### Troubleshooting

**SSL Certificate Error with Remote Theme:**

If you encounter SSL certificate verification errors when using the default `_config.yml`, use the development configuration instead:

```bash
bundle exec jekyll serve --config _config_dev.yml
```

This uses a local theme instead of fetching from GitHub, avoiding SSL issues.

**Alternative Workaround (if needed):**

If you need to use the production config with the remote theme, you can disable SSL verification (⚠️ **use with caution - only in trusted local development environments**):

```bash
# macOS/Linux
SSL_CERT_FILE="" bundle exec jekyll serve

# Or set an environment variable
export SSL_CERT_FILE=""
bundle exec jekyll serve
```

**Warning:** Disabling SSL certificate verification removes security protections. Only use this workaround on trusted networks and for local development.

For more details on GitHub Pages setup, see [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md).

## 📝 Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit papers, resources, or corrections.

### How to Contribute

1. Fork this repository
2. Add your resource in the appropriate section
3. Ensure the formatting matches existing entries
4. Submit a pull request with a clear description

### Contribution Criteria

- Resources should be related to invariant or equivariant filtering
- Include proper citations with authors and year
- Provide working links to papers or resources
- Maintain the awesome list spirit: quality over quantity

## 👥 Contributors

This project originated at **Georgia Tech** and is maintained by the GTSAM community.

**Core Contributors:**

- **Rohan Bansal** - Initial curation and project setup
- **Frank Dellaert** - Project guidance and oversight

We welcome contributions from the community! See [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is released under Creative Commons Zero v1.0 Universal license.

---

**Maintained by the GTSAM community** | **Originated at Georgia Tech** | [Website](https://github.com/borglab/AwesomeEqF) | [Contribute](CONTRIBUTING.md)
