import unittest
from src.data_layer.todo_database import Todo
from src.data_layer.todo_database import Database


class TestTodo(unittest.TestCase):

    def test_area_todo(self):
        todo = Todo('Test1', 'Das ist ein erster Test', True)
        self.assertAlmostEqual(todo.title, 'Test1')
        self.assertAlmostEqual(todo.content, 'Das ist ein erster Test')
        self.assertAlmostEqual(todo.is_done, True)
        self.assertAlmostEqual(todo.card_id, -1)
        self.assertAlmostEqual(todo.color, 'yellow')

        for i in range(0,2):
            todo.is_done = i
            self.assertAlmostEqual(todo.is_done, i)


        todo2 = Todo('Test2', 'Das ist ein zweiter Test', True, 15)
        self.assertAlmostEqual(todo2.title, 'Test2')
        self.assertAlmostEqual(todo2.content, 'Das ist ein zweiter Test')
        self.assertAlmostEqual(todo2.is_done, True)
        self.assertAlmostEqual(todo2.card_id, 15)

    def test_title_property(self):
        todo = Todo('titel', 'content')
        with self.assertRaises(ValueError):
            todo.title = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            todo.is_done = -1
            todo.is_done = 4

    def test_area_db(self):
        db = Database('test.db')

        todo = Todo('Test1', 'Das ist ein erster Test', True)
        todo2 = Todo('Test2', 'Das ist ein zweiter Test', True)

        db.add_todo(todo)
        db.add_todo(todo2)

        db_todo = db.get_todo(2)
        self.assertAlmostEqual(db_todo.title, 'Test2')
        self.assertAlmostEqual(db_todo.content, 'Das ist ein zweiter Test')
        self.assertAlmostEqual(db_todo.is_done, True)
        self.assertAlmostEqual(db_todo.card_id, 2)

if __name__ == '__main__':
    unittest.main()