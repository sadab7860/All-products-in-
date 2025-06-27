from flask import Flask, request, jsonify
from PIL import Image
import os
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "FindThatLook App Backend Running!"

@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = file.filename
    filepath = os.path.join("uploads", filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(filepath)

    matched_links = [
        "https://www.amazon.in/dp/B0CXYZT123",
        "https://www.flipkart.com/item/p/itmabcd123",
        "https://www.meesho.com/product/p/xyz987"
    ]

    if random.choice([True, False]):
        return jsonify({"link": random.choice(matched_links)})
    else:
        return jsonify({"message": "Sorry, product out of stock"}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
