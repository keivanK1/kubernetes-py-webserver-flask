# Product service
# We want to make it restful api, so we will import flask and flask_restful
# flask is a web framework for python

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
  def get(self):
    return{
      'cars':[
        'BMW',
        'Benz',
        'Audi'
      ]
    }

api.add_resource(Product, '/')

if __name__=='__main__':
  app.run(host="0.0.0.0", port=int("5000"), debug=True)

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# if __name__ == '__main__':
#     app.run()