import sqlite3
from utils.ConnectionDB import ConnectionDB
from models.Instruction import Instruction


def findAll():
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        instructions = []
        for row in cursor.execute("SELECT * FROM instructions"):
            instructions.append(Instruction(row[0], row[1], row[2]))
        return instructions
    except sqlite3.Error as error:
        print(error.with_traceback())


def findBySection(id_section):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        instructions = []
        for row in cursor.execute("SELECT * FROM instructions WHERE id_section = ?", (id_section,)):
            instructions.append(Instruction(row[0], row[1], row[2]))
        return instructions
    except sqlite3.Error as error:
        print(error.with_traceback())


def findOneById(id_ins):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM instructions WHERE id = ?', (id_ins,))
        row = cursor.fetchone()
        instruction = Instruction(id_ins, row[1], row[2])
        return instruction
    except sqlite3.Error as error:
        print(error.with_traceback())


def insert(instruction):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO instructions (text_ins, id_section) VALUES (?, ?)',
                       (instruction.text_ins, instruction.id_section))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print(error.with_traceback())


def update(instruction):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE instructions SET text_ins = ? WHERE id = ?',
                       (instruction.text_ins, instruction.id_ins))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteById(id_ins):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM instructions WHERE id = ?', (id_ins,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())


def deleteBySection(id_section):
    conn = ConnectionDB().getConnection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM instructions WHERE id_section = ?', (id_section,))
        conn.commit()
    except sqlite3.Error as error:
        print(error.with_traceback())