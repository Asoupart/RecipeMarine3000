import json
from flask import make_response, abort
from DAO import InstructionDAOimpl
from models.Instruction import Instruction


def read_all():
    instructions = []
    for instruction in InstructionDAOimpl.findAll():
        instructions.append(instruction.to_dict())
    json.dumps(instructions)
    return instructions


def read_one(id_ins):
    return InstructionDAOimpl.findOneById(id_ins).to_dict()


def read_by_section(id_section):
    instructions = []
    for instruction in InstructionDAOimpl.findBySection(id_section):
        instructions.append(instruction.to_dict())
    json.dumps(instructions)
    return instructions


def create(instruction):
    text = instruction.get("text", None)
    id_section = instruction.get("id_section", None)
    instruction = Instruction(None, text, id_section)
    InstructionDAOimpl.insert(instruction)


def update(id_ins, instruction):
    text = instruction.get("text", None)
    id_section = instruction.get("id_section", None)
    instruction = Instruction(id_ins, text, id_section)
    InstructionDAOimpl.update(instruction)


def delete(id_ins):
    InstructionDAOimpl.deleteById(id_ins)
