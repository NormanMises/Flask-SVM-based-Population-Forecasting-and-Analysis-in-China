import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler


class SVM:
    def __init__(self) -> None:
        self.scaler = StandardScaler()
        self.df = pd.read_csv('./data/ChinaPopulation.csv')
        self.df_scaler = self.scaler.fit_transform(self.df)
        self.name = self.df.columns
        # X=df.filter(regex='[^自然增长率(%)]')[:-1]
        y = np.array(self.df['自然增长率(%)'])[1:]  # 明年自然增长率
        self.y = y

        X_scaled = self.df_scaler[:, :-1]

        # 手动划分数据集
        # X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        train = [i for i in range(40)]
        test = [i for i in range(40, 49)]
        X_train, X_test, y_train, y_test = X_scaled[train], X_scaled[test], y[train], y[test]

        # 初始化SVM回归模型
        self.svr = svm.SVR(kernel='linear')  # 这里使用了线性核函数

        # 训练模型  
        self.svr.fit(X_train, y_train)
        self.y_test = y_test

        # 对测试集进行预测  
        self.y_pred = self.svr.predict(X_test)
        self.y_pred_all = self.svr.predict(X_scaled)

        # 计算均方误差（MSE）  
        mse = mean_squared_error(self.y_test, self.y_pred)
        print('Mean Squared Error:', mse)

        self.wight = self.svr.coef_

    # 处理新的数据
    def pred(self, data):
        y = data['自然增长率(%)']
        X = self.scaler.transform(data)[:, :-1]
        return self.svr.predict(X)

    # 读取表格的原始数据
    def read(self):
        return self.df

    # 读取标准化之后的数据（由于标准化之后是numpy类型，不像df还有个列名，所以贴心的返回一个列名表name）
    def read_scaler(self):
        return self.name, self.df_scaler

    # 获取训练的权重二维numpy类型
    def get_wight(self):
        return self.wight

    # 获取数据集的标签和预测值，还贴心的返回了一个日期
    def get_real_and_y_pred(self, all=0):
        if all == 0:
            # 如果不指定要全部（all==0），就只返回测试集的数据（2011年以后的）
            date = [2011 + i for i in range(9)]
            return self.y_test, self.y_pred, date
        # 如果指定了要全部（all！=0），就只返回所有的数据
        date = [1971 + i for i in range(49)]
        return self.y, self.y_pred_all, date


if __name__ == '__main__':
    svm = SVM()
    data = svm.read()
    data10 = data.sample(n=10)
    print(type(data10))
    y_ = svm.pred(data10)
    print(list(y_))
