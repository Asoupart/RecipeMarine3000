import json
from flask import make_response, abort
from DAO import CategoryDAOimpl
from models.Category import Category


def read_all():
    categories = []
    for category in CategoryDAOimpl.findAll():
        categories.append(category.to_dict())
    json.dumps(categories)
    return categories


def read_by_recipe(id_recipe):
    categories = []
    for category in CategoryDAOimpl.findByRecipe(id_recipe):
        categories.append(category.to_dict())
    json.dumps(categories)
    return categories


def read_one(id_ing):
    return CategoryDAOimpl.findOneById(id_ing).to_dict()


def create(category):
    name = category.get("name", None)
    category = Category(None, name)
    id_cat = CategoryDAOimpl.insert(category)
    json.dumps(id_cat)
    return id_cat


def update(id_cat, category):
    name = category.get("name", None)
    category = Category(id_cat, name)
    CategoryDAOimpl.update(category)


def delete(id_cat):
    CategoryDAOimpl.deleteById(id_cat)
