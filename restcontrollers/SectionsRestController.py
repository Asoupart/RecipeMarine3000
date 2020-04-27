import json
from flask import make_response, abort
from DAO import SectionDAOimpl
from DAO import InstructionDAOimpl
from models.Section import Section
from models.Instruction import Instruction


def read_all():
    sections = []
    for section in SectionDAOimpl.findAll():
        sections.append(section.to_dict())
    json.dumps(sections)
    return sections


def read_by_recipe(id_recipe):
    sections = []
    for section in SectionDAOimpl.findByRecipe(id_recipe):
        sections.append(section.to_dict())
    json.dumps(sections)
    return sections


def read_one(id_sec):
    return SectionDAOimpl.findOneById(id_sec).to_dict()


def create(section):
    name = section.get("name", None)
    id_recipe = section.get("id_recipe", None)
    section = Section(None, name, id_recipe)
    id_section = SectionDAOimpl.insert(section)
    json.dumps(id_section)
    return id_section


def add_section(id_recipe, section):
    section_to_insert = Section(None, section.get("name", None), id_recipe)
    id_section = SectionDAOimpl.insert(section_to_insert)
    for ingredient in section.get("ingredients", None):
        SectionDAOimpl.addIngredientToDB(id_section, ingredient.get("id_ingredient", None),
                                         ingredient.get("quantity", None), ingredient.get("unit", None))
    for instruction in section.get("instructions", None):
        InstructionDAOimpl.insert(Instruction(None, instruction.get("text", None), id_section))


def update(id_sec, section):
    name = section.get("name", None)
    id_recipe = section.get("id_recipe", None)
    section = Section(id_sec, name, id_recipe)
    SectionDAOimpl.update(section)


def delete(id_sec):
    InstructionDAOimpl.deleteBySection(id_sec)
    SectionDAOimpl.eraseAllMappingBySection(id_sec)
    SectionDAOimpl.deleteById(id_sec)


def set_ingredient(id_sec, id_ing, properties):
    quantity = properties.get("quantity", None)
    unit = properties.get("unit", None)
    SectionDAOimpl.addIngredientToDB(id_sec, id_ing, quantity, unit)


def delete_mapping(id_sec, id_ing):
    SectionDAOimpl.removeIngredientFromDB(id_sec, id_ing)

