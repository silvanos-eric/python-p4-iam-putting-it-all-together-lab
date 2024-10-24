from flask_restful import Resource
from models import Recipe
from utils import validate_session


class RecipeIndex(Resource):

    def get(self):
        validate_session()

        recipe_list = Recipe.query.all()
        recipe_dict_list = [recipe.to_dict() for recipe in recipe_list]

        return recipe_dict_list
