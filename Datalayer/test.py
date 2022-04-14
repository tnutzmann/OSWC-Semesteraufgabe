from ToDoItem import ToDoItem
from TODO_DB import DbHandler

db = DbHandler("test.db")
todo = ToDoItem("Test2", "Das ist ein zweiter Test", True)

#db.addTodoToDB(todo)
print(db.getAllTodoFromDB())

db.removeTodoFromDB(1)

print(db.getAllTodoFromDB())