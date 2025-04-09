import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from model import MLModel
import sqlite3

api = Flask(__name__)
CORS(api)
api.config["CORS_HEADERS"] = "Content-Type"
auth_key = "uPTPeF9BDNiqAkNj"
limiter = Limiter(get_remote_address, app=api, default_limits=["200 per day", "50 per hour"])

MLmodel = MLModel()
MLmodel.load_model(
    "operations_models/5degpolymulti.sav",
    "operations_models/5degpolymulti.pkl",
    "operations_models/scaling_params.pkl"  
)

logging.basicConfig(filename="api_security_log.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

def check_api_key():
    if request.headers.get("Authorisation") != auth_key:
        return jsonify({"message": "Invalid or missing API key"}), 401

@api.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Prediction API!",
        "endpoints": {
            "/api/prediction": "POST - Make predictions",
        }
    }), 200

@api.route("/api/prediction", methods=["POST"])
@limiter.limit("1/second")
def prediction():
    auth_response = check_api_key()
    if auth_response:
        return auth_response
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "No input data provided"}), 400
        
        logging.debug(f"Received input data: {data}")
        
        prediction = MLmodel.predict(data)
        return jsonify({"prediction": prediction})
    except ValueError as ve:
        logging.error(f"Validation error: {ve}")
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        logging.error(f"Error in prediction: {e}")
        return jsonify({"message": "Error processing the request"}), 500

@api.route("/api/user_inputs", methods=["GET"])
def get_user_inputs():
    """Retrieve all saved user inputs."""
    conn = sqlite3.connect("user_inputs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_inputs")
    rows = cursor.fetchall()
    conn.close()

    columns = [
        "id", "Hours_Studied", "Attendance", "Parental_Involvement", "Access_to_Resources",
        "Extracurricular_Activities", "Sleep_Hours", "Previous_Scores", "Motivation_Level",
        "Internet_Access", "Tutoring_Sessions", "Family_Income", "Teacher_Quality",
        "School_Type", "Peer_Influence", "Physical_Activity", "Learning_Disabilities",
        "Parental_Education_Level", "Distance_from_Home", "Gender"
    ]
    user_inputs = [dict(zip(columns, row)) for row in rows]
    return jsonify(user_inputs)

if __name__ == "__main__":
    api.run(debug=True, host="0.0.0.0", port=3000)