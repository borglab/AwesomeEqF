---
title: Examples and Implementations
---

# Implementations and Example Notebooks

This section collects **notebook implementations of key papers and ideas** in invariant and equivariant filtering.
All notebooks are rendered directly on the site via MyST / Jupyter Book, so you can see code, equations, and figures inline.

## 📓 Getting Started

- **Invariant EKF Basics** (`notebooks/01_intro_to_iekf.ipynb`)  
  A gentle introduction to the Invariant Extended Kalman Filter with a simple attitude estimation example.

- **Equivariant Filter Basics** (`notebooks/02_intro_to_eqf.ipynb`)  
  Understanding the principles of equivariant filtering through the same attitude estimation example.

## 🔬 Advanced Topics

- **Visual-Inertial Odometry with IEKF** (`notebooks/03_vio_with_iekf.ipynb`)  
  Implementing a visual-inertial odometry system using the Invariant EKF.

- **Visual-Inertial Odometry with EqF** (`notebooks/04_vio_with_eqf.ipynb`)  
  Implementing a visual-inertial odometry system using an EqF.


## 🚀 Running Notebooks Locally

```bash
# Clone the repository
git clone https://github.com/borglab/AwesomeEqF.git
cd AwesomeEqF

# Create a virtual environment using uv
uv init .
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv add -r notebooks/requirements.txt

cd notebooks

# Launch Jupyter
jupyter notebook
```

## 🤝 Contributing Implementations

If you would like to teach about a topic in the realm of EqFs, please create a notebook!

1. Create your notebook following our existing style in `notebooks/`.
2. Ensure it runs without errors from a clean environment.
3. Add clear explanations and visualizations.
4. Submit a pull request.

See our [Contributing Guide](CONTRIBUTING.md) for more details.
