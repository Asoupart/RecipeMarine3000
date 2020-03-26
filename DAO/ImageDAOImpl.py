import sqlite3

from models.Image import Image
from utils.ConnectionDB import ConnectionDB


def findAll():
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        images = []
        for row in cursor.execute("SELECT * FROM images"):
            images.append(Image(row[0], row[1], row[2]))
        return images
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneById(id_img):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM images WHERE id = ?', (id_img,))
        row = cursor.fetchone()
        image = Image(id_img, row[1], row[2])
        return image
    except sqlite3.Error as error:
        print(error.with_traceback())


def findByRecipe(id_recipe):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        images = []
        for row in cursor.execute("SELECT * FROM images WHERE id_recipe = ?", (id_recipe,)):
            images.append(Image(row[0], row[1], row[2]))
        return images
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneByName(name):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM images WHERE name = ?', (name,))
        row = cursor.fetchone()
        image = Image(row[0], name, row[2])
        return image
    except sqlite3.Error as error:
        print(error.with_traceback())


def insert(image):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO sections (name, id_recipe) VALUES (?,?)', (image.name, image.id_recipe))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def update(image):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE images SET name = ? AND id_recipe WHERE id = ?',
                       (image.name, image.id_recipe, image.id_img))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteById(id_img):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM images WHERE id = ?', (id_img,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())
