# Drawings

Hand-drawn-style diagrams for posts, kept as SVG so they can be edited. Each embeds the Patrick Hand font (Google Fonts, Latin subset) as a base64 `@font-face`, so it renders the same anywhere. Boxes get a fraction of a degree of rotation for the sketchy feel.

Render to PNG, then convert to webp for `assets/images/`:

```bash
google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=1500,1280 --screenshot=out.png file://$PWD/name.svg
python3 -c "from PIL import Image; Image.open('out.png').convert('RGB').save('../../assets/images/name.webp','WEBP',quality=88)"
```

Match `--window-size` to the SVG's width and height. Captions below about 28px come out too small at the blog's column width.
