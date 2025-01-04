
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Gift Finder API is running!"

@app.route('/recommend_gifts', methods=['POST'])
def recommend_gifts():
    # Example response data
    data = [
        {"name": "Luxury Candle", "price": 40, "photo_url": "https://example.com/candle.jpg", "url": "https://example.com/candle"},
        {"name": "Personalized Mug", "price": 20, "photo_url": "https://example.com/mug.jpg", "url": "https://example.com/mug"}
    ]
    return jsonify({"recommendations": data})

if __name__ == '__main__':
    app.run()
