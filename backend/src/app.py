from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from config import config

app = Flask(__name__)
app.config["MONGO_URI"] = config["MONGO_URI"]

CORS(app)
mongo = PyMongo(app)
db = mongo.db.users

@app.route("/users", methods=["GET"])
def get_users():
    users = []
    for user in db.find():
        users.append({
            "_id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "password": user["password"],
        })
    return jsonify(users)

@app.route("/user/<id>", methods=["GET"])
def get_user(id):
    user = db.find_one({"_id": ObjectId(id)})
    if user:
        user["_id"] = str(user["_id"])
        return jsonify(user=user)
    return jsonify(error="User not found"), 404

@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    user = db.insert_one({
        "name": data["name"],
        "email": data["email"],
        "password": data["password"],
    })
    return jsonify(id=str(user.inserted_id), message="User created successfully."), 201

@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id: str):
    result = db.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return jsonify(message="User deleted", id=id)
    return jsonify(error="User not found"), 404

@app.route("/user/<id>", methods=["PUT"])
def update_user(id: str):
    data = request.json
    result = db.update_one(
        {'_id': ObjectId(id)},
        {"$set": {
            'name': data["name"],
            'email': data["email"],
            'password': data["password"]
        }}
    )
    if result.modified_count:
        return jsonify(message="User updated", id=id)
    return jsonify(message="No changes made", id=id)

# ✅ START THE FLASK APP
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

