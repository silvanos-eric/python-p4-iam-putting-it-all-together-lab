from config import db
from flask import request, session
from flask_restful import Resource
from models import User
from utils import error_handler


class Signup(Resource):

    def post(self):
        errors = []

        # Extract data
        user_data = request.json
        username = user_data.get('username')
        password = user_data.get('password')
        # confirm_password = user_data.get('confirm_password')
        image_url = user_data.get('image_url')
        bio = user_data.get('bio')

        # Validate fields
        if not username:
            errors.append("Username is required")
        if not password:
            errors.append("Password is required")
        # if not confirm_password:
        #     error_messages.append("Confirm Password is required")
        # if password != confirm_password:
        #     error_messages.append(
        #         "Password and Confirm Password do not match")

        if errors:
            return {'errors': errors}, 422

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

        if user_id is None:
            return {
                'error': 'Unauthorized',
                'message': 'No active session found. Please log in to continue'
            }, 401

        user = User.query.get(user_id)
        if user is None:
            return {
                'error': 'Unauthorized',
                'message':
                'Your account no longer exists. Create a new account'
            }, 401

        return user.to_dict()


class Login(Resource):

    def post(self):
        errors = []

        user_data = request.json
        username = user_data.get("username")
        password = user_data.get("password")

        if not username:
            errors.append("Username is required")
        if not password:
            errors.append("Password is required")

        if errors:
            return {"errors": errors}, 422

        user = User.query.filter_by(username=username).first()
        if not user or not user.authenticate(password):
            return {"error": "Invalid username/password"}, 401

        return user.to_dict()
