# Drawings

Hand-drawn-style diagrams for posts, kept as SVG so they can be edited. Each embeds the Patrick Hand font (Google Fonts, Latin subset) as a base64 `@font-face`, so it renders the same anywhere. Boxes get a fraction of a degree of rotation for the sketchy feel.

Render to PNG, then convert to webp for `assets/images/`:

```bash
google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=1500,1280 --screenshot=out.png file://$PWD/name.svg
python3 -c "from PIL import Image; Image.open('out.png').convert('RGB').save('../../assets/images/name.webp','WEBP',quality=88)"
```

Match `--window-size` to the SVG's width and height. Captions below about 28px come out too small at the blog's column width.

Dark variants: the embedded `<style>` sets `text{fill:#1f1f1f}`, and CSS beats the `fill` attribute, so a dark file must replace `#1f1f1f` everywhere (defs included), not just on the shapes. The `gen-*.py` scripts here build both themes from one layout; run them from any directory, they write the SVGs next to themselves. Posts carry two `<img>` tags, `drawing-light` and `drawing-dark`, and `style.css` swaps them on `html.dark-mode`.

Captions are labels, not slogans. Name the parts and the arrows; leave the argument to the post. Rob, 8 Oct 2026: "less is so often more".

Every `<img>` carries `width` and `height` in real pixels of the webp so the page does not shift when it loads; CSS keeps `height: auto`.
