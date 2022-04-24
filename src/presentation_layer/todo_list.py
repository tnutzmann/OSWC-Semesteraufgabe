'''
Contains all the functions that are necessary to create the website.
'''

import cgi
from data_layer.todo_database import Todo
from data_layer.todo_database import Database

def todo_to_html(todo: Todo):
    '''
   Create the Todo Card Div.
    '''
    return f'''
    <div class="todo {todo.color} state_{todo.is_done}" id="todo_{todo.card_id}">
        <h2 class="todo_header">#{todo.card_id} {todo.title}</h2>
        <p class="todo_content">{todo.content}</p>
    </div>'''

def all_todos_to_html():
    '''
    Create all Todo Cards
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
    #print ("<h1>TODO List</h1>")
    print ('<div class="todo_list">')
    print (all_todos_to_html())
    print ("</div>")

def print_todo_kanban():
    '''
    Print all Tddo Cards in Kanban
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

    return kanban


def perform_action_create(form: cgi.FieldStorage):
    '''
    Created todo entry in database, via url
    '''

    database = Database('todo.db')

    title = form.getvalue('title')
    content = form.getvalue('content')
    color = form.getvalue('color')

    todo = Todo(title, content, color)

    database.add_todo(todo)

def perform_action_delete(form: cgi.FieldStorage):
    '''
    Delete todo entry in database, via url
    '''
    database = Database('todo.db')
    todo_id = form.getvalue('id')
    database.remove_todo(todo_id)

def perform_action_update(form: cgi.FieldStorage):
    '''
    Update todo entry in database, via url
    '''
    database = Database('todo.db')
    todo_id = form.getvalue('id')

    todo: Todo = database.get_todo(todo_id)

    todo.title = form.getvalue('title')
    todo.content = form.getvalue('content')
    todo.color = form.getvalue('color')

    database.update_todo(todo)

def perform_action_shift(form: cgi.FieldStorage):
    '''
    Sets the status of the todo carte to the next level
    '''
    database = Database('todo.db')
    todo_id = form.getvalue('id')
    todo: Todo = database.get_todo(todo_id)

    if todo.is_done < 2:
        todo.is_done += 1
        database.update_todo(todo)

def perform_action(form: cgi.FieldStorage):
    '''
    Action from URL validation
    '''
    action = form.getvalue('action')

    if action == 'create':
        perform_action_create(form)
    if action == 'delete':
        perform_action_delete(form)
    if action == 'update':
        perform_action_update(form)
    if action == 'shift':
        perform_action_shift(form)

def draw(form: cgi.FieldStorage):
    '''
    Assemble the html document
    '''
    perform_action(form)
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
        <div class="actions_container popup">
            <form action="/cgi/index.cgi" class="todo_create_form">
                <input type="text" placeholder="Title" name="title" required>
                <input type="text" placeholder="Content" name="content" required>
                <select id="colors" name="color">
                    <option value="yellow">yellow</option>
                    <option value="green">green</option>
                    <option value="orange">orange</option>
                    <option value="purple">purple</option>
                    <option value="rosa">rosa</option>
                </select>
                <input type="submit" class="button" name="action" value="create">
            </form>
        </div>
    ''')

    print(print_todo_kanban())
    #print_todo_list()

    print ('''
    </body>
    </html>
    ''')
