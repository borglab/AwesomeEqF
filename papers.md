---
title: Papers and Reading
---

# Papers and Reading Path

This page collects and categorizes key papers on invariant and equivariant filtering.

## 1. Foundations of Invariant and Equivariant Filtering

### 1.1 Core IEKF Theory

- **[Invariant Extended Kalman Filter: theory and application to a velocity-aided attitude estimation problem](https://minesparis-psl.hal.science/hal-00494342v1/document)** (2009)  
  _Silvère Bonnabel, Philippe Martin, Pierre Rouchon_  
  The seminal paper introducing the IEKF, showing improved consistency for attitude estimation.

- **[Non-linear state error based extended Kalman filters with applications to navigation](https://pastel.hal.science/tel-01344622v1/document)** (2013)  
  _Axel Barrau_  
  Comprehensive PhD thesis on IEKF theory and applications.

- **[The Invariant Extended Kalman Filter as a Stable Observer](https://arxiv.org/abs/1410.1465)** (2016)  
  _Axel Barrau, Silvère Bonnabel_  
  Rigorous stability analysis of the IEKF, establishing conditions for local asymptotic stability.

- **[The Difference between the Left and Right Invariant Extended Kalman Filter](https://arxiv.org/abs/2507.04568)** (2025)  
  _Yixiao Ge et al._  
  A recent clarification paper proving that left and right IEKFs are mathematically equivalent when the reset step is correctly implemented, debunking the myth that handedness must match measurement physics.

### 1.2 Symmetry-Preserving and Geometric Observers

- **[Symmetry-preserving observers](https://arxiv.org/abs/math/0612193)** (2004)  
  _A. Saccon, A. P. Aguiar, A. M. Pascoal_  
  Early work on observer design that preserves system symmetries.

- **[Nonlinear Complementary Filters on the Special Orthogonal Group](https://hal.science/hal-00488376v1/document)** (2008)  
  _Robert Mahony, Tarek Hamel, Jean-Michel Pflimlin_  
  Nonlinear complementary filter on SO(3) that strongly influenced later invariant and equivariant attitude observers.

- **[Observer Design on the Special Euclidean Group SE(3)](https://trumpf.id.au/pubs/Hua_Zamani_Trumpf_Mahony_Hamel_CDC2011.pdf)** (2011)  
  _Minh-Duc Hua, Mohammad Zamani, Jochen Trumpf, Robert Mahony, Tarek Hamel_  
  Early work on observer design for pose estimation on SE(3).

## 2. Equivariant Filters (EqF) and Unified Viewpoints

### 2.1 Equivariant Filter Design

- **[Equivariant Filter (EqF)](https://arxiv.org/abs/2010.14666)** (2020/2021)  
  _Pieter van Goor, Tarek Hamel, Robert Mahony_  
  Foundational paper on equivariant filtering for systems on homogeneous spaces.

- **[Equivariant Filter (EqF): A General Filter Design for Systems on Homogeneous Spaces](https://arxiv.org/abs/2107.05193)** (2021)  
  _Pieter van Goor, Tarek Hamel, Robert Mahony_  
  Extended version with detailed theoretical development.

- **[Equivariant Filter Design for Kinematic Systems on Lie Groups](https://arxiv.org/abs/2004.00828)** (2021)  
  _Robert Mahony, Jochen Trumpf_  
  Framework for embedding kinematic systems on Lie groups into equivariant systems.

### 2.2 Advanced EqF Architectures

- **[MSCEqF: A Multi State Constraint Equivariant Filter for Vision-Aided Inertial Navigation](https://arxiv.org/abs/2311.11649)** (2023/2024)  
  _Alessandro Fornasier, Pieter van Goor, Robert Mahony, Stephan Weiss_  
  Extends the MSCKF (Multi-State Constraint Kalman Filter) to the equivariant framework, allowing for consistent VIO with onboard calibration.

- **[APEqF: An Equivariant Filter for ArduPilot](https://www.aau.at/wp-content/uploads/2024/01/APEqF.pdf)** (2024)  
  _Alessandro Fornasier, Yixiao Ge, Pieter van Goor, Martin Scheiber, Andrew Tridgell, Robert Mahony_  
  A novel EqF formulation exploiting Semi-Direct-Bias symmetry for multi-sensor fusion, specifically designed to handle GNSS outliers and shifts in open-source autopilot software.

- **[Equivariant Symmetries for Aided Inertial Navigation](https://arxiv.org/abs/2407.14297)** (TBD)  
  _Alessandro Fornasier_  
  Dissertation that advances the understanding of equivariant symmetries in the context of inertial navigation systems.

- **[Overcoming Bias: Equivariant Filter Design for Biased Attitude Estimation with Online Calibration](https://arxiv.org/abs/2209.12038)** (TBD)  
  _Alessandro Fornasier, Yonhon Ng, Christian Brommer, Christoph Böhm, Robert Mahony, Stephan Weiss_  
  Paper that introduces a new generic formulation for a gyroscope aided attitude estimator, taking advantage of states in a single equivariant geometric structure.

## 3. Applications and Advanced Topics

### 3.1 Legged Robotics & Contact Estimation

- **[Contact-Aided Invariant Extended Kalman Filtering for Legged Robot State Estimation](https://arxiv.org/abs/1904.09251)** (2018)  
  _Ross Hartley, Maani Ghaffari, Ryan M. Eustice, Jessy W. Grizzle_  
  The “killer app” for InEKF, using contact constraints as invariant measurements.

- **[Adaptive Invariant Extended Kalman Filter for Legged Robot State Estimation](https://arxiv.org/abs/2510.16755)** (2025)  
  _Kyung-Hwan Kim, DongHyun Ahn, Dong-hyun Lee, et al._  
  Proposes an adaptive mechanism to improve proprioceptive state estimation and handle slip more robustly than standard InEKF.

- **[Legged Robot State Estimation With Invariant Extended Kalman Filter Using Neural Measurement Network](https://arxiv.org/abs/2402.00366)** (2024)  
  _Donghoon Youm, Hyunsik Oh, Suyoung Choi, Hyeongjun Kim, Jemin Hwangbo_  
  A hybrid approach integrating a Neural Measurement Network (NMN) with an InEKF to bridge the sim-to-real gap in terrain-aware state estimation.

### 3.2 Visual-Inertial Odometry (VIO)

- **[Invariant Kalman Filtering for Visual-Inertial SLAM](https://hal.science/hal-01588669v2/document)** (2018)  
  _Martin Brossard, Silvère Bonnabel, Axel Barrau_  
  Application of IEKF to visual-inertial odometry.

- **[EqVIO: An Equivariant Filter for Visual-Inertial Odometry](https://arxiv.org/abs/2205.01980)** (2023)  
  _Pieter van Goor, Robert Mahony_  
  The definitive journal paper on EqVIO, demonstrating superior consistency over standard VIO (like VINS-Mono) by utilizing an equivariant output approximation.

- **[SP-VIO: Symmetry-Preserving Visual-Inertial Odometry](https://arxiv.org/abs/2411.07551)** (2024)  
  _Xueyu Du, Lilian Zhang, Chengjun Ji, Xinchan Luo, Huaiyi Zhang, Maosong Wang, Wenqi Wu, Jun Mao_  
  A new framework combining neural networks for bias learning with symmetry-preserving filters to handle long-term visual deprivation.

## 4. General Equivariance

### 4.1 Equivariant Diffusion Policies (Robot Learning)

- **[Equivariant Diffusion Policy](https://equidiff.github.io/)** (2024)  
  _Dian Wang, Stephen Hart, David Surovik, Tarik Kelestemur, Haojie Huang, Haibo Zhao, Mark Yeatman, Jiuguang Wang, Robin Walters, Robert Platt_  
  Introduces a diffusion policy that leverages domain symmetries (like SO(2)) to drastically improve sample efficiency in imitation learning.

- **[EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable and Data Efficient Learning](https://arxiv.org/abs/2407.01479)** (2024)  
  _Jingyun Yang, Zi-ang Cao, Congyue Deng, Rika Antonova, Shuran Song, Jeannette Bohg_  
  Extends equivariance to the SIM(3) group (translation, rotation, and scale), allowing robots to learn manipulation tasks that generalize to objects of different sizes and poses.

- **[Spherical Diffusion Policy](https://arxiv.org/abs/2507.01723)** (2025)  
  _Xupeng Zhu, Fan Wang, Robin Walters, Jane Shi_  
  A state-of-the-art policy that embeds the diffusion process in spherical Fourier space to achieve exact SE(3) equivariance for complex 3D manipulation.

- **[ET-SEED: Efficient Trajectory-Level SE(3) Equivariant Diffusion Policy](https://arxiv.org/abs/2411.03990)** (TBD)  
  _Chenrui Tie, Yue Chen, Ruihai Wu, Boxuan Dong, Zeyi Li, Chongkai Gao, Hao Dong_  
  Introduction of a SE(3)-equivariant diffusion policy that generates robot trajectories more efficiently and generalizes better with less data.

- **[Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation](https://arxiv.org/abs/2309.02685)** (2023)  
  _Hyunwoo Ryu, Jiwoo Kim, Hyunseok An, Junwoo Chang, Joohwan Seo, Taehan Kim, Yubin Kim, Chaewon Hwang, Jongeun Choi, Roberto Horowitz_  
  Bi-equivariant denoising generative modeling on SE(3) for visual robotic manipulation.

- **[A Practical Guide for Incorporating Symmetry in Diffusion Policy](https://arxiv.org/abs/2505.13431)** (2025)  
  _Dian Wang, Boce Hu, Shuran Song, Robin Walters, Robert Platt_  
  Practical guidance on incorporating symmetry into diffusion policies without requiring fully equivariant architectures.

## 5. Surveys and Tutorials

- **[A Micro Lie Theory for State Estimation in Robotics](https://arxiv.org/abs/1812.01537)** (2018)  
  _Joan Solà, Jeremie Deray, Dinesh Atchuthan_  
  The essential primer for engineers entering the field.

- **[Symmetry in Robot Learning: A Survey](https://pmc.ncbi.nlm.nih.gov/articles/PMC9515513/pdf/frobt-09-969380.pdf)** (2022)  
  _Maani Ghaffari et al._  
  Comprehensive overview of how symmetry is used in perception, state estimation, and control.

- **[SE(3)-Equivariant Robot Learning and Control: A Tutorial Survey](https://arxiv.org/abs/2503.09829)** (2025)  
  _Joohwan Seo et al._  
  A recent tutorial unifying mathematical notation for group equivariant deep learning and geometric control.

---

For software and practical implementations, see the **Implementations / Notebooks** section of this site and the GTSAM EKF variants documentation.
