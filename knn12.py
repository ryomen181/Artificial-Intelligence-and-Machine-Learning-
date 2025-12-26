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
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=42)

knn=KNeighborsClassifier(n_neighbors=5) #Class is defined by the 5 nearest datapoints
knn.fit(X_train,y_train) 
y_pred=knn.predict(X_test)

cm=confusion_matrix(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
error_rate= 1-accuracy
print("Confusion matrix:\n",cm)
print("Accuracy:",accuracy)
print("Precision:",precision)
print("Recall:",recall)
print("Error rate:",error_rate)
