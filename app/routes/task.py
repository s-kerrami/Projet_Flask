from app import app
from flask import redirect, render_template, url_for

from app.models.forms.task_form import TaskForm

tasks = []

@app.route('/task/new', methods=['GET', 'POST'])
def newTask():
    # Déclaration d'une variable de type task_form
    form = TaskForm()
    
    # post
    if form.validate_on_submit():
        new_task = {
            'nom' : form.nom.data,
            'description' : form.description.data
        }

        tasks.append(new_task)
        
        print("------------")
        for task in tasks:
            print(task)
        print("------------")
        
        return redirect(url_for('index'))
    # get
    return render_template('task/create_task.html', form=form)