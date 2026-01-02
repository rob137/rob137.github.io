# Rob's Blog

A personal blog built with Jekyll, hosted on GitHub Pages.

## Quick Start

### Writing a new post

1. Create a file in `_posts/` with the format: `YYYY-MM-DD-title-of-post.md`
2. Add front matter at the top:

```yaml
---
layout: post
title: "Your Post Title"
date: 2026-01-02
tags: [optional, tags]
---
```

3. Write your content in Markdown below the front matter
4. Commit and push to GitHub

### Deploying to GitHub Pages

1. Create a repository named `rob137.github.io` on GitHub
2. Push this directory to that repository:

```bash
cd ~/sandpit/blog
git init
git add .
git commit -m "Initial blog setup"
git remote add origin git@github.com:rob137/rob137.github.io.git
git branch -M main
git push -u origin main
```

3. Go to repository Settings > Pages > ensure "Deploy from branch" is selected (main branch)
4. Your site will be live at https://rob137.github.io within a few minutes

### Local development (optional)

If you want to preview locally before pushing:

```bash
# Install dependencies (one time)
bundle install

# Run local server
bundle exec jekyll serve

# View at http://localhost:4000
```

Requires Ruby to be installed. But honestly, you can skip this and just push to GitHub - the preview there is fast enough.

## File structure

```
blog/
├── _config.yml      # Site configuration
├── _layouts/        # Page templates
│   ├── default.html # Base layout
│   └── post.html    # Blog post layout
├── _posts/          # Your blog posts (Markdown)
├── assets/css/      # Stylesheets
├── index.html       # Home page
├── about.md         # About page
└── feed.xml         # RSS feed
```

## Customization

- **Site title/description**: Edit `_config.yml`
- **Styling**: Edit `assets/css/style.css`
- **Layout**: Edit files in `_layouts/`
- **Navigation**: Edit the nav in `_layouts/default.html`

## Useful Markdown features

```markdown
# Heading 1
## Heading 2

**bold** and *italic*

[Link text](https://example.com)

![Image alt text](/path/to/image.jpg)

> Blockquote

- Bullet list
- Item 2

1. Numbered list
2. Item 2

`inline code`

​```python
# Code block with syntax highlighting
def hello():
    print("Hello, world!")
​```
```
