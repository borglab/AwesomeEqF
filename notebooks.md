---
title: Examples and Implementations
---

# Implementations and Example Notebooks

This section collects **notebook implementations of key papers and ideas** in invariant and equivariant filtering.
All notebooks are rendered directly on the site via MyST / Jupyter Book, so you can see code, equations, and figures inline.

## 📓 Getting Started

- **Introduction to Invariant EKF** (`notebooks/01_intro_to_iekf.ipynb`)  
  A gentle introduction to the Invariant Extended Kalman Filter with a simple attitude estimation example.

- **Equivariant Filter Basics** (`notebooks/02_equivariant_filter_basics.ipynb`)  
  Understanding the principles of equivariant filtering through hands-on examples.

## 🔬 Advanced Topics

- **Visual-Inertial Odometry with IEKF** (`notebooks/03_vio_with_iekf.ipynb`)  
  Implementing a visual-inertial odometry system using the Invariant EKF.

These notebooks also appear individually in the navigation and are executed (or cached) by Jupyter Book when the site is built.

## 🚀 Running Notebooks Locally

```bash
# Clone the repository
git clone https://github.com/borglab/AwesomeEqF.git
cd AwesomeEqF/notebooks

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

## 📦 Notebook Dependencies

Most notebooks require:

- NumPy
- SciPy
- Matplotlib
- Jupyter

Some advanced notebooks may also use:

- GTSAM Python bindings
- OpenCV
- Pandas

See each notebook's requirements cell for specific dependencies.

## 🤝 Contributing Implementations

Have a great implementation or teaching notebook to share?

1. Create your notebook following our template (or existing style) in `notebooks/`.
2. Ensure it runs without errors from a clean environment.
3. Add clear explanations and visualizations.
4. Submit a pull request.

See our [Contributing Guide](https://github.com/borglab/AwesomeEqF/blob/main/CONTRIBUTING.md) for more details.
