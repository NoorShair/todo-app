from app.todo.models import Task
from app import db
from flask import Blueprint, render_template, request, redirect, url_for


todo_blueprint= Blueprint(
    'todo',
    __name__,
    template_folder='templates'
)


# @todo_blueprint.route('/')
# def index():
#     return render_template('hello_world.html')

@todo_blueprint.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@todo_blueprint.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['content']
    new_task = Task(content=task_content)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('todo.index'))


@todo_blueprint.route('/update/<int:id>')
def update_task(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('todo.index'))


@todo_blueprint.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo.index'))
