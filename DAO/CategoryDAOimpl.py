import sqlite3

from models.Category import Category
from utils.ConnectionDB import ConnectionDB


def findAll():
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        categories = []
        for row in cursor.execute("SELECT * FROM categories"):
            categories.append(Category(row[0], row[1]))
        return categories
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneById(id_cat):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM categories WHERE id = ?', (id_cat,))
        row = cursor.fetchone()
        category = Category(id_cat, row[1])
        return category
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneByName(name):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM categories WHERE name = ?', (name,))
        row = cursor.fetchone()
        category = Category(row[0], name)
        return category
    except sqlite3.Error as error:
        print(error.with_traceback())


def findByRecipe(id_recipe):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        categories = []
        for row in cursor.execute('''SELECT categories.id, categories.name FROM map_recipe_category 
                                    JOIN categories on categories.id=map_recipe_category.id_category 
                                    WHERE id_recipe = ?''', (id_recipe,)):
            categories.append(Category(row[0], row[1]))
        return categories
    except sqlite3.Error as error:
        print(error.with_traceback())


def insert(category):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO categories (\'name\') VALUES (?)', (category.name,))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print(error.with_traceback())


def update(category):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE categories SET name = ? WHERE id = ?', (category.name, category.id_cat))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteById(id_cat):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM categories WHERE id = ?', (id_cat,))
        cursor.execute('DELETE FROM map_recipe_category WHERE id_category = ?', (id_cat,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteByName(name):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM categories WHERE name = ?', (name,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def addCategory(recipe, category):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO map_recipe_category (id_recipe, id_category) VALUES (?,?)',
                       (recipe.id_recipe, category.id_cat,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())