import json
from flask import make_response, abort
from DAO import IngredientDAOImpl
from models.Ingredient import Ingredient


def read_all():
    ingredients = []
    for ingredient in IngredientDAOImpl.findAll():
        ingredients.append(ingredient.to_dict())
    json.dumps(ingredients)
    return ingredients


def read_one(id_ing):
    return IngredientDAOImpl.findOneById(id_ing).to_dict()


def read_by_tag(tag):
    ingredients = []
    for ingredient in IngredientDAOImpl.findOneByName(tag):
        ingredients.append(ingredient.to_dict())
    json.dumps(ingredients)
    return ingredients


def create(ingredient):
    name = ingredient.get("name", None)
    ingredient = Ingredient(None, name)
    IngredientDAOImpl.insert(ingredient)


def update(id_ing, ingredient):
    name = ingredient.get("name", None)
    ingredient = Ingredient(id_ing, name)
    IngredientDAOImpl.update(ingredient)


def delete(id_ing):
    IngredientDAOImpl.deleteById(id_ing)