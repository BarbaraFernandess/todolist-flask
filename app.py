from flask import Flask, render_template, request

app = Flask(__name__)

tasksList = []
# localhost:5000
# localhost:5000/sobre
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if request.form.get("task") != "":
            tasksList.append(request.form.get("task"))
    return render_template(
        "index.html",
        tasksList=tasksList
    )
    
@app.route('/remove/<task>', methods=['POST', 'GET'])
def remove(task):
    if task in tasksList:
        tasksList.remove(task)
    return render_template(
        "index.html",
        tasksList=tasksList
    )
    
@app.route('/clean')
def clean():
    tasksList.clear()
    return render_template(
        "index.html",
        tasksList=tasksList
    )