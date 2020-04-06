import time

from models import ToDoDB


class ToDoService:
    def __init__(self):
        self.db = ToDoDB()

    def create(self, params):
        return self.db.create(params['title'], params['description'], time.time(), params['due_date'])

    def get_all(self):
        return self.db.todos

    def delete(self, id):
        return self.db.delete_by_id(id)

    def check_done(self, id):
        return self.db.check_as_done_by_id(id)
