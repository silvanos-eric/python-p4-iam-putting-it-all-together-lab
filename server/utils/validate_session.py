from typing import Optional, Tuple, Union

from flask import session
from models import User, db
from werkzeug.exceptions import Unauthorized


def validate_session() -> Union[Tuple[dict, int], User]:
    user_id: Optional[int] = session.get('user_id')

    if not user_id:
        raise Unauthorized(
            'No active session found. Please log in to continue.')

    user: Optional[User] = db.session.get(User, user_id)
    if not user:
        raise Unauthorized(
            'Your account no longer exists. Please create a new account.')

    return user
