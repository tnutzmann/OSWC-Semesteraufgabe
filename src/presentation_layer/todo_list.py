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

# Just for testing
def print_all():
    print ("<h1>TODO List</h1>")
    print ("<div>")
    print (all_todos_to_html())
    print ("</div>")

def draw(form: cgi.FieldStorage):
    print('Content-Type:text/html\n')
    print('<!DOCTYPE html>')
    print('<html lang="de">')
    print ("<head>")
    print ("<title>TODO List</title>")
    print ("</head>")
    print ("<body>")
    
    print_all()

    print ("</body>")
    print ("</html>")