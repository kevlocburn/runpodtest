from flask import Flask, request, jsonify
from blip_model import ImageCaptionGenerator
from stable_diffusion import TextToImageGenerator

app = Flask(__name__)
caption_generator = ImageCaptionGenerator()
text_to_image_generator = TextToImageGenerator()

@app.route('/caption', methods=['POST'])
def generate_caption():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image = request.files['image']
    image_path = f"./uploaded_image.jpg"
    image.save(image_path)
    caption = caption_generator.generate_caption(image_path)
    return jsonify({"caption": caption})

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "No prompt provided"}), 400
    prompt = data["prompt"]
    image_path = text_to_image_generator.generate_image(prompt)
    return jsonify({"image_path": image_path})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
