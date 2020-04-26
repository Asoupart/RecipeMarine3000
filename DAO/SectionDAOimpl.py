import sqlite3

from models.Section import Section
from utils.ConnectionDB import ConnectionDB


def findAll():
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        sections = []
        for row in cursor.execute("SELECT * FROM sections"):
            sections.append(Section(row[0], row[1], row[2]))
        return sections
    except sqlite3.Error as error:
        print(error.with_traceback())


def findByRecipe(id_recipe):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        sections = []
        for row in cursor.execute("SELECT * FROM sections WHERE id_recipe = ?", (id_recipe,)):
            sections.append(Section(row[0], row[1], row[2]))
        return sections
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneById(id_sec):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM sections WHERE id = ?', (id_sec,))
        row = cursor.fetchone()
        section = Section(id_sec, row[1], row[2])
        return section
    except sqlite3.Error as error:
        print(error.with_traceback())


def insert(section):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO sections (name, id_recipe) VALUES (?, ?)', (section.name, section.id_recipe,))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print(error.with_traceback())


def update(section):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE sections SET name = ? AND id_recipe = ? WHERE id = ?', (section.name, section.id_recipe, section.id_sec))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteById(id_sec):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM sections WHERE id = ?', (id_sec,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def addIngredientToDB(id_sec, id_ing, quantity, unit):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO map_section_ingredient (id_section, id_ingredient, quantity, unit) 
            VALUES (?,?,?,?)''', (id_sec, id_ing, quantity, unit))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def eraseAllMappingBySection(id_section):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM map_section_ingredient WHERE id_section = ?', (id_section,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def removeIngredientFromDB(id_sec, id_ing):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM map_section_ingredient WHERE id_section = ? AND id_ingredient = ?', (id_sec, id_ing,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())