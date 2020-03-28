import json
from flask import make_response, abort
from DAO import RecipeDAOimpl
from models.Recipe import Recipe


def read_all():
    recipes = []
    for recipe in RecipeDAOimpl.findAll():
        recipes.append(recipe.to_dict())
    json.dumps(recipes)
    return recipes


def read_by_source(id_src):
    recipes = []
    for recipe in RecipeDAOimpl.findByRecipe(id_src):
        recipes.append(recipe.to_dict())
    json.dumps(recipes)
    return recipes


def read_one(id_recipe):
    return RecipeDAOimpl.findOneById(id_recipe).to_dict()


def create(recipe):
    name = recipe.get("name", None)
    nbr_person = recipe.get("nbr_person", None)
    id_src = recipe.get("id_src", None)
    recipe = Recipe(None, name, nbr_person, id_src)
    id_recipe = RecipeDAOimpl.insert(recipe)
    json.dumps(id_recipe)
    return id_recipe


def update(id_recipe, recipe):
    name = recipe.get("name", None)
    nbr_person = recipe.get("nbr_person", None)
    id_src = recipe.get("id_src", None)
    recipe = Recipe(id_recipe, name, nbr_person, id_src)
    RecipeDAOimpl.update(recipe)


def delete(id_recipe):
    RecipeDAOimpl.deleteById(id_recipe)


def set_category(id_recipe, id_cat):
    RecipeDAOimpl.addCategory(id_recipe, id_cat)


def set_tool(id_recipe, id_tool):
    RecipeDAOimpl.addTool(id_recipe, id_tool)