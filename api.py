from flask import Flask, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson.json_util import dumps
import json
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/election"

CORS(app)

api = Api(app)
mongo = PyMongo(app)

# List of candidates
class Candidates(Resource):
    def get(self):
        return json.loads(
                dumps(mongo.db.people_key
                    .find({},{"_id":0,"person_id":1,"name":1})
                    .distinct("name")
                )
            )

# individual candidate
# class Candidate(Resource):
#     def get(self,person_id):
#         return json.loads(
#             dumps(mongo.db.people_key
#                 .find({"person_id":person_id},{'_id':0,'text':1,'value':1})
#             )
#         )

api.add_resource(Candidates,'/people')



