from flask import Flask,render_template,request

   

#构建服务器的变量
app = Flask(__name__)

@app.route("/wight")
def city_salary():
    
    wight_data= [-0.49, 2.48, -0.95, -0.53, -0.05, 0.2, -0.13, -0.28, -0.95]
    return render_template("权重图_换行.html",wight_data=wight_data)


#启动服务器  开启调试模式
app.run(debug=True)