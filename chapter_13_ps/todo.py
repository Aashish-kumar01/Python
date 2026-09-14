from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []  # global task list

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template("todo.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)

# app.run()

