---
title: Papers and Reading
---

# Papers and Reading Path

This page collects key papers on invariant and equivariant filtering, organized as a **reading path** that starts from the basics and gradually moves to more advanced and application-focused work.

The goal is to help you answer:

- **What should I read first?**
- **How do IEKF and EqF relate?**
- **Where do I go for applications like VIO or navigation?**

## 1. Foundations of Invariant and Equivariant Filtering

### 1.1 Core IEKF Theory

- **[Invariant Extended Kalman Filter: theory and application to a velocity-aided attitude estimation problem](http://www.silvere-bonnabel.com/pdf/CDC2009IEKF.pdf)** (2009)  
  _Silvère Bonnabel, Philippe Martin, Pierre Rouchon_  
  The seminal paper introducing the IEKF, showing improved consistency for attitude estimation.

- **[Non-linear state error based extended Kalman filters with applications to navigation](https://theses.hal.science/tel-01344622/)** (2013)  
  _Axel Barrau_  
  Comprehensive PhD thesis on IEKF theory and applications.

- **[The Invariant Extended Kalman Filter as a Stable Observer](https://arxiv.org/abs/1410.1465)** (2016)  
  _Axel Barrau, Silvère Bonnabel_  
  Rigorous stability analysis of the IEKF, establishing conditions for local asymptotic stability.

### 1.2 Symmetry-Preserving and Geometric Observers

- **[Symmetry-preserving observers](https://ieeexplore.ieee.org/document/1339919)** (2004)  
  _A. Saccon, A. P. Aguiar, A. M. Pascoal_  
  Early work on observer design that preserves system symmetries.

- **[Nonlinear Complementary Filters on the Special Orthogonal Group](https://arxiv.org/abs/0806.0620)** (2008)  
  _Robert Mahony, Tarek Hamel, Jean-Michel Pflimlin_  
  Nonlinear complementary filter on SO(3) that strongly influenced later invariant and equivariant attitude observers.

- **[Observer Design on the Special Euclidean Group SE(3)](https://ieeexplore.ieee.org/document/6160453)** (2011)  
  _Robert Mahony, Tarek Hamel_  
  Early work on observer design for pose estimation on SE(3).

## 2. Equivariant Filters (EqF) and Unified Viewpoints

### 2.1 Equivariant Filter Design

- **[Equivariant Filter (EqF)](https://arxiv.org/abs/2010.14666)** (2021)  
  _Pieter van Goor, Tarek Hamel, Robert Mahony_  
  Foundational paper on equivariant filtering for systems on homogeneous spaces.

- **[EQUIVARIANT FILTER (EQF): A GENERAL FILTER DESIGN FOR SYSTEMS ON HOMOGENEOUS SPACES](https://arxiv.org/pdf/2107.05193)** (2021)  
  _Pieter van Goor, Tarek Hamel, Robert Mahony_  
  Extended version with detailed theoretical development.

- **[Equivariant Filter Design for Kinematic Systems on Lie Groups](https://www.sciencedirect.com/science/article/pii/S240589632100642X)** (2021)  
  _Alessandro Saccon et al._  
  Framework for embedding kinematic systems on Lie groups into equivariant systems.

### 2.2 Equivariant Systems and IEKF–EqF Connections

- **[Equivariant Systems Theory and Observer Design](https://arxiv.org/abs/2006.08276)** (2020)  
  _Pieter van Goor, Robert Mahony_  
  Unified framework connecting invariant and equivariant approaches.

- **[The Difference between the Left and Right Invariant Extended Kalman Filter](https://arxiv.org/abs/2507.04568)** (2024)  
  Explores when left and right IEKF variants yield identical performance with proper reset steps.

## 3. Applications and Advanced Topics

### 3.1 Navigation, INS/GNSS, and IMU Integration

- **[An Iterated Equivariant Filter and Its Application in Tightly Coupled GNSS/INS](https://ieeexplore.ieee.org/document/10979539)** (2024)  
  Combines covariance reset steps for improved performance in tightly coupled systems.

- **[Invariant Kalman Filtering for Visual-Inertial SLAM](https://ieeexplore.ieee.org/document/8455807)** (2018)  
  Application of IEKF to visual-inertial odometry and SLAM.

### 3.2 Visual-Inertial Odometry (VIO) and Robotics

These and related works build on the above theory to address:

- Visual-inertial odometry and SLAM
- Attitude estimation for aerospace applications
- Legged robot and aerial vehicle state estimation
- Pose tracking for AR/VR and robotics navigation

## 4. Background and Related Reading

- **[Lie Groups for 2D and 3D Transformations](https://ethaneade.com/lie.pdf)**  
  _Ethan Eade_ — A concise primer on Lie groups in robotics, highly recommended background.

- **[Awesome invariant-and-equivariant filter-and-observer](https://github.com/LYRen1900/Awesome-invariant-and-equivariant-filter-and-observer)**  
  Another curated list with additional resources.

For software and practical implementations, see the **Implementations / Notebooks** section of this site and the GTSAM EKF variants documentation.
