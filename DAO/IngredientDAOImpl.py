import sqlite3
import json
from utils.ConnectionDB import ConnectionDB
from models.Ingredient import Ingredient


def findAll():
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        ingredients = []
        for row in cursor.execute("SELECT * FROM ingredients"):
            ingredients.append(Ingredient(row[0], row[1]))
        return ingredients
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneById(id_ing):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM ingredients WHERE id = ?', (id_ing,))
        row = cursor.fetchone()
        ingredient = Ingredient(id_ing, row[1])
        return ingredient
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneByName(name):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    name = f'{name}%'

    try:
        ingredients = []
        for row in cursor.execute('SELECT * FROM ingredients WHERE name LIKE ?', (name,)):
            ingredients.append(Ingredient(row[0], row[1]))
        return ingredients
    except sqlite3.Error as error:
        print(error.with_traceback())


def findBySection(id_section):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        ingredients = []
        for row in cursor.execute(
                '''SELECT map_section_ingredient.id_ingredient, ingredients.name, map_section_ingredient.quantity, map_section_ingredient.unit
                FROM map_section_ingredient
                INNER JOIN ingredients
                on map_section_ingredient.id_ingredient = ingredients.id
                WHERE map_section_ingredient.id_section = ?''', (id_section,)):
            ingredients.append(row)
        return ingredients
    except sqlite3.Error as error:
        print(error.with_traceback())


def insert(ingredient):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO ingredients (\'name\') VALUES (?)', (ingredient.name,))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print(error.with_traceback())


def update(ingredient):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE ingredients SET name = ? WHERE id = ?', (ingredient.name, ingredient.id_ing))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteById(id_ing):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM ingredients WHERE id = ?', (id_ing,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteByName(name):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM ingredients WHERE name = ?', (name,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())
