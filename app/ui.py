from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger configuration
SWAGGER_URL = "/api/docs"  # URL for accessing Swagger UI
API_URL = "/static/swagger.json"  # Path to Swagger JSON

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "LLM Alignment Assistant API Documentation"},
)

# Register Swagger Blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(debug=True)
