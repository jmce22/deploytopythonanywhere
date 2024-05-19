# flask server that links to a DAO

from flask import Flask, request, jsonify, abort, render_template
from gymDAO import gymDAO

app = Flask(__name__)

@app.route('/')
def index():
        return 'Hello World'

# getall
# curl http://127.0.0.1:5000/gym

@app.route('/gym', methods=['GET'])
def getAll():
        return jsonify(gymDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/gym/1

@app.route('/gym/<int:id>', methods=['GET'])
def findById(id):
        return jsonify(gymDAO.findByID(id))


# create
# need to set Content-type to JSON and pass in paramter -H "Content-Type: application/json" - see https://reqbin.com/req/c-dwjszac0/curl-post-json-example
# curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Frank Furter\", \"sex\":\"male\", \"age\":\"22\", \"height\":\"190\", \"weight\":\"84\"}" http://127.0.0.1:5000/gym
@app.route('/gym', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        gym = {}

        if "name" not in jsonstring:
                abort(403)
        gym["name"] = jsonstring["name"]

        if "sex" not in jsonstring:
                abort(403)
        gym["sex"] = jsonstring["sex"]

        if "age" not in jsonstring:
                abort(403)
        gym["age"] = jsonstring["age"]

        if "height" not in jsonstring:
                abort(403)
        gym["height"] = jsonstring["height"]

        if "weight" not in jsonstring:
                abort(403)
        gym["weight"] = jsonstring["weight"]
        
        return jsonify(gymDAO.create(gym))

# update
# curl -X PUT -d "{\"id\":\"3\", \"name\":\"some guy\", \"sex\":\"male\", \"age\":\"43\", \"height\":\"180\", \"weight\":\"80\"}" http://127.0.0.1:5000/gym/3

@app.route('/gym/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        gym = {}

        if "name" in jsonstring:
                gym["name"] = jsonstring["name"]
        if "sex" in jsonstring:
                gym["sex"] = jsonstring["sex"]
        if "age" in jsonstring:
                gym["age"] = jsonstring["age"]
        if "height" in jsonstring:
                gym["height"] = jsonstring["height"]
        if "weight" in jsonstring:
                gym["weight"] = jsonstring["weight"]         
        return jsonify(gymDAO.update(id, gym))

# Delete
# curl -X DELETE  http://127.0.0.1:5000/gym/1

@app.route('/gym/<int:id>', methods=['DELETE'])
def delete(id):
        return jsonify(gymDAO.delete(id))


if __name__ == "__main__":
    app.run(debug = True)
