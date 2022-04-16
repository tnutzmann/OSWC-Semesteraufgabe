'''
todo: Contains the Todo class, this contains all the necessary attributes for a Todo card.
'''

class Todo:
    '''Class for TODO-Tickets '''

    def __init__(self, title, content, is_done = False, todo_id = -1):
        self.__title = title
        self.__content = content
        self.__is_done = is_done
        self.__todo_id = todo_id # todo_id is set by the Database

    def __str__(self):
        return str(self.__todo_id) + '\n' + \
               self.__title + '\n' + \
               self.__content + \
               '\nDone: ' + str(self.__is_done)

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
        '''
        try:
            bool(is_done)
        except NameError:
            raise TypeError('is_done must be an bool.') from NameError
        self.__is_done = str(is_done)

    @is_done.deleter
    def is_done(self):
        '''
        Deleter for is_done
        '''
        del self.is_done

    @property
    def todo_id(self):
        '''
        Getter for todo_id
        '''
        return self.__todo_id

    @todo_id.setter
    def todo_id(self, todo_id):
        '''
        Setter for todo_id
        '''
        try:
            int(todo_id)
        except NameError:
            raise TypeError('todo_id must be an Integer.') from NameError
        self.__title = int(todo_id)

    @todo_id.deleter
    def todo_id(self):
        '''
        Deleter for todo_id
        '''
        del self.__todo_id
