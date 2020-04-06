from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from service import ToDoService

app = Flask(__name__)
to_do_service = ToDoService()


@app.route('/todo', methods=["GET"])
def home():
    res = to_do_service.get_all()
    print(res)
    return render_template('index.html', todos=res)


@app.route('/todo', methods=["POST"])
def create_todo():
    print(to_do_service.create(request.form))
    return redirect('/todo')


@app.route('/delete/<id>')
def delete_todo(id):
    print(to_do_service.delete(id))
    return redirect('/todo')


@app.route('/done/<id>')
def check_todo_as_done(id):
    print(to_do_service.check_done(id))
    return redirect('/todo')

if __name__ == '__main__':
    app.run(debug=True)
