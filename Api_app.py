from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Client(Resource):
    def get(self):
        data = pd.read_csv('Dataset\client.csv')
        dict_data = data.to_dict()
        # read csv file

        return {'data': dict_data}, 200
    
    def post(self):
        requirements = reqparse.RequestParser()
        requirements.add_argument('userId', required=True)
        requirements.add_argument('name', required=True)
        requirements.add_argument('city', required=True)
        args = requirements.parse_args()

        data = pd.read_csv('Dataset\client.csv')
        # read csv data

        if args['userId'] in list(data['userId']):
            return {'message': f"username '{args['userId']}' already exits."}, 409
        
        new_data_client = pd.DataFrame({'userId': [args['userId']], 'name': [args['name']], 'city': [args['city']], 'place': [[]] })
        data = data.append(new_data_client, ignore_index=True)
        dict_data = data.to_dict()
        data.to_csv('Dataset\client.csv',index=False)
        # add updated data to csv file

        return {'data': dict_data}, 200


api.add_resource(Client, '/client')


class Place(Resource):
    def get(self):
        data = pd.read_csv('Dataset\place.csv')
        dict_data = data.to_dict()
        # read csv file
        return {'data': dict_data}, 200 

    def post(self):
        requirements = reqparse.RequestParser()
        
        requirements.add_argument('placeId', required=True, type=int)
        requirements.add_argument('name', required=True)
        requirements.add_argument('rating', required=True)
        args = requirements.parse_args()

        data = pd.read_csv('Dataset\place.csv')

        if args['placeId'] in list(data['placeId']):
            return {'message': f"place '{args['placeId']}' already exits."}, 409
        
        new_data_client = pd.DataFrame({'placeId': [args['placeId']], 'name': [args['name']], 'rating': [args['rating']]})
        data = data.append(new_data_client, ignore_index=True)
        dict_data = data.to_dict()
        data.to_csv('Dataset\place.csv',index=False)
        # add updated data to csv file

        return {'data': dict_data}, 200


api.add_resource(Place, '/place')

@app.route("/")
def main():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)