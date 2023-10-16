from flask import Flask, render_template

from SVM import SVM

svm = SVM()

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/populationAnalysis", methods=["POST", "GET"])
def populationAnalysis():
    name, data = svm.read_scaler()
    x = [list(i) for i in data.transpose()[:-1]]
    pre = ['年份', '出生人口', '总人口', '人均GPA', '性别比例', '就业人口', '城镇人口', '乡村人口',
           '美元兑换人民币汇率']

    wight_data = list(svm.get_wight()[0])
    print(type(wight_data))

    return render_template("populationAnalysis.html", x=x, pre=pre, wight_data=wight_data)


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
