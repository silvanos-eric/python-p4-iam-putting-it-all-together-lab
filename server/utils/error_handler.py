from models import db
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import UnsupportedMediaType


def error_handler(e):
    print(f"\033[91m{type(e)}\033[0m")
    print(f"\033[91m{e}\033[0m")

    db.session.rollback()

    if isinstance(e, UnsupportedMediaType):
        return {
            "error": "Unsupported Media Type",
            "message": "Set Content-Type to 'application/json' and try again."
        }, 415

    if isinstance(e, IntegrityError):
        return {
            "error":
            "Conflict",
            "message":
            "The username 'username' is already taken. Please choose a different username."
        }, 409

    return {'error': 'An uknown error occurred'}, 500
