from flask import Flask, render_template, request, redirect
import json
import os

return render_template("index.html", tasks=tasks)


app = Flask(__name__)
DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
    return redirect("/")

@app.route("/done/<int:index>")
def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
