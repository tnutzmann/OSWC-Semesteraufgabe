'''
todo_database: Contains all the functions to use todo database and the Todo class, this contains all the necessary attributes for a Todo card.
'''
import sqlite3
import re

class Todo:
    '''Class for TODO-Tickets'''

    def __init__(self, title, content, is_done = 0, id = -1, color = "yellow"):
        self.__title = title
        self.__content = content
        self.__is_done = is_done
        self.__id = id # id is set by the Database
        self.__color = color

    def __str__(self):
        return str(self.__id) + '\n' + \
               self.__title + '\n' + \
               self.__content + '\n' + \
               self.__color + '\n' + \
               '\nDone: ' + str(self.__is_done)

    def is_done_to_str(self):
        switcher = {
            0: 'TO DO',
            1: 'DOING',
            2: 'DONE',
        }
        print(switcher.get(self.__is_done, 'Number must be between 0 and 2.'))

    @property
    def title(self):
        '''
        Getter for title
        '''
        return self.__title

    @title.setter
    def title(self, title):
        '''
        Setter for title
        '''
        try:
            str(title)
        except SyntaxError:
            raise TypeError('title must be an String.') from SyntaxError

        if len(title) < 50:
            self.__title = str(title)
        else:
            raise ValueError('title cannot be longer than 50 characters.')

    @title.deleter
    def title(self):
        '''
        Deleter for title
        '''
        del self.__title

    @property
    def content(self):
        '''
        Getter for content
        '''
        return self.__content

    @content.setter
    def content(self, content):
        '''
        Setter for content
        '''
        try:
            str(content)
        except SyntaxError:
            raise TypeError('content must be an String.') from SyntaxError
        self.__content = str(content)

    @content.deleter
    def content(self):
        '''
        Deleter for content
        '''
        del self.__content

    @property
    def is_done(self):
        '''
        Getter for is_done
        '''
        return self.__is_done

    @is_done.setter
    def is_done(self, is_done):
        '''
        Setter for is_done
        0 = TO DO
        1 = DOING
        2 = DONE
        '''
        try:
            int(is_done)
        except NameError:
            raise TypeError('is_done must be an integer.') from NameError
        if is_done > 2:
            raise ValueError('is_done cannot higer then 2.')
        elif is_done < 0:
            raise ValueError('is_done must be an positive number.')
        else:
            self.__is_done = int(is_done)

    @is_done.deleter
    def is_done(self):
        '''
        Deleter for is_done
        '''
        del self.is_done

    @property
    def id(self):
        '''
        Getter for id
        '''
        return self.__id

    @id.setter
    def id(self, id):
        '''
        Setter for id
        '''
        try:
            int(id)
        except NameError:
            raise TypeError('id must be an Integer.') from NameError
        self.__title = int(id)

    @id.deleter
    def id(self):
        '''
        Deleter for id
        '''
        del self.__id

    @property
    def color(self):
        '''
        Getter for color
        '''
        return self.__color

    @color.setter
    def color(self, color):
        '''
        Setter for color
        '''
        try:
            str(color)
        except SyntaxError:
            raise TypeError('color must be an String.') from SyntaxError

        switcher = {
            'yellow': 'yellow',
            'green': 'green',
            'orange': 'orange',
            'purple': 'purple',
            'rosa': 'rosa'
        }
        self.__title = switcher.get(color, 'yellow')

    @color.deleter
    def color(self):
        '''
        Deleter for color
        '''
        del self.__color

class Database:
    '''
    Class to use the database.
    '''

    def __init__(self, db_name):
        self.__db_name = db_name
        self.init_todo_table()

    def init_todo_table(self):
        '''
        Erstellt eine Tabelle wenn sie noch nicht existiert.
        Diese enthält hat die Spalten: titel, content und is_done
        '''
        con = sqlite3.connect(self.__db_name)
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS todos
         (title TEXT, content TEXT, is_done INTEGER, color TEXT)''')

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
            todo.append(Todo(i[1], i[2], i[3], int(i[0]), i[4]))
        return todo

    def add_todo(self, todo: Todo):
        '''
        Fügt ein Todo Item Objekt der Datenbank hinzu.
        :param: todo todo: Ein Objekt der Klasse todo.
        '''
        if (todo.id == -1):
            con = sqlite3.connect(self.__db_name)
            cur = con.cursor()

            cur.execute('INSERT INTO todos VALUES (?,?,?,?)',
             (todo.title, todo.content, todo.is_done, todo.color))

            con.commit()
            con.close()

    def remove_todo(self, id: int):
        '''
        Löscht Todo aus der Tabelle anhand der Id eines Todo Items.
        :param: int id: Die Id des Todo Item Objekts.
        '''
        if (id >= 0):
            con = sqlite3.connect(self.__db_name)
            cur = con.cursor()

            cur = con.cursor()
            cur.execute('DELETE FROM todos WHERE rowid=?', (str(id)))

            con.commit()
            con.close()

    def get_all_todos(self):
        '''
         Gibt alle todos aus der Datenbank zurück.
        :return: todo_list: Gibt eine Liste von Todo Objekten zurück.
        '''
        con = sqlite3.connect(self.__db_name)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM todos")
        query = cur.fetchall()

        con.commit()
        con.close()

        todo = self.query_to_todo(query)
        return todo

    def get_todo(self, id: int):
        '''
        Gibt ein Todo Item anhand seiner Id zurück.
        :param int id: Die Id des Todo Objekts.
        :return todo_list: Gibt ein Objekt der Klasse.
        '''
        con = sqlite3.connect(self.__db_name)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM todos WHERE rowid=?", (str(id)))
        query = cur.fetchall()

        con.commit()
        con.close()

        todo = self.query_to_todo(query)[0]
        return todo

    def update_todo(self, todo: Todo):
        '''
        Verändert in bestehendes todo item.
        :param int id: Die Id des Todo Objekts.
        :return todo_list: Gibt ein Objekt der Klasse.
        '''
        con = sqlite3.connect(self.__db_name)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("UPDATE todos SET title = ?, content = ?, is_done = ?, color = ? WHERE rowid=?", (todo.title, todo.content, todo.is_done, todo.color, str(todo.id)))
        query = cur.fetchall()

        con.commit()
        con.close()

    @property
    def db_name(self):
        '''
        Getter for db_name
        '''
        return self.__db_name

    @db_name.setter
    def db_name(self, db_name):
        '''
        Setter for db_name
        '''
        try:
            str(db_name)
        except SyntaxError:
            raise TypeError('db_name must be an String.') from SyntaxError

        if re.match('.*\.(?:db)', db_name, re.VERBOSE):
            self.__db_name = db_name
        else:
            raise ValueError('db_name must end with .db')

    @db_name.deleter
    def db_name(self):
        '''
        Deleter for name
        '''
        del self.__db_name