# Awesome Equivariant Filtering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**AwesomeEqF** is a community hub for invariant and equivariant filtering on manifolds and Lie groups.  

See [the website](http://borglab.github.io/AwesomeEqF) for papers, blog posts, and examples!

## Building locally

### 1. Clone the repository

```bash
git clone https://github.com/borglab/AwesomeEqF
cd AwesomeEqF
```

### 2. Install dependencies

From the repository root:

```bash
uv sync
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Build the site with live preview

```bash
jupyter-book --
```

## 📝 Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to:

- Add or refine papers in the **Papers and Reading** page
- Contribute **notebook implementations** in `notebooks/`
- Improve explanations, figures, or examples on the website

## 👥 Contributors

This project originated at **Georgia Tech** and is maintained by the GTSAM community.

**Core Contributors:**

- **Rohan Bansal** – Initial curation and project setup
- **Frank Dellaert** – Project guidance and oversight

## 📄 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is released under Creative Commons Zero v1.0 Universal license.
