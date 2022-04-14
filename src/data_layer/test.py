from todo import Todo
from todo_database import Database as db

db = db("foobar.db")


todo = Todo("Test1", "Das ist ein erste Test", True)
todo2 = Todo("Test2", "Das ist ein zweite Test", True)

#db.add_todo(todo)
#db.add_todo(todo2)

#foo = db.get_todo(2)

#print(foo.todo_id)
#print(foo.title)
#print(foo.content)
#print(foo.is_done)

bar = db.get_all_todos()

for i in bar:
    print(i.title)