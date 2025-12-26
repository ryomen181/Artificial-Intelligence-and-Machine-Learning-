import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix

data=pd.read_csv("diabetes.csv")
# Preprocess the data
data.fillna(data.median(),inplace=True)
#Define the feature set X and the target y
X=data.drop("Outcome",axis=1)
y=data['Outcome']
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=42) #Used a 70-30 split between train and test 

knn=KNeighborsClassifier(n_neighbors=5) #Class is defined by the 5 nearest datapoints
knn.fit(X_train,y_train) #Fit the feature set X and target set y in the KNN classifier
y_pred=knn.predict(X_test) #Predict the outcome on the test set

cm=confusion_matrix(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
error_rate= 1-accuracy

print("Confusion matrix:\n",cm)
print("Accuracy:",accuracy) #Percentage of Correct predictions
print("Precision:",precision) #Out of all diabetics, how many are actually diabetic
print("Recall:",recall) #Out of all diabetics, how many were correctly identified
print("Error rate:",error_rate) #Percentage of incorrect predictions
