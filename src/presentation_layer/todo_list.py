'''
Contains all the functions that are necessary to create the website.
'''

import cgi
import logging
from data_layer.todo_database import Todo
from data_layer.todo_database import Database

logging.basicConfig( level=logging.DEBUG, filename='todo_cgi.log')

def todo_to_html(todo: Todo):
    '''
   Create the Todo Card Div.
   :param: Todo Item
   :return: f-string todo as html div tag
    '''
    return f'''
    <div class="todo {todo.color} state_{todo.is_done}" id="todo_{todo.card_id}">
        <h2 class="todo_header">#{todo.card_id} {todo.title}</h2>
        <p class="todo_content">{todo.content}</p>
        <form>
            <input type="hidden" name="id" value="{todo.card_id}"/>
            <input class="btn" type="submit" name="action" value="Delete"/>
            <input class="btn" type="submit" name="action" value="Shift"/>
        </form>
    </div>'''

def all_todos_to_html():
    '''
    Create all Todo Cards
    :return: all todos as html
    '''
    database = Database('todo.db')

    todos = database.get_all_todos()
    todos_html = ""

    for todo in todos:
        todos_html += todo_to_html(todo)
    return todos_html

def print_todo_list():
    '''
    Print all Tddo Cards in Html
    '''
    print ('<div class="todo_list">')
    print (all_todos_to_html())
    print ("</div>")

def print_todo_kanban():
    '''
    Print all Todo Cards in Kanban
    '''
    database = Database('todo.db')

    todos = database.get_all_todos()

    # Listen für die Kanban Spalten
    is_done_0 = []
    is_done_1 = []
    is_done_2 = []

    # Alle Todos in die Spalten sortieren
    for todo in todos:
        if todo.is_done == 0:
            is_done_0.append(todo)
        elif todo.is_done == 1:
            is_done_1.append(todo)
        else:
            is_done_2.append(todo)

    # Alle Spalten in html umwandeln
    kanban = '<div class="todo_kanban">'

    kanban += '<div class="todo_kanban_column todo_kanban_column_left">'
    kanban += '<h1 class="todo_kanban_column_header">To do</h1>'
    for todo in is_done_0:
        kanban += todo_to_html(todo)
    kanban += '</div>'

    kanban += '<div class="todo_kanban_column todo_kanban_column_center">'
    kanban += '<h1 class="todo_kanban_column_header">Active</h1>'
    for todo in is_done_1:
        kanban += todo_to_html(todo)
    kanban += '</div>'

    kanban += '<div class="todo_kanban_column todo_kanban_column_right">'
    kanban += '<h1 class="todo_kanban_column_header">Done</h1>'
    for todo in is_done_2:
        kanban += todo_to_html(todo)
    kanban += '</div>'

    kanban += '</div>'

    print(kanban)

def print_create_form():
    '''
    Print the input mask for todo creation
    Button to Display it has to be added seperatly!!!
    '''
    print('''
        <div class="popup" id="create-form">
            <form action="/cgi/index.cgi" class="todo_create_form">
                <h2>Create new TODO</h2>
                <input type="text" placeholder="Title" name="title" required>
                <input type="text" placeholder="Content" name="content" required>
                <select id="colors" name="color">
                    <option value="yellow">yellow</option>
                    <option value="green">green</option>
                    <option value="orange">orange</option>
                    <option value="purple">purple</option>
                    <option value="rosa">rosa</option>
                </select>
                <input type="submit" class="btn" name="action" value="Create">
                <button class="btn" onclick="closeForm()">Close</button>
            </form>
        </div>
        <script>
            function openForm() {
                document.getElementById("create-form").style.display = "block";
            }

            function closeForm() {
                document.getElementById("create-form").style.display = "none";
            }
        </script>
    ''')

def perform_action_create(form: cgi.FieldStorage):
    '''
    Created todo entry in database, via url
    :param: cgi input for create todo
    '''
    logging.debug('perform_action_create aufgerufen')
    database = Database('todo.db')
    logging.debug('database = Database("todo.db")')

    title = form.getvalue('title')
    content = form.getvalue('content')
    color = form.getvalue('color')
    is_done = 0

    todo = Todo(title, content, is_done, color=color)
    logging.debug("todo wurde erstellt:")
    logging.debug(todo)
    try:
        database.add_todo(todo)
        logging.debug("todo zur DB hinzugefügt")
    except ValueError as ex:
        logging.error(ex)

def perform_action_delete(form: cgi.FieldStorage):
    '''
    Delete todo entry in database, via url
    :param: cgi input to delete todo
    '''
    logging.debug('perform_action_delete aufgerufen')
    database = Database('todo.db')
    logging.debug('database = Database("todo.db")')

    todo_id = int(form.getvalue('id'))
    logging.debug('todo_id = %s', todo_id)

    try:
        database.remove_todo(todo_id)
        logging.debug('todo removed from DB')
    except ValueError as ex:
        logging.error(ex)

def perform_action_update(form: cgi.FieldStorage):
    '''
    Update todo entry in database, via url
    :param: cgi input to update todo
    '''
    database = Database('todo.db')
    todo_id = int(form.getvalue('id'))

    todo: Todo = database.get_todo(todo_id)

    todo.title = form.getvalue('title')
    todo.content = form.getvalue('content')
    todo.color = form.getvalue('color')

    database.update_todo(todo)

def perform_action_shift(form: cgi.FieldStorage):
    '''
    Sets the status of the todo carte to the next level
    :param: cgi input to shift todo
    '''
    database = Database('todo.db')
    todo_id = int(form.getvalue('id'))
    logging.debug('todo_id = %s', todo_id)
    todo: Todo = database.get_todo(todo_id)
    logging.debug('todo:')
    logging.debug(todo)

    try:
        todo.is_done += 1
        logging.debug('wert von isDone: %s', todo.is_done)
        database.update_todo(todo)
        logging.debug('todo shifted')
    except ValueError as ex:
        logging.error(ex)

def perform_action(form: cgi.FieldStorage):
    '''
    Action from URL validation
    :param: cgi input action
    '''
    logging.debug('vor perform action, action getValue')
    action = str(form.getvalue('action')).lower()
    logging.debug('nach perform action, action getValue')
    logging.debug('action =  %s', action)

    if action == 'create':
        logging.debug('action == create')
        perform_action_create(form)
    elif action == 'delete':
        logging.debug('action == delete')
        perform_action_delete(form)
    elif action == 'update':
        perform_action_update(form)
    elif action == 'shift':
        perform_action_shift(form)

def draw(form: cgi.FieldStorage):
    '''
    Assemble the html document
    :param: cgi input
    '''
    logging.debug('vor perform action')
    perform_action(form)
    logging.debug('nach perform action')

    # For the cgi
    print('Content-Type:text/html\n')

    # Begin html output
    print('''
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="presentation_layer/css/tonys_style.css">
        <title>TODO List</title>
    </head>
    <body>
        <header class="header">
            <h1 class="heading">TODO-List</h1>
            <button class="create-btn" onclick="openForm()">+</button>
        </header>
        <div class="content">
    ''')
    print_create_form()
    print_todo_kanban()

    print ('''
        </div>
    </body>
    </html>
    ''')
