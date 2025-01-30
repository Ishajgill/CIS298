from flask import Blueprint, jsonify

# Create a blueprint for APIs
api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "message": "Hello from the Flask API!",
        "data": ["Item 1", "Item 2", "Item 3"]
    })
