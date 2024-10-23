#!/usr/bin/env python3

from auth import SignUp
from config import api, app
from flask_restful import Resource


class CheckSession(Resource):
    pass


class Login(Resource):
    pass


class Logout(Resource):
    pass


class RecipeIndex(Resource):
    pass


@app.errorhandler(404)
def not_found_error(error):
    return {"error": "Resource not found"}, 404


api.add_resource(SignUp, '/signup')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
