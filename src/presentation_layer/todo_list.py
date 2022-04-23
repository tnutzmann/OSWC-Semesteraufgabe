import cgi

from data_layer.todo_database import Todo
from data_layer.todo_database import Database

def todo_to_html(todo: Todo):
    return f'''
    <div>
        <h2>{todo.card_id}. {todo.title}</h2>
        <p>{todo.content}</p>
    </div>'''

def all_todos_to_html():
    db = Database('todo.db')
    todos = db.get_all_todos()
    todos_html = ""
    for t in todos:
        todos_html += todo_to_html(t)
    return todos_html


def print_todo_list():
    print ("<h1>TODO List</h1>")
    print ("<div>")
    print (all_todos_to_html())
    print ("</div>")

def perform_action_create(form: cgi.FieldStorage):
        db = Database('todo.db')

        title = form.getvalue('title')
        content = form.getvalue('content')
        color = form.getvalue('color')

        if color != 'None':
            todo = Todo(title, content, color=color)
        else:
            todo = Todo(title, content)
        
        db.add_todo(todo)

def perform_action_delete(form: cgi.FieldStorage):
    db = Database('todo.db')
    todo_id = form.getvalue('id')
    db.remove_todo(todo_id)

def perform_action_update(form: cgi.FieldStorage):
    db = Database('todo.db')
    todo_id = form.getvalue('id')

    todo: Todo = db.get_todo(todo_id)

    todo.title = form.getvalue('title')
    todo.content = form.getvalue('content')
    todo.color = form.getvalue('color')

    db.update_todo(todo)

def perform_action_shift(form: cgi.FieldStorage):
    db = Database('todo.db')
    todo_id = form.getvalue('id')
    todo: Todo = db.get_todo(todo_id)

    if todo.is_done < 2:
        todo.is_done += 1
        db.update_todo(todo)

def perform_action(form: cgi.FieldStorage):
    action = form.getvalue('action')
    match action:
        case 'create':
            perform_action_create(form)
        case 'delete':
            perform_action_delete(form)
        case 'update':
            perform_action_update(form)
        case 'shift':
            perform_action_shift(form)

def draw(form: cgi.FieldStorage):
    perform_action(form)

    print('Content-Type:text/html\n')
    print('<!DOCTYPE html>')
    print('<html lang="de">')
    print ("<head>")
    print ("<title>TODO List</title>")
    print ("</head>")
    print ("<body>")

    print_todo_list()

    print ("</body>")
    print ("</html>")