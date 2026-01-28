#!/usr/bin/env python3
"""Generate images for blog posts using OpenAI gpt-image-1.5"""

import os
import base64
import requests
from pathlib import Path

API_KEY = os.environ.get('OPENAI_API_KEY')
if not API_KEY:
    raise ValueError("OPENAI_API_KEY not set")

IMAGES_DIR = Path(__file__).parent.parent / "assets" / "images"

# Posts and their image prompts
POSTS = [
    {
        "slug": "books-as-compressed-prompts",
        "filename": "library-glow.webp",
        "prompt": "A vintage library with glowing books on shelves. Ethereal streams of light emanate from several book spines and converge into a single bright focal point in the center. The atmosphere suggests compressed knowledge being accessed and expanded. Warm amber lighting, dust particles visible in light beams, photorealistic cinematic style."
    },
    {
        "slug": "crossing-the-horizon",
        "filename": "event-horizon.webp",
        "prompt": "An abstract visualization of crossing an event horizon. A silhouette of a person standing at the edge of a cosmic threshold - one side showing familiar territory, the other side showing a warped, luminous realm of possibilities. Deep blues and purples with bright white light at the boundary. Ethereal, contemplative, cinematic science fiction aesthetic."
    },
    {
        "slug": "how-i-keep-up",
        "filename": "information-streams.webp",
        "prompt": "A person calmly standing in a vast river of flowing digital information streams. Glowing data particles and text fragments flow around them like water. Some streams are highlighted/selected while others fade into the background, suggesting curation. Cool blue tones with warm accent highlights. Modern, clean, contemplative aesthetic."
    },
    {
        "slug": "how-this-blog-exists",
        "filename": "voice-to-code.webp",
        "prompt": "Sound waves emanating from a person speaking, transforming into lines of code and website elements as they travel through the air. The person is standing casually in a kitchen, not looking at any screen. Voice waves morph into text and code mid-air. Warm domestic lighting contrasted with cool digital elements. Photorealistic with subtle magical realism."
    },
    {
        "slug": "intermediary-times",
        "filename": "transition-period.webp",
        "prompt": "A landscape split between two eras - on one side, an industrial revolution scene with smokestacks and steam engines, on the other, a gleaming futuristic cityscape. In the middle, a turbulent transition zone where the two worlds collide and blend, showing both creation and destruction. Dramatic lighting, painterly epic style reminiscent of romantic era paintings meeting science fiction."
    },
]

def generate_image(prompt: str, filename: str) -> Path:
    """Generate an image and save it to the images directory"""
    print(f"Generating: {filename}")

    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        json={
            'model': 'gpt-image-1.5',
            'prompt': prompt,
            'n': 1,
            'size': '1536x1024',
            'quality': 'medium'
        },
        timeout=120
    )

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
        raise Exception(f"API error: {response.status_code}")

    data = response.json()
    b64_data = data['data'][0]['b64_json']

    # Decode and save
    image_data = base64.b64decode(b64_data)
    output_path = IMAGES_DIR / filename

    # Convert PNG to WebP using PIL if available, otherwise save as PNG
    try:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(image_data))
        img.save(output_path, 'WEBP', quality=85)
        print(f"Saved: {output_path}")
    except ImportError:
        # Fall back to PNG
        output_path = output_path.with_suffix('.png')
        with open(output_path, 'wb') as f:
            f.write(image_data)
        print(f"Saved as PNG (PIL not available): {output_path}")

    return output_path

def main():
    for post in POSTS:
        try:
            path = generate_image(post['prompt'], post['filename'])
            print(f"✓ {post['slug']}: {path}")
        except Exception as e:
            print(f"✗ {post['slug']}: {e}")

if __name__ == "__main__":
    main()
