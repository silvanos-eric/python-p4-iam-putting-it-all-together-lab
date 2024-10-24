from models import db
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import InternalServerError, UnprocessableEntity


def error_handler(e):
    print(f"\033[91m{type(e)}\033[0m")  # Print in red
    print(f"\033[91m{e}\033[0m")  # Print in red

    db.session.rollback()

    if isinstance(e, IntegrityError) and 'UNIQUE' in str(
            e) and 'users.username' in str(e):
        raise UnprocessableEntity(
            "The username is already taken. Please choose a different username."
        )

    if isinstance(
            e,
            IntegrityError) and 'CHECK' and 'length(instructions)' in str(e):
        raise UnprocessableEntity(
            "Instructions should be at least 50 characters long")

    raise InternalServerError()
