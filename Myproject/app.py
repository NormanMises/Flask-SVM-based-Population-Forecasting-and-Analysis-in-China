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
    # print(type(wight_data))

    return render_template("populationAnalysis.html", x=x, pre=pre, wight_data=wight_data)


@app.route("/populationPredictions<int:i>", methods=["POST", "GET"])
def populationPredictions(i=0):
    a, b, c = svm.get_real_and_y_pred(all=i)
    a = list(a)
    b = list(b)
    # 读取全部数据
    pred_data = svm.read()
    # 从数据框中随机抽取20个样本
    random_sample = pred_data.sample(n=20, random_state=42)  # 设置 random_state 以确保结果可重复
    # 按照年份从小到大排序
    sorted_sample = random_sample.sort_values(by='年份')
    # 取出年份并放到列表中
    years_list = (sorted_sample['年份']+1).tolist()
    # 取出真实值放入列表中
    real_y = sorted_sample['明年自然增长率(%)'].tolist()
    # 用支持向量机计算预测值放入列表中
    pred_y = svm.pred(sorted_sample).tolist()
    return render_template("populationPredictions.html", years_list=years_list, real=real_y, pred=pred_y, a=a, b=b, c=c,
                           i=i)


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
