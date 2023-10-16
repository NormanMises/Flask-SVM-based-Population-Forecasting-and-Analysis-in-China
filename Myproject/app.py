from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/populationAnalysis", methods=["POST", "GET"])
def populationAnalysis():
    return render_template("populationAnalysis.html")


@app.route("/populationPredictions", methods=["POST", "GET"])
def populationPredictions():
    return render_template("populationPredictions.html")


# @app.route("/update/<int:id>", methods=["GET", "POST"])
# def update(id):
#     pass
#     # if request.method == "POST":
#     #     task.content = request.form["content"]
#     #
#     #     try:
#     #         db.session.commit()
#     #         return redirect("/")
#     #     except:
#     #         return "There was an issue updating your task."
#     # else:
#     #     return render_template("update.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)
