from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():  # put application's code here
    # if request.method == "POST":
    #     pass
    # else:
    #     return render_template("index.html", tasks=tasks)
    return render_template("index.html")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    pass
    # if request.method == "POST":
    #     task.content = request.form["content"]
    #
    #     try:
    #         db.session.commit()
    #         return redirect("/")
    #     except:
    #         return "There was an issue updating your task."
    # else:
    #     return render_template("update.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)
