# GitHub Copilot Instructions for AwesomeEqF

## Project Overview

This repository is a curated "Awesome List" for Invariant and Equivariant Filtering resources, maintained by the GTSAM community at Georgia Tech. It's a Jekyll-based GitHub Pages site that serves as a comprehensive collection of papers, software, tutorials, and applications related to invariant and equivariant filtering for state estimation on manifolds and Lie groups.

## Project Structure

```
.
├── README.md              # Main content - rendered as homepage
├── CONTRIBUTING.md        # Contribution guidelines
├── _config.yml           # Jekyll production configuration
├── _config_dev.yml       # Jekyll development configuration
├── _layouts/             # Jekyll layout templates
├── _posts/               # Blog posts about EqF and IEKF
├── notebooks/            # Jupyter notebooks with examples
├── index.md              # Homepage template
├── blog.md              # Blog index page
├── notebooks.md         # Notebooks index page
└── Gemfile              # Ruby dependencies
```

## Build and Development Commands

### Setup
```bash
# Install dependencies
bundle install
```

### Local Development
```bash
# Serve the site locally (development config - avoids SSL issues)
bundle exec jekyll serve --config _config_dev.yml

# Visit http://localhost:4000/AwesomeEqF in your browser
```

### Testing
```bash
# Build the site to check for errors
bundle exec jekyll build

# Build with production config
bundle exec jekyll build --config _config.yml
```

## Content Guidelines

### Adding Papers and Resources

Follow the established formatting in README.md:

**For papers:**
```markdown
- **[Paper Title](link-to-paper)** (Year)  
  *Author Names*  
  Brief description of the contribution.
```

**For software/libraries:**
```markdown
- **[Project Name](link-to-repo)** - Brief description
  - Key features or variants
```

### Contribution Standards

1. **Quality over Quantity**: Only add high-quality, relevant resources
2. **Proper Citations**: Include authors, year, and working links
3. **Chronological Order**: Maintain oldest to newest within sections
4. **Working Links**: Verify all links are accessible and prefer official sources (arXiv, IEEE Xplore, author pages)
5. **Clear Descriptions**: Provide concise, informative descriptions

### Sections in README.md

- **Foundational Papers**: Seminal works (IEKF, EqF basics)
- **Recent Advances**: Papers from last 3-5 years
- **Software and Libraries**: Open-source implementations (especially GTSAM)
- **Tutorials and Talks**: Educational materials
- **Applications**: Domain-specific use cases
- **Related Resources**: Adjacent topics and awesome lists

## Coding Standards

### Markdown
- Use proper heading hierarchy (H1 for main title, H2 for sections, etc.)
- Include emoji icons for visual clarity (existing pattern: 📚, 🎯, 📖, 🚀, 💻, etc.)
- Maintain consistent formatting with existing entries
- Use relative links for internal pages, absolute for external resources

### Jekyll/Liquid
- Follow existing template patterns in `_layouts/`
- Keep templates simple and maintainable
- Use site variables from `_config.yml`

### Blog Posts
- Use YAML frontmatter with: title, date, author, categories
- Save in `_posts/` with format: `YYYY-MM-DD-title.md`
- Keep technical content accurate and accessible

### Jupyter Notebooks
- Include clear markdown explanations
- Add appropriate headers and section breaks
- Ensure all code cells run without errors
- Save in `notebooks/` directory

## Review Criteria

When reviewing contributions:
1. ✅ Is the resource relevant to invariant/equivariant filtering?
2. ✅ Is the formatting consistent with existing entries?
3. ✅ Are links working and pointing to official sources?
4. ✅ Is the description clear and accurate?
5. ✅ Is it in the correct section?
6. ✅ Does it maintain chronological order?
7. ❌ Is it a duplicate of an existing entry?
8. ❌ Is it unpublished work without a preprint?

## Common Tasks for Copilot

### Good Tasks for Copilot
- Adding new papers to appropriate sections
- Fixing broken links
- Updating formatting to match style guidelines
- Adding new blog posts about EqF/IEKF topics
- Creating or updating Jupyter notebooks
- Improving documentation clarity
- Adding new sections following existing patterns
- Updating dependencies in Gemfile

### Tasks Requiring Human Review
- Removing entries (requires discussion)
- Major restructuring of sections
- Changing core design or layout
- Making judgments on paper quality or relevance
- Resolving conflicting contributions

## Important Files and Context

- **README.md**: The main content file - this is what users see
- **CONTRIBUTING.md**: Guidelines for contributors - keep aligned with README
- **_config.yml**: Jekyll configuration - be careful with changes
- **_config_dev.yml**: Local development config (uses local theme to avoid SSL issues)

## Links to Documentation

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Awesome List Guidelines](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md)
- [GTSAM Project](https://github.com/borglab/gtsam)
- [GTSAM EKF Variants Documentation](https://borglab.github.io/gtsam/ekf-variants/)

## Notes for AI Agents

- This is primarily a **content curation** project, not a software development project
- Focus on maintaining high quality, relevant resources
- Preserve the established formatting and organizational structure
- When in doubt about a resource's relevance, err on the side of caution
- All contributions should align with the "Awesome List" philosophy: quality over quantity
- The site is built with Jekyll but doesn't require complex code changes
- Most contributions will be to README.md and occasionally to blog posts or notebooks
