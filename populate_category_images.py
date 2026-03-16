
import os
from PIL import Image, ImageDraw, ImageFont
import random

# Mapping of Category -> Image Filename (relative to static/)
category_images = [
    ('Electronics', 'uploads/20251120000226electronics_cat.png'),
    ('Fashion', 'uploads/20251120000226fashion_cat.png'),
    ('Wearables', 'uploads/20251120000226wearables_cat.png'),
    ('Photography', 'uploads/20251120000226photography_cat.png'),
    ('Audio', 'uploads/20251120000226audio_cat.png'),
    ('Home & Living', 'uploads/20251120000226home__living_cat.png'),
    ('Sports & Outdoors', 'uploads/20251120000226sports__outdoors_cat.png'),
    ('Books & Stationery', 'uploads/20251120000226books__stationery_cat.png'),
    ('Beauty & Personal Care', 'uploads/20251120000226beauty__personal_care_cat.png'),
    ('Kitchen & Dining', 'uploads/20251120000226kitchen__dining_cat.png'),
    ('Gaming', 'uploads/20251120000755gaming_cat.png'),
    ('Home & Kitchen', 'uploads/20251120095918home__kitchen.jpg')
]

# Base static directory
static_dir = os.path.join(os.getcwd(), 'static')
uploads_dir = os.path.join(static_dir, 'uploads')

if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)
    print(f"Created directory: {uploads_dir}")

def generate_placeholder(text, filename):
    # Determine full path
    # filename includes 'uploads/', so strip that if we join with uploads_dir, or just join with static_dir
    # Based on the list, 'uploads/...' is the relative path.
    # The list items already have 'uploads/' prefix.
    # So full path is static_dir + filename
    
    full_path = os.path.join(static_dir, filename)
    
    # Ensure directory for this file exists (just in case)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    # Create image
    width, height = 800, 600
    # Random vibrant background color
    bg_color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
    img = Image.new('RGB', (width, height), color=bg_color)
    
    draw = ImageDraw.Draw(img)
    
    # Try to load a font, otherwise use default
    try:
        # On Windows, try Arial
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()
    
    # Text positioning
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    # Draw text with shadow for readability
    shadow_offset = 2
    draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=(0, 0, 0))
    draw.text((x, y), text, font=font, fill=(255, 255, 255))
    
    # Save
    # Check extension
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
        img.save(full_path, 'JPEG')
    else:
        img.save(full_path, 'PNG')
        
    print(f"Generated: {full_path}")

for cat_name, rel_path in category_images:
    generate_placeholder(cat_name, rel_path)

print("All category images generated successfully.")
