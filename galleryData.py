from pathlib import Path
import json

# Define gallery structure
base_dir = Path("gallery")
categories = ["people", "places", "things"]
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

image_library = {}

for category in categories:
    folder = base_dir / category
    if not folder.exists():
        continue
    entries = []
    for file in folder.iterdir():
        if file.suffix.lower() in image_extensions:
            entries.append({
                "src": f"gallery/{category}/{file.name}",
                "label": file.stem.replace("_", " ").replace("-", " ")
            })
    image_library[category] = entries

# Output the result as a JS variable assignment
gallery_data_js = f"window.imageLibrary = {json.dumps(image_library, indent=2)};"

output_path = Path("galleryData.js")
output_path.write_text(gallery_data_js)

output_path.name
