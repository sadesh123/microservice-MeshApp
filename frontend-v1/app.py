from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        response = requests.get("http://backend:5002/data")
        data = response.json()
    except Exception as e:
        data = {"error": str(e)}

    html = """
    <h1>Frontend Service</h1>

    <p><b>Data Source:</b> {{ data.get('service') }}</p>
    <p><b>Backend Timestamp:</b> {{ data.get('timestamp') }}</p>
    <p><b>Total Reviews:</b> {{ data.get('total_reviews') }}</p>

    <h2>Reviews (From Reviews Service):</h2>
    <ul>
    {% for review in data.get('reviews_data', {}).get('reviews', []) %}
        <li><b>{{ review.user }}</b>: {{ review.comment }}</li>
    {% else %}
        <li>No reviews available</li>
    {% endfor %}
    </ul>
    """

    return render_template_string(html, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
