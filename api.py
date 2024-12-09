from flask import Flask, request, jsonify
from model import ImageCaptionGenerator

app = Flask(__name__)
caption_generator = ImageCaptionGenerator()

@app.route('/caption', methods=['POST'])
def generate_caption():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image = request.files['image']
    image_path = f"./uploaded_image.jpg"
    image.save(image_path)
    caption = caption_generator.generate_caption(image_path)
    return jsonify({"caption": caption})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
