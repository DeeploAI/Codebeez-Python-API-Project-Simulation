# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data store
users = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/user', methods=['POST'])
def add_user():
    # Intentional issue: Lack of input validation
    user = request.json
    users.append(user)
    return jsonify(user), 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Intentional issue: Inefficient user lookup
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
