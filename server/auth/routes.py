from config import db
from flask import request, session
from flask_restful import Resource
from models import User
from utils import error_handler


class Signup(Resource):

    def post(self):
        error_messages = []

        # Extract data
        user_data = request.json
        username = user_data.get('username')
        password = user_data.get('password')
        # confirm_password = user_data.get('confirm_password')
        image_url = user_data.get('image_url')
        bio = user_data.get('bio')

        # Validate fields
        if not username:
            error_messages.append("Username is required")
        if not password:
            error_messages.append("Password is required")
        # if not confirm_password:
        #     error_messages.append("Confirm Password is required")
        # if password != confirm_password:
        #     error_messages.append(
        #         "Password and Confirm Password do not match")

        if error_messages:
            return {'errors': error_messages}, 422

        try:

            # Save user to database
            new_user = User(username=username, image_url=image_url, bio=bio)
            new_user.password_hash = password

            db.session.add(new_user)
            db.session.commit()

            # Create a session for the user
            session['user_id'] = new_user.id

            return new_user.to_dict(), 201
        except Exception as error:
            return error_handler(error)


class CheckSession(Resource):

    def get(self):
        user_id = session.get('user_id')

        if not user_id:
            return {
                "error": "Unauthorized",
                "message": "No active session found. Please log in to continue"
            }, 401

        user = db.session.get(User, user_id)
        if not user:
            return {
                "error": "Unauthorized",
                "message":
                "Your account no longer exists. Create a new account"
            }
        return user.to_dict()
