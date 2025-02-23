import pandas
from sklearn.model_selection import train_test_split

from data.columns import FEATURE_COLUMNS
from models.index import Models, print_metrics
from models.neural_network import train_shallow, train_deepish, train_deep

columns = FEATURE_COLUMNS

# read files

df = pandas.read_csv("../csv/ScoreboardPlayerCountering.csv", sep=";")
df = df.dropna()

X = df[columns].to_numpy()
y = df["Winner"].to_numpy()

for index, value in enumerate(y):
    y[index] = value - 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = Models(X_train, y_train, X_test, y_test)

dt = models.decision_tree()
print_metrics(dt, "Decision Tree")

rf = models.random_forest()
print_metrics(rf, "Random Forest")

gnb = models.naive_bayes()
print_metrics(gnb, "Naive Bayes")

svm = models.support_vector()
print_metrics(svm, "SVM")

logr = models.logistic_regression()
print_metrics(logr, "LogR")

shallow = train_shallow(X_train, X_test, y_train, y_test, columns)
deepish = train_deepish(X_train, X_test, y_train, y_test, columns)
deep = train_deep(X_train, X_test, y_train, y_test, columns)
