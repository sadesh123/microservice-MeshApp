from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/data')
def get_data():
    try:
        response = requests.get("http://reviews:5003/reviews")
        reviews_data = response.json()
    except Exception as e:
        reviews_data = {"error": str(e)}

    # Add some processing info
    total_reviews = len(reviews_data.get("reviews", [])) if "reviews" in reviews_data else 0
    current_time = datetime.utcnow().isoformat() + "Z"

    return jsonify({
        "service": "backend",
        "timestamp": current_time,
        "total_reviews": total_reviews,
        "reviews_data": reviews_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
