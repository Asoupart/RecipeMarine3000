import sqlite3

from models.Source import Source
from utils.ConnectionDB import ConnectionDB


def findAll():
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        sources = []
        for row in cursor.execute("SELECT * FROM sources"):
            sources.append(Source(row[0], row[1]))
        return sources
    except sqlite3.Error as error:
        print("FAIL")


def findOneById(id_src):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM sources WHERE id = ?', (id_src,))
        row = cursor.fetchone()
        source = Source(id_src, row[1])
        return source
    except sqlite3.Error as error:
        print("FAIL")


def findOneByName(name):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM sources WHERE name = ?', (name,))
        row = cursor.fetchone()
        source = Source(row[0], name)
        return source
    except sqlite3.Error as error:
        print("FAIL")


def insert(source):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO sources (name) VALUES (?)', (source.name,))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print(error.with_traceback())


def update(source):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE sources SET name = ? WHERE id = ?', (source.name, source.id_src))
        conn.commit()
    except sqlite3.Error as error:
        print("FAIL")


def deleteById(id_src):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM sources WHERE id = ?', (id_src,))
        conn.commit()
    except sqlite3.Error as error:
        print("FAIL")
