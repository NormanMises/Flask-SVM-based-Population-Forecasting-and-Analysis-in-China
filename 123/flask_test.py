from flask import Flask,render_template,request
from 支持向量机 import SVM
svm=SVM()


#构建服务器的变量
app = Flask(__name__)

@app.route("/wight")
def wight():
    
    wight_data= svm.get_wight()
    return render_template("权重_换行.html",wight_data=wight_data)

@app.route("/pred")
def pred():
    a,b=svm.get_real_and_y_pred()
    real = list(a)
    pred = list(b)
    return render_template("预测图_echarts.html",real=real,pred=pred)

name,data=svm.read_scaler()
@app.route("/comper<int:i>", methods=["GET", "POST"])
def comper(i):
    
    xi =list( data[:,i])
    
    return render_template("数据与增长率变化趋势对比折线图.html",xi=xi)

#启动服务器  开启调试模式
app.run(debug=True)