import os
from flask import Flask, request, jsonify
from converter import NumberConverter
from functools import wraps

app = Flask(__name__)

# In production, these would be in environment variables
API_KEY = os.environ.get("APP_API_KEY")

def require_api_key():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            key = request.headers.get('X-API-Key')
            if not key or key != API_KEY:
                return jsonify({"error": "Unauthorized"}), 401
            return f(*args, **kwargs)
        return decorated_function
    return decorator

converter = NumberConverter()

@app.route('/')
def health_check():
    return "OK", 200

@app.route('/convert', methods=['POST'])
@require_api_key()
def convert_number():
    data = request.json

    if not data or 'number' not in data:
        return jsonify({"error": "Missing 'number' in request body"}), 400

    try:
        number = int(data['number'])

        result = converter.convert(number)
        return jsonify({"original": number, "converted": result})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
