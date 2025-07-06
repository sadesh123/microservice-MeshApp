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
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Frontend v2</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" 
            rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container py-5">
            <div class="text-center mb-5">
                <h1 class="display-4 text-primary">🎉 Frontend Service v2 🎉</h1>
                <p class="lead">Powered by Python + Bootstrap</p>
            </div>

            {% if data.get("error") %}
                <div class="alert alert-danger" role="alert">
                    Error fetching data from backend: {{ data["error"] }}
                </div>
            {% else %}
                <div class="card mb-4 shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">📦 Backend Data</h5>
                        <p><strong>Service:</strong> {{ data.get("service") }}</p>
                        <p><strong>Timestamp:</strong> {{ data.get("timestamp") }}</p>
                        <p><strong>Total Reviews:</strong> {{ data.get("total_reviews") }}</p>
                    </div>
                </div>

                <div class="card shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">💬 Reviews from Reviews Service</h5>
                        {% if data.get("reviews_data", {}).get("reviews") %}
                            <ul class="list-group list-group-flush">
                            {% for review in data["reviews_data"]["reviews"] %}
                                <li class="list-group-item">
                                    <strong>{{ review.user }}:</strong> {{ review.comment }}
                                </li>
                            {% endfor %}
                            </ul>
                        {% else %}
                            <p>No reviews available.</p>
                        {% endif %}
                    </div>
                </div>
            {% endif %}
        </div>
    </body>
    </html>
    """
    return render_template_string(html, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
