import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
heart_disease = pd.read_csv('../data/heart-disease.csv')
head = heart_disease.head()

# Remove target column (whether person has heart disease or not)
X = heart_disease.drop("target", axis=1)

# Empty column to hold our prediction 
y = heart_disease["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

clf.fit(X=X_train, y=y_train)

y_preds = clf.predict(X=X_test)

train_acc = clf.score(X=X_train, y=y_train)
print(f"Model train accuracy is {train_acc * 100}%")

test_acc = clf.score(X=X_test, y=y_test)
print(f"Model test accuracy is {test_acc * 100}%")