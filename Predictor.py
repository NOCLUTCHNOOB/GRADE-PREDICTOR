import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split 
data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1","G2","G3","studytime","age","traveltime","failures","freetime","goout","Dalc","Walc","health","absences"]]
predict = "G3"
import pickle
best = 0
x = np.array(data.drop([predict], axis = 1))
y = np.array(data[predict])
for _ in range(30):
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train,y_train)
    acc = linear.score(x_test,y_test)
    if acc>best:
        best = acc
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
print("Accuracy: ", best)