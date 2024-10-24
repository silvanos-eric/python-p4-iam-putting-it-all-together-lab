from flask import request
from flask_restful import Resource
from models import Recipe, db
from utils import error_handler, validate_session
from werkzeug.exceptions import UnprocessableEntity


class RecipeIndex(Resource):

    def get(self):
        validate_session()

        recipe_list = Recipe.query.all()
        recipe_dict_list = [recipe.to_dict() for recipe in recipe_list]

        return recipe_dict_list

    def post(self):
        errors = []
        user = validate_session()

        # Retreive data
        recipe_data = request.json
        title = recipe_data.get('title')
        instructions = recipe_data.get('instructions')
        minutes_to_complete = recipe_data.get('minutes_to_complete')
        user_id = user.id

        if not title:
            errors.append("Title is required")
        if not instructions:
            errors.append("Instrctions is required")
        if not minutes_to_complete:
            errors.append("Minutes to complete, is required")

        if errors:
            raise UnprocessableEntity(errors)

        try:
            new_recipe = Recipe(title=title,
                                instructions=instructions,
                                minutes_to_complete=minutes_to_complete,
                                user_id=user_id)
            db.session.add(new_recipe)
            db.session.commit()

            return new_recipe.to_dict(), 201
        except Exception as e:
            return error_handler(e)
