'''
todo_database: Contains all the functions to
use todo database and the Todo class, this
contains all the necessary attributes for
a Todo card.
'''
import sqlite3
import re


class Todo:
    '''
    Class for TODO-Tickets
    '''

    #  pylint: disable=too-many-arguments
    def __init__(self, title, content, is_done=0, card_id=-1, color="yellow"):
        self.__title = title
        self.__content = content
        self.__is_done = is_done
        self.__card_id = card_id  # card_id is set by the Database
        self.__color = color

    def __str__(self):
        return str(self.__card_id) + '\n' + \
               self.__title + '\n' + \
               self.__content + '\n' + \
               self.__color + '\n' + \
               'Done: ' + str(self.__is_done)

    def is_done_to_str(self):
        '''
        :return the String of is_done
        '''
        switcher = {
            0: 'TO DO',
            1: 'DOING',
            2: 'DONE',
        }
        return switcher.get(self.__is_done, 'Number must be between 0 and 2.')

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

        if 0 <= is_done <= 2:
            self.__is_done = int(is_done)
        else:
            raise ValueError('is_done must be between 0 and 2 ')

    @is_done.deleter
    def is_done(self):
        '''
        Deleter for is_done
        '''
        del self.is_done

    @property
    def card_id(self):
        '''
        Getter for card_id
        '''
        return self.__card_id

    @card_id.setter
    def card_id(self, card_id):
        '''
        Setter for card_id
        '''
        try:
            int(card_id)
        except NameError:
            raise TypeError('card_id must be an Integer.') from NameError
        self.__title = int(card_id)

    @card_id.deleter
    def card_id(self):
        '''
        Deleter for card_id
        '''
        del self.__card_id

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
        Creates a table if it does not already exist.
        This contains has the columns: title, content and is_done
        '''
        con = sqlite3.connect(self.__db_name)
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS todos
         (title TEXT, content TEXT, is_done INTEGER, color TEXT)''')

        con.commit()
        con.close()

    @classmethod
    def query_to_todo(cls, query: list):
        '''
        Converts a query list into an object.
        :param list query: Query list from a database.
        :return todo: List from todo objects.
        '''
        todo = []
        for i in query:
            todo.append(Todo(i[1], i[2], i[3], int(i[0]), i[4]))
        return todo

    def add_todo(self, todo: Todo):
        '''
        Adds a Todo Item object to the database.
        :param todo: An object of the class todo.
        '''
        if todo.card_id == -1:
            con = sqlite3.connect(self.__db_name)
            cur = con.cursor()

            cur.execute('INSERT INTO todos VALUES (?,?,?,?)',
                        (todo.title, todo.content, todo.is_done, todo.color))

            con.commit()
            con.close()

    def remove_todo(self, card_id: int):
        '''
        Deletes todo from the table based on the id of a todo item.
        :param int id: The id of the todo item object.
        '''
        if card_id >= 0:
            con = sqlite3.connect(self.__db_name)
            cur = con.cursor()

            cur = con.cursor()
            cur.execute('DELETE FROM todos WHERE rowid=?', (str(card_id)))

            con.commit()
            con.close()
        else:
            raise ValueError('Id is to low.')

    def get_all_todos(self):
        '''
         Returns all todos from the database.
        :return: todo_list: Returns a list of todo objects.
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

    def get_todo(self, card_id: int):
        '''
        Returns a todo item by its id.
        :param int id: The id of the todo object.
        :return todo_list: Returns an object of the class.
        '''
        con = sqlite3.connect(self.__db_name)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM todos WHERE rowid=?", (str(card_id)))
        query = cur.fetchall()

        con.commit()
        con.close()

        todo = self.query_to_todo(query)[0]
        return todo

    def update_todo(self, todo: Todo):
        '''
        Changed to existing todo item.
        :param int id: The id of the todo object.
        :return todo_list: Returns an object of the class.
        '''
        con = sqlite3.connect(self.__db_name)
        cur = con.cursor()

        cur = con.cursor()
        cur.execute("UPDATE todos \
                    SET title = ?, \
                    content = ?, \
                    is_done = ?, \
                    color = ? \
                    WHERE rowid=?",
                    (todo.title,
                     todo.content,
                     str(todo.is_done),
                     todo.color,
                     str(todo.card_id)))

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

        if re.match(r'.*\.(?:db)', db_name, re.VERBOSE):
            self.__db_name = db_name
        else:
            raise ValueError('db_name must end with .db')

    @db_name.deleter
    def db_name(self):
        '''
        Deleter for name
        '''
        del self.__db_name
