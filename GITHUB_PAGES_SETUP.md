# GitHub Pages Setup Instructions

This document explains how to enable GitHub Pages for the AwesomeEqF repository.

## Quick Setup

1. Go to the repository settings: https://github.com/borglab/AwesomeEqF/settings/pages

2. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select your main/master branch
   - **Folder**: Select "/ (root)"

3. Click "Save"

4. Wait a few minutes for the site to build (you'll see a notification)

5. The site will be available at: https://borglab.github.io/AwesomeEqF

## What Gets Published

The GitHub Pages site includes:

- **Homepage** (`index.md`): Main landing page with latest blog posts
- **Blog** (`blog.md`): List of all blog posts
- **Notebooks** (`notebooks.md`): Interactive Jupyter notebooks with Colab links
- **Blog Posts** (`_posts/`):
  - Welcome post
  - IEKF tutorial
  - EqF introduction

## File Structure

```
/
├── _config.yml           # Jekyll configuration
├── _layouts/             # Custom page layouts
│   └── default.html
├── _posts/               # Blog posts (auto-discovered by Jekyll)
│   ├── 2024-11-01-introduction-to-eqf.md
│   ├── 2024-11-15-understanding-iekf.md
│   └── 2024-12-02-welcome-to-awesomeeqf.md
├── index.md              # Homepage
├── blog.md               # Blog listing
├── notebooks.md          # Notebooks listing
└── notebooks/            # Jupyter notebooks
    ├── 01_intro_to_iekf.ipynb
    ├── 02_equivariant_filter_basics.ipynb
    └── 03_vio_with_iekf.ipynb
```

## Customization

To customize the site:

1. **Theme**: Edit `_config.yml` to change the theme
2. **Colors**: Modify the CSS in `_layouts/default.html`
3. **Navigation**: Update links in `_layouts/default.html`
4. **Content**: Add new blog posts in `_posts/` or edit existing pages

## Adding New Blog Posts

Create a new file in `_posts/` with the format:
```
YYYY-MM-DD-title-of-post.md
```

Include this front matter at the top:
```yaml
---
layout: default
title: "Your Post Title"
date: YYYY-MM-DD
categories: tutorial
author: Your Name
excerpt: "Brief description"
---

# Your Post Title

Content here...
```

## Adding New Notebooks

1. Create the notebook in `notebooks/`
2. Update `notebooks.md` to include a link
3. Optional: Add a Colab badge for easy running

## Testing Locally

To test the site locally before deploying:

### Quick Start (Recommended)

```bash
# Install dependencies
bundle install

# Run Jekyll server with development configuration
bundle exec jekyll serve --config _config_dev.yml

# Visit http://localhost:4000 in your browser
```

The `_config_dev.yml` file is configured for local development and avoids SSL certificate issues by using a local theme instead of a remote theme.

### Using Production Configuration

If you need to test with the production configuration (`_config.yml`), be aware that it uses a remote theme which may cause SSL certificate errors on some systems:

```bash
bundle exec jekyll serve

# Visit http://localhost:4000/AwesomeEqF
```

**Note:** The production config uses a different baseurl, so the site will be at `/AwesomeEqF` path.

### SSL Certificate Troubleshooting

If you encounter SSL certificate verification errors like:
```
SSL_connect returned=1 errno=0 state=error: certificate verify failed
```

**Solution 1: Use Development Config (Recommended)**
```bash
bundle exec jekyll serve --config _config_dev.yml
```

**Solution 2: Disable SSL Verification (Use with caution)**
```bash
# macOS/Linux
SSL_CERT_FILE="" bundle exec jekyll serve

# Windows PowerShell
$env:SSL_CERT_FILE=""; bundle exec jekyll serve
```

**Solution 3: Update Ruby SSL Certificates**
```bash
# macOS with Homebrew
brew install openssl
brew link --force openssl

# Update Ruby certificates
gem install certified
```

## Troubleshooting

### Local Development Issues

**SSL Certificate Errors:**
See the "SSL Certificate Troubleshooting" section under "Testing Locally" above. The recommended solution is to use the development configuration:
```bash
bundle exec jekyll serve --config _config_dev.yml
```

### Site not building?
- Check GitHub Actions tab for build errors
- Ensure `_config.yml` is valid YAML
- Verify all links use `relative_url` or `absolute_url` filters

### Pages not showing up?
- Blog posts must be in `_posts/` directory
- Filenames must follow `YYYY-MM-DD-title.md` format
- Posts must have valid front matter

### Links broken?
- Use `{{ '/path' | relative_url }}` for internal links
- Check `baseurl` in `_config.yml` matches repository name

## Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Jekyll Themes](https://pages.github.com/themes/)

## Support

For issues or questions:
- Open an issue on GitHub
- Check Jekyll build logs in Actions tab
- Review GitHub Pages documentation
