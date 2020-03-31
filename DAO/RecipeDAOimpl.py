import sqlite3
from utils.ConnectionDB import ConnectionDB
from models.Recipe import Recipe


def findAll():
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        recipes = []
        for row in cursor.execute("SELECT * FROM recipes"):
            recipes.append(Recipe(row[0], row[1], row[2], row[3]))
        return recipes
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneById(id_recipe):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM recipes WHERE id = ?', (id_recipe,))
        row = cursor.fetchone()
        recipe = Recipe(id_recipe, row[1], row[2], row[3])
        return recipe
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneByName(name):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM recipes WHERE name = ?', (name,))
        row = cursor.fetchone()
        recipe = Recipe(row[0], name, row[2], row[3])
        return recipe
    except sqlite3.Error as error:
        print(error.with_traceback())


def insert(recipe):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        if recipe.id_src is None:
            cursor.execute('INSERT INTO recipes (name, nbr_person) VALUES (?,?)', (recipe.name, recipe.nbr_person,))
        else:
            cursor.execute('INSERT INTO recipes (name, nbr_person, id_src) VALUES (?,?,?)', (recipe.name, recipe.nbr_person, recipe.id_src))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print(error.with_traceback())


def update(recipe):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE recipes SET name = ? AND nbr_person WHERE id = ?',
                       (recipe.name, recipe.nbr_person, recipe.id_recipe))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteById(id_recipe):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM recipes WHERE id = ?', (id_recipe,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def addCategory(id_recipe, id_cat):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO map_recipe_category (id_recipe, id_category) 
            VALUES (?,?)''', (id_recipe, id_cat))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def addTool(id_recipe, id_tool):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO map_recipe_tool (id_recipe, id_tool) 
            VALUES (?,?)''', (id_recipe, id_tool))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())