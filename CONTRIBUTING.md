---
title: Contributing
---

## How Can I Contribute to Awesome Equivariant Filtering?

### Adding a New Resource

1. **Fork the repository** and create a new branch from `main`
2. **Add your resource** in the appropriate section of README.md
3. **Follow the formatting style** of existing entries
4. **Submit a pull request** with a clear description

### Formatting Guidelines

**For papers:**

```markdown
- **[Paper Title](link-to-paper)** (Year)  
  _Author Names_  
  Brief description of the contribution.
```

**For software/libraries:**

```markdown
- **[Project Name](link-to-repo)** - Brief description
  - Key features or variants
```

### What to Include

✅ **Do include:**

- Peer-reviewed papers on invariant or equivariant filtering
- Open-source software implementations
- Educational resources (tutorials, lectures, documentation)
- Applications demonstrating these techniques
- Related awesome lists or curated resources

❌ **Don't include:**

- Unpublished work without preprints
- Commercial or closed-source software
- Duplicate entries
- Resources unrelated to invariant/equivariant filtering

### Sections

Resources should be added to appropriate sections:

- **Foundational Papers**: Seminal works that established the field
- **Recent Advances**: Papers from the last 3-5 years
- **Software and Libraries**: Open-source implementations
- **Tutorials and Talks**: Educational materials
- **Applications**: Domain-specific use cases
- **Related Resources**: Adjacent topics and lists

### Blog Posts

We welcome focused blog posts that:

- Explain concepts in invariant / equivariant filtering
- Summarize or contextualize specific papers
- Walk through implementations or examples (ideally linked to notebooks)

To add a blog post:

1. **Create a new Markdown file** under the `blog/` folder, for example:  
   `blog/2025-12-20-iekf-vs-eqf-notes.md`

2. **Add minimal front matter** with a title:

   ```yaml
   ---
   title: Your Post Title
   ---
   ```

3. **Start the post** with an optional header block:

   ```markdown
   > **Date:** YYYY-MM-DD  
   > **Author:** Your Name
   ```

4. **Write the content** in regular Markdown / MyST (equations, code blocks, images are all fine).

5. **Wire it into navigation** by updating `myst.yml`:

   ```yaml
   - file: blog.md
     children:
       - file: blog/2025-12-18-welcome.md
       - file: blog/2025-12-20-iekf-vs-eqf-notes.md
   ```

6. Optionally, **add a link** to the new post under **Latest Posts** in `blog.md`.

### Quality Standards

- Links must be working and publicly accessible
- Prefer official sources (author pages, arXiv, IEEE Xplore)
- Include DOI or arXiv links when available
- Provide clear, concise descriptions
- Maintain chronological order within sections (oldest to newest)

## Suggesting Improvements

If you have ideas for improving the structure or organization:

1. Open an issue describing your suggestion
2. Explain the benefit to users
3. Discuss with maintainers before making large changes

## Reporting Issues

Found a broken link or error? Please:

1. Open an issue with a descriptive title
2. Provide the section and entry name
3. Include the correction or working link if known

## Code of Conduct

Be respectful and constructive. This is a community resource, and we're all here to learn and share knowledge about this fascinating field!

## Questions?

Feel free to open an issue for any questions about contributing.

Thank you for helping make this resource better! 🙏
