class ToDoModel:
    def __init__(self, title, description, created_on, due_date, id, is_deleted=False, is_done=False):
        self.id = id
        self.title = title
        self.description = description
        self.created_on = created_on
        self.due_date = due_date
        self._is_deleted = is_deleted
        self._is_done = is_done

    def to_json(self):
        return {'id': self.id,
                'title': self.title,
                'description': self.description,
                'created_on': self.created_on,
                'due_date': self.due_date,
                'is_deleted': self._is_deleted,
                'is_done': self._is_done}


class ToDoDB:
    def __init__(self):
        self.todos = []
        self.id_counter = 0

    def create(self, title, description, created_on, due_date):
        todo = ToDoModel(title, description, created_on, due_date, self.id_counter)
        self.id_counter += 1
        self.todos.append(todo)
        return todo

    def find_by_id(self, id):
        for todo in self.todos:
            if int(todo.id) == int(id):
                return todo

    def delete_by_id(self, id_to_delete):
        todo = self.find_by_id(id_to_delete)
        todo._is_deleted = True
        return todo

    def check_as_done_by_id(self, id_done):
        todo = self.find_by_id(id_done)
        todo._is_done = True
        return todo
