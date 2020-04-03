import sqlite3

from models.Tool import Tool
from utils.ConnectionDB import ConnectionDB


def findAll():
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        tools = []
        for row in cursor.execute("SELECT * FROM tools"):
            tools.append(Tool(row[0], row[1]))
        return tools
    except sqlite3.Error as error:
        print(error.with_traceback())


def findByRecipe(id_recipe):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        tools = []
        for row in cursor.execute('''SELECT tools.id, tools.name FROM tools JOIN map_recipe_tool ON 
                            tools.id = map_recipe_tool.id_recipe WHERE map_recipe_tool.id_recipe = ?''', (id_recipe,)):
            tools.append(Tool(row[0], row[1]))
        return tools
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneById(id_tool):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM tools WHERE id = ?', (id_tool,))
        row = cursor.fetchone()
        tool = Tool(id_tool, row[1])
        return tool
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneByName(name):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM tools WHERE name = ?', (name,))
        row = cursor.fetchone()
        tool = Tool(row[0], name)
        return tool
    except sqlite3.Error as error:
        print(error.with_traceback())


def insert(tool):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO tools (name) VALUES (?)', (tool.name,))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print(error.with_traceback())


def update(tool):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE tools SET name = ? WHERE id = ?',
                       (tool.name, tool.id_tool,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteById(id_tool):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM tools WHERE id = ?', (id_tool,))
        cursor.execute('DELETE FROM map_recipe_tool WHERE id_tool = ?', (id_tool,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def addTool(recipe, tool):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO map_recipe_tool (id_recipe, id_tool) VALUES (?,?)',
                       (recipe.id_recipe, tool.id_tool,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())