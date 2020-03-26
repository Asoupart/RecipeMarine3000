import json
from flask import make_response, abort
from DAO import ToolDAOImpl
from models.Tool import Tool


def read_all():
    tools = []
    for tool in ToolDAOImpl.findAll():
        tools.append(tool.to_dict())
    json.dumps(tools)
    return tools


def read_one(id_tool):
    return ToolDAOImpl.findOneById(id_tool).to_dict()


def create(tool):
    name = tool.get("name", None)
    tool = Tool(None, name)
    ToolDAOImpl.insert(tool)


def update(id_tool, tool):
    name = tool.get("name", None)
    tool = Tool(id_tool, name)
    ToolDAOImpl.update(tool)


def delete(id_tool):
    ToolDAOImpl.deleteById(id_tool)
