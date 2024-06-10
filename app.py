from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []
# localhost:5000
# localhost:5000/sobre
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if request.form.get("task"):
            tasks.append(request.form.get("task"))
    return render_template(
        "index.html",
        tasks=tasks
    )
