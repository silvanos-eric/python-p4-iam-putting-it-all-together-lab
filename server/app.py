#!/usr/bin/env python3

from auth import CheckSession, Login, Logout, Signup
from config import api, app
from recipes import RecipeIndex


@app.errorhandler(404)
def not_found_error(error):
    return {"error": "Resource not found"}, 404


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Logout, '/logout')
api.add_resource(RecipeIndex, '/recipes')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
