import sqlite3
from Models.ToDoItem import ToDoItem

class DbHandler:
    dbName: str

    def __init__(self, dbName: str):
        self.dbName = dbName
        self.migrateDB()

    # erstellt Tabelle wenn sie nicht existiert
    def migrateDB(self):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()

        # Create Table
        cur.execute('''CREATE TABLE IF NOT EXISTS todos (title text, context text, isDone INTEGER)''')

        con.commit()
        con.close()

    def addTodoToDB(self, todo: ToDoItem):
        if (todo.todoID == -1):
            con = sqlite3.connect(self.dbName)
            cur = con.cursor()

            cur.execute(f'INSERT INTO todos VALUES ({todo.title},{todo.content},{todo.isDone})')
            
            con.commit()
            con.close()

    def removeTodoFromDB(self, todo: ToDoItem):
        if (todo.todoID >= 0):
            con = sqlite3.connect(self.dbName)
            cur = con.cursor()

            cur = con.cursor(f'DELETE FROM todos WHERE rowid={todo.todoID};')
            cur.execute()

            con.commit()
            con.close()

    def getAllTodoFromDB(self):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("SELECT * FROM todos")
        query = cur.fetchall()

        con.commit()
        con.close()

        return query
