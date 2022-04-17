import os, sys

#currentdir = os.path.dirname(os.path.realpath(__file__))
#parentdir = os.path.dirname(currentdir)
#sys.path.append(parentdir)

from data_layer.todo import Todo
from data_layer.todo_database import Database

def todo_to_html(todo: Todo):
    return f'''
    <div>
        <h2>{todo.card_id}. {todo.title}</h2>
        <p>{todo.content}</p>
    </div>'''

def all_todos_to_html():
    db = Database('foobar.db')
    todos = db.get_all_todos()
    todos_html = ""
    for t in todos:
        todos_html += todo_to_html(t)
    return todos_html

# Just for testing
def print_all():
    print ("<html>")
    print ("<head>")
    print ("<title>TODO List</title>")
    print ("</head>")
    print ("<body>")
    print ("<h1>TODO List</h1>")
    print ("<div>")
    print (all_todos_to_html())
    print ("</div>")
    print ("</body>")
    print ("</html>")