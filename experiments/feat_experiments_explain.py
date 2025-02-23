import pandas
import shap.plots
from sklearn.model_selection import train_test_split

from data.columns import FEATURE_COLUMNS
from models.index import Models, print_metrics

columns = FEATURE_COLUMNS

# read files

df = pandas.read_csv("../csv/ScoreboardPlayerCountering.csv", sep=";")
df = df.dropna()

X = df[columns]
y = df["Winner"].to_numpy().tolist()

for index, value in enumerate(y):
    y[index] = value - 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = Models(X_train, y_train, X_test, y_test)

rf = models.random_forest()
print_metrics(rf, "RF")

explainer = shap.Explainer(rf.rf, X_train)
explanation = explainer(X_train)
shap_values = explanation.values

shap.plots.bar(explanation[:, :, 0])
