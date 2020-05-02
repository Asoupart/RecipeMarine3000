import json, os
from flask import make_response, abort
from DAO import RecipeDAOimpl, SectionDAOimpl, ImageDAOImpl, InstructionDAOimpl
from restcontrollers import SectionsRestController
from models.Recipe import Recipe
from models.Section import Section
from models.Instruction import Instruction
from models.Image import Image


def read_all():
    recipes = []
    for recipe in RecipeDAOimpl.findAll():
        recipes.append(recipe.to_dict())
    json.dumps(recipes)
    return recipes


def read_by_source(id_src):
    recipes = []
    for recipe in RecipeDAOimpl.findBySource(id_src):
        recipes.append(recipe.to_dict())
    json.dumps(recipes)
    return recipes


def read_by_category(id_category):
    recipes = []
    for recipe in RecipeDAOimpl.findByCategory(id_category):
        recipes.append(recipe.to_dict())
    json.dumps(recipes)
    return recipes


def read_by_tool(id_tool):
    recipes = []
    for recipe in RecipeDAOimpl.findByTool(id_tool):
        recipes.append(recipe.to_dict())
    json.dumps(recipes)
    return recipes


def read_one(id_recipe):
    return RecipeDAOimpl.findOneById(id_recipe).to_dict()


def read_by_ingredient(id_ingredient):
    recipes = []
    for recipe in RecipeDAOimpl.findByIngredient(id_ingredient):
        recipes.append(recipe.to_dict())
    json.dumps(recipes)
    return recipes


def create(recipe):
    name = recipe.get("name", None)
    nbr_person = recipe.get("nbr_person", None)
    id_src = recipe.get("id_src", None)
    recipe = Recipe(None, name, nbr_person, id_src)
    id_recipe = RecipeDAOimpl.insert(recipe)
    json.dumps(id_recipe)
    return id_recipe


def create_recipe(recipe):
    name_recipe = recipe.get("name_recipe", None)
    nbr_person = recipe.get("nbr_person", None)
    id_src = recipe.get("id_src", None)
    if id_src == 0:
        id_src = None

    recipe_to_insert = Recipe(None, name_recipe, nbr_person, id_src)
    id_recipe = RecipeDAOimpl.insert(recipe_to_insert)

    for img in recipe.get("images", None):
        ImageDAOImpl.insert(Image(None, img.get("name", None), id_recipe))
    for id_cat in recipe.get("id_cats", None):
        RecipeDAOimpl.addCategory(id_recipe, id_cat)
    for id_tool in recipe.get("id_tools", None):
        RecipeDAOimpl.addTool(id_recipe, id_tool)
    for section in recipe.get("sections", None):
        SectionsRestController.add_section(id_recipe, section)


def update(id_recipe, recipe):
    name = recipe.get("name", None)
    nbr_person = recipe.get("nbr_person", None)
    id_src = recipe.get("id_src", None)
    recipe = Recipe(id_recipe, name, nbr_person, id_src)
    RecipeDAOimpl.update(recipe)


def delete(id_recipe):
    RecipeDAOimpl.deleteById(id_recipe)


def delete_full(id_recipe):
    for section in SectionDAOimpl.findByRecipe(id_recipe):
        InstructionDAOimpl.deleteBySection(section.id_sec)
        SectionDAOimpl.eraseAllMappingBySection(section.id_sec)
        SectionDAOimpl.deleteById(section.id_sec)
    for image in ImageDAOImpl.findByRecipe(id_recipe):
        ImageDAOImpl.deleteById(image.id_img)
    RecipeDAOimpl.eraseCategoryMapping(id_recipe)
    RecipeDAOimpl.eraseToolMapping(id_recipe)
    RecipeDAOimpl.deleteById(id_recipe)


def set_category(id_recipe, id_cat):
    RecipeDAOimpl.addCategory(id_recipe, id_cat)


def delete_category_mapping(id_recipe):
    RecipeDAOimpl.eraseCategoryMapping(id_recipe)


def set_tool(id_recipe, id_tool):
    RecipeDAOimpl.addTool(id_recipe, id_tool)


def delete_tool_mapping(id_recipe):
    RecipeDAOimpl.eraseToolMapping(id_recipe)