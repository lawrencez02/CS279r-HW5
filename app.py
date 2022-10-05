# import relevant Flask libraries
from flask import Flask, render_template, request, redirect, url_for

# initialize the application
app = Flask(__name__)

# global id number counter for tasks
id_num = 1
# global list of todo task items
todos = []

# the home page of the application
@app.route("/")
def home():
    # just renders the base HTML page with the full list of todos
    return render_template("base.html", todo_list=todos)


# when user submits the form and wants to add a todo task
@app.route("/add", methods=["POST"])
def add():
    global id_num
    # add the new task to the todos list, with title of what the user inputted
    todos.append({"title": request.form.get("title"), "id": id_num, "complete": False})
    # increment id_num so that no 2 tasks have same id number
    id_num += 1
    # redirect to the homepage, i.e., the full list of todos
    return redirect(url_for("home"))


# when user clicks an update button to toggle the completed state of a task
@app.route("/update/<int:todo_id>")
def update(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            # toggle one specific task's complete status
            todo["complete"] = not todo["complete"]
            break
    # redirect to the homepage, i.e., the full list of todos
    return redirect(url_for("home"))


# when user clicks a delete button to delete a task
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            # delete one specific task from the todos list
            todos.pop(i)
            break
    # redirect to the homepage, i.e., the full list of todos
    return redirect(url_for("home"))

# run the application
if __name__ == "__main__":
    app.run(debug=True)
