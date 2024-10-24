#!/usr/bin/env python3

from auth import CheckSession, Signup
from config import api, app
from flask_restful import Resource


class Login(Resource):
    pass


class Logout(Resource):
    pass


class RecipeIndex(Resource):
    pass


@app.errorhandler(404)
def not_found_error(error):
    return {"error": "Resource not found"}, 404


api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check_session')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
