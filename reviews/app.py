from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/reviews')
def get_reviews():
    return jsonify({
        "service": "reviews",
        "reviews": [
            {"user": "Alice", "comment": "Great!"},
            {"user": "Bob", "comment": "Not bad!"}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
