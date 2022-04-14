import sqlite3
from ToDoItem import ToDoItem


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
        cur.execute('''CREATE TABLE IF NOT EXISTS todos (title TEXT, context TEXT, isDone INTEGER)''')

        con.commit()
        con.close()

    def addTodoToDB(self, todo: ToDoItem):
        if (todo.todoID == -1):
            con = sqlite3.connect(self.dbName)
            cur = con.cursor()

            cur.execute('INSERT INTO todos VALUES (?,?,?)',(todo.title, todo.content, todo.isDone))
            
            con.commit()
            con.close()

    def removeTodoFromDB(self, todoID: int):
        if (todoID >= 0):
            con = sqlite3.connect(self.dbName)
            cur = con.cursor()

            cur = con.cursor()
            cur.execute('DELETE FROM todos WHERE rowid=?', (str(todoID)))

            con.commit()
            con.close()

    def getAllTodoFromDB(self):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM todos")
        query = cur.fetchall()

        con.commit()
        con.close()

        # TODO: in Objekte umwandeln
        return query

    def get_todo_from_db(self, todoID: int):
        con = sqlite3.connect(self.dbName)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM todos WHERE rowid=?", (todoID))
        query = cur.fetchall()

        con.commit()
        con.close()
        # TODO: in Objekt umwandeln
        return query