import sqlite3


class ConnectionDB:
    class __ConnectionDB:

        def __init__(self):
            self.connection = sqlite3.connect("../recipebook.db", check_same_thread=False, timeout=10)

        def getConnection(self):
            return self.connection

        def closer(self):
            self.connection.close()

    instance = None

    def __new__(cls, *args, **kwargs):
        if not ConnectionDB.instance:
            ConnectionDB.instance = ConnectionDB.__ConnectionDB()
        return ConnectionDB.instance
