import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import metrics

df = sns.load_dataset('iris')
user_predict = float(input('enter a petal width to predict length'))

def LinearRegressionPlot():
    global user_predict
    sns.lmplot(x='petal_width', y='petal_length', data=df)
    plt.title('petal_width vs petal_length')
    plt.xlim(0, 2.75)
    plt.axvline(user_predict)
    plt.show()

def LinearRegressionAlgo():
    X = df['petal_width']
    y = df['petal_length']

    # TTS
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

    # refer to model
    lm = LinearRegression()

    # fit data
    lm.fit(np.array(X_train).reshape(-1, 1), np.array(y_train).reshape(-1, 1))

    # predict
    global user_predict
    print('Prediction:', float(lm.predict(np.array(user_predict).reshape(-1, 1))))

    # score
    print('Accuracy:', lm.score(np.array(X_test).reshape(-1, 1), np.array(y_test).reshape(-1, 1)) * 100)

    # predictions
    predictions = lm.predict(np.array(y_test).reshape(-1, 1))

    def errors():
        MAE = metrics.mean_absolute_error(y_test, predictions)
        MSE = metrics.mean_squared_error(y_test, predictions)
        RMSE = np.sqrt(metrics.mean_squared_error(y_test, predictions))
        print('MAE: {}\nMSE: {}\nRMSE: {}\n'.format(MAE, MSE, RMSE))
    errors()

    def predictionPlot():
        x, y = y_test, predictions
        plt.scatter(x, y)
        plt.title('y_test vs predictions')
    predictionPlot()

LinearRegressionAlgo()
LinearRegressionPlot()
