import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler


class SVM:
    def __init__(self) -> None:
        scaler = StandardScaler()
        self.df = pd.read_csv('./data/ChinaPopulation.csv')
        self.df_scaler = scaler.fit_transform(self.df)
        self.name = self.df.columns
        # X=df.filter(regex='[^自然增长率(%)]')[:-1]
        y = np.array(self.df['自然增长率(%)'][1:])  # 明年自然增长率

        X_scaled = self.df_scaler[:, :-1]

        # 手动划分数据集
        # X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        train = [i for i in range(40)]
        test = [i for i in range(40, 49)]
        X_train, X_test, y_train, y_test = X_scaled[train], X_scaled[test], y[train], y[test]

        # 初始化SVM回归模型
        svr = svm.SVR(kernel='linear')  # 这里使用了线性核函数

        # 训练模型  
        svr.fit(X_train, y_train)
        self.y_test = y_test

        # 对测试集进行预测  
        self.y_pred = svr.predict(X_test)

        # 计算均方误差（MSE）  
        mse = mean_squared_error(self.y_test, self.y_pred)
        print('Mean Squared Error:', mse)

        self.wight = svr.coef_

    def read(self):
        return self.df

    def read_scaler(self):
        return self.name, self.df_scaler

    def get_wight(self):
        return self.wight

    def get_real_and_y_pred(self):
        return self.y_test, self.y_pred
