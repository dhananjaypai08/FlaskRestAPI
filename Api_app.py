from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Client(Resource):
    def get(self):
        data = pd.read_csv('client.csv')
        dict_data = data.to_dict()
        
        return {'data': dict_data}, 200
    
    def post(self):
        requirements = reqparse.RequestParser()
        requirements.add_argument('userId', required=True)
        requirements.add_argument('name', required=True)
        requirements.add_argument('city', required=True)
        args = requirements.parse_args()

        data = pd.read_csv('client.csv')

        if args['userId'] in list(data['userId']):
            return {'message': f"username '{args['userId']}' already exits."}, 409
        else:
            new_data_client = pd.DataFrame({'userId': args['userId'], 'name': args['name'], 'city': args['city'], 'place': [[]] })
        data = data.append(new_data_client, ignore_index=True)
        dict_data = data.to_dict()
        data.to_csv('client.csv',index=False)
        return {'data': dict_data}, 200

api.add_resource(Client, '/client')


class Place(Resource):
    def get(self):
        data = pd.read_csv('place.csv')
        dict_data = data.to_dict()

        return {'data': dict_data}, 200 

    def post(self):
        pass

api.add_resource(Place, '/place')

if __name__=='__main__':
    app.run(debug=True)