import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

def convert_txt_to_numpy(inputdata):
    data=np.genfromtxt(inputdata)
    return data


x = convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW2/digits')
y= convert_txt_to_numpy('/Users/amirhossein/Desktop/term8/cpmplex/projects/HW2/realIdx')

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))

