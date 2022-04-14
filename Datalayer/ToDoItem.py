class ToDoItem:
    """Object for TODO-Items"""
    todoID: int = -1 # todoID is set by the Database
    title: str = None
    content: str = None
    isDone: bool = False

    # Constructors
    def __init__(self, todoID:int, title: str, content: str, isDone: bool):
        self.todoID = todoID
        self.title = title
        self.content = content
        self.isDone = isDone

    def __init__(self, title: str, content: str, isDone: bool):
        self.title = title
        self.content = content
        self.isDone = isDone

    # print todoItem
    def __str__(self):
        return self.title + "\n" + self.content + "\nDone: " + str(self.isDone)
