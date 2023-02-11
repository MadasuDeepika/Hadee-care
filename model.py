import pandas as pd
import numpy as np 
import pickle
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
df = pd.read_csv('E:\\Bootstrap\\PCOS-Predictor Final\\pcos files\\full3 (1).csv') 
print(df.shape)
df.describe().transpose()
X=df.drop(columns = ['PCOS'])
y = df['PCOS']
y = np.array(y)
X= np.array(X)
y = y.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=None)
print(X_train.shape); print(X_test.shape)
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(5,8,5), activation='relu', solver='adam', max_iter=1000)
mlp.fit(X_train,y_train.ravel())

predict_train = mlp.predict(X_train)
predict_test = mlp.predict(X_test)
pickle.dump(mlp, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_train,predict_train))

print(classification_report(y_train,predict_train))
print(confusion_matrix(y_test,predict_test))
print(classification_report(y_test,predict_test))
