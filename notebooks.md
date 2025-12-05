---
layout: default
title: Notebooks
permalink: /notebooks/
---

# Example Notebooks

Interactive Jupyter notebooks demonstrating invariant and equivariant filtering techniques.

## 📓 Available Notebooks

### Getting Started

- **[Introduction to Invariant EKF](./notebooks/01_intro_to_iekf.ipynb)** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/borglab/AwesomeEqF/blob/main/notebooks/01_intro_to_iekf.ipynb)
  
  A gentle introduction to the Invariant Extended Kalman Filter with a simple attitude estimation example.

- **[Equivariant Filter Basics](./notebooks/02_equivariant_filter_basics.ipynb)** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/borglab/AwesomeEqF/blob/main/notebooks/02_equivariant_filter_basics.ipynb)
  
  Understanding the principles of equivariant filtering through hands-on examples.

### Advanced Topics

- **[Visual-Inertial Odometry with IEKF](./notebooks/03_vio_with_iekf.ipynb)** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/borglab/AwesomeEqF/blob/main/notebooks/03_vio_with_iekf.ipynb)
  
  Implementing a visual-inertial odometry system using the Invariant EKF.

## 🚀 Running Notebooks

### Option 1: Google Colab (Recommended)
Click the "Open in Colab" badge next to any notebook to run it in your browser without any setup.

### Option 2: Local Installation

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

## 📦 Dependencies

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

## 🤝 Contributing Notebooks

Have a great example to share? We'd love to include it!

1. Create your notebook following our [template](https://github.com/borglab/AwesomeEqF/blob/main/notebooks/notebook_template.ipynb)
2. Ensure it runs without errors
3. Add clear explanations and visualizations
4. Submit a pull request

See our [Contributing Guide](https://github.com/borglab/AwesomeEqF/blob/main/CONTRIBUTING.md) for more details.

---

<div style="background-color: #f6f8fa; padding: 1em; border-radius: 6px; margin-top: 2em;">
  <h3>💡 Tips for Learning</h3>
  <ul>
    <li>Start with the introduction notebooks to build foundational understanding</li>
    <li>Experiment by modifying parameters and observing the effects</li>
    <li>Read the referenced papers for deeper theoretical insights</li>
    <li>Ask questions via <a href="https://github.com/borglab/AwesomeEqF/issues">GitHub issues</a></li>
  </ul>
</div>
