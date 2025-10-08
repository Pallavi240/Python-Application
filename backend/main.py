from flask import Flask, request, jsonify
from flask_cors import CORS
import pyrebase


app = Flask(__name__)
CORS(app)

firebaseConfig = {
    'apiKey': "AIzaSyB2Wr5cz3wM6s57Huqyx7ZfSqAVXOOmp80",
    'authDomain': "authdemo-d185f.firebaseapp.com",
    'databaseURL': "https://trialauth-7eea1-default-rtdb.firebaseio.com",
    'projectId': "authdemo-d185f",
    'storageBucket': "authdemo-d185f.firebasestorage.app",
    'messagingSenderId': "1050926821771",
    'appId': "1:1050926821771:web:cfe0c772c8d31116a5bf8e",
    'measurementId': "G-PQEHB2LBVT"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


@app.route('/')
def home():
    return jsonify({"message": "Backend is running successfully"})


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data['email']
    password = data['password']
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return jsonify({"message": "User created successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        token = user['idToken']
        return jsonify({"message": "Login successful", "token": token}), 200
    except Exception as e:
        return jsonify({"error": "Invalid email or password"}), 401


if __name__ == '__main__':
    app.run(debug=True)
