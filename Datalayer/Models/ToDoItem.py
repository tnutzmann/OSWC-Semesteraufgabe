from turtle import title


class ToDoItem:
    """Object for TODO-Items"""
    title: str = None
    content: str = None
    isDone: bool = False

    # Constructor
    def __init__(self, title: str, content: str, isDone: bool):
        self.title = title
        self.content = content
        self.isDone = isDone

    def __str__(self):
        return self.title + "\n" + self.content + "\nDone: " + str(self.isDone)
