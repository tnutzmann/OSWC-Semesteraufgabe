'''
Enthält alle Funktionen um todo Datenbank zu benutzen.
'''

from queue import Empty
import sqlite3
from todo import Todo


class Database:
    '''
    KLasse zum benutzen der Datenbank.
    '''
    db_name: str

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.init_todo_table()

    def init_todo_table(self):
        '''
        Erstellt eine Tabelle wenn sie noch nicht existiert.
        Diese enthält hat die Spalten: titel, content und is_done
        '''
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS todos
         (title TEXT, content TEXT, is_done INTEGER)''')

        con.commit()
        con.close()

    def query_to_todo(self, query: list):
        '''
        Wandelt eine Query list in ein Objekt.
        :param list query: Liste aus einer Datenbank abfrage.
        :return todo todo: Liste aus todo Objekten.
        '''
        todo = []
        for i in query:
            todo.append(Todo(i[1], i[2], i[3], int(i[0])))
        return todo

    def add_todo(self, todo: Todo):
        '''
        Fügt ein Todo Item Objekt der Datenbank hinzu.
        :param: todo todo: Ein Objekt der Klasse todo.
        '''
        if (todo.todo_id == -1):
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()

            cur.execute('INSERT INTO todos VALUES (?,?,?)',
             (todo.title, todo.content, todo.is_done))

            con.commit()
            con.close()

    def remove_todo(self, todo_id: int):
        '''
        Löscht Todo aus der Tabelle anhand der Id eines Todo Items.
        :param: int todo_id: Die Id des Todo Item Objekts.
        '''
        if (todo_id >= 0):
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()

            cur = con.cursor()
            cur.execute('DELETE FROM todos WHERE rowid=?', (str(todo_id)))

            con.commit()
            con.close()

    def get_all_todos(self):
        '''
         Gibt alle todos aus der Datenbank zurück.
        :return: todo_list: Gibt eine Liste von Todo Objekten zurück.
        '''
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM todos")
        query = cur.fetchall()

        con.commit()
        con.close()

        todo = self.query_to_todo(query)
        return todo

    def get_todo(self, todo_id: int):
        '''
        Gibt ein Todo Item anhand seiner Id zurück.
        :param int todo_id: Die Id des Todo Objekts.
        :return todo_list: Gibt ein Objekt der Klasse.
        '''
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM todos WHERE rowid=?", (str(todo_id)))
        query = cur.fetchall()

        con.commit()
        con.close()

        todo = self.query_to_todo(query)[0]
        return todo

    def update_todo(self, todo: Todo):
        '''
        Verändert in bestehendes todo item.
        :param int todo_id: Die Id des Todo Objekts.
        :return todo_list: Gibt ein Objekt der Klasse.
        '''
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("UPDATE todos SET title = ?, content = ?, is_done = ? WHERE rowid=?", (todo.title, todo.content, todo.is_done, str(todo.todo_id)))
        query = cur.fetchall()

        con.commit()
        con.close()
        