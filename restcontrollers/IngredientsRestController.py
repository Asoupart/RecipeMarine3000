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


def read_by_section(id_section):
    ingredients = []
    for row in IngredientDAOImpl.findBySection(id_section):
        ingredient = {"id_ingredient": row[0], "name": row[1], "quantity": row[2], "unit": row[3]}
        ingredients.append(ingredient)
    json.dumps(ingredients)
    return ingredients


def read_by_recipe(id_recipe):
    ingredients = []
    for row in IngredientDAOImpl.findByRecipe(id_recipe):
        ingredient = {"id_ingredient": int(row[0]), "name": row[1], "quantity": int(row[2]), "unit": row[3]}
        insert_ingredient = True
        if len(ingredients) > 0:
            for elem in ingredients:
                if int(elem['id_ingredient']) == row[0]:
                    insert_ingredient = False
                    elem['quantity'] = int(elem['quantity']) + int(row[2])
            if insert_ingredient:
                ingredients.append(ingredient)
        else:
            ingredients.append(ingredient)
    json.dumps(ingredients)
    return ingredients


def create(ingredient):
    name = ingredient.get("name", None)
    ingredient = Ingredient(None, name)
    id_ing = IngredientDAOImpl.insert(ingredient)
    json.dumps(id_ing)
    return id_ing


def update(id_ing, ingredient):
    name = ingredient.get("name", None)
    ingredient = Ingredient(id_ing, name)
    IngredientDAOImpl.update(ingredient)


def delete(id_ing):
    IngredientDAOImpl.deleteById(id_ing)
