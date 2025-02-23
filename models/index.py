from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, precision_score, recall_score


class BaseModel:
    def __init__(self, model, X_test, y_test):
        self.model = model
        self.X_test = X_test
        self.y_test = y_test

    def predict(self):
        return self.model.predict(self.X_test)

    def score(self):
        return self.model.score(self.X_test, self.y_test)

    def report(self):
        predict_values = self.model.predict(self.X_test)
        return classification_report(predict_values, self.y_test)

    def precision(self):
        return precision_score(self.y_test, self.predict())

    def recall(self):
        return recall_score(self.y_test, self.predict())


class DecisionTree(BaseModel):
    def __init__(self, X_train, y_train, X_test, y_test):
        self.dt = DecisionTreeClassifier()
        self.dt.fit(X_train, y_train)

        super(DecisionTree, self).__init__(self.dt, X_test, y_test)


class RandomForest(BaseModel):
    def __init__(self, X_train, y_train, X_test, y_test):
        self.rf = RandomForestClassifier()
        self.rf.fit(X_train, y_train)

        super(RandomForest, self).__init__(self.rf, X_test, y_test)


class NaiveBayes(BaseModel):
    def __init__(self, X_train, y_train, X_test, y_test):
        self.gnb = GaussianNB()
        self.gnb.fit(X_train, y_train)

        super(NaiveBayes, self).__init__(self.gnb, X_test, y_test)


class SupportVector(BaseModel):
    def __init__(self, X_train, y_train, X_test, y_test):
        self.svc = LinearSVC()
        self.svc.fit(X_train, y_train)

        super(SupportVector, self).__init__(self.svc, X_test, y_test)


class MLPerceptron(BaseModel):
    def __init__(self, X_train, y_train, X_test, y_test):
        self.mlp = MLPClassifier()
        self.mlp.fit(X_train, y_train)

        super(MLPerceptron, self).__init__(self.mlp, X_test, y_test)


class LogRegression(BaseModel):
    def __init__(self, X_train, y_train, X_test, y_test):
        self.logr = LogisticRegression(max_iter=10000)
        self.logr.fit(X_train, y_train)

        super(LogRegression, self).__init__(self.logr, X_test, y_test)


class Models:
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test

    def decision_tree(self):
        return DecisionTree(
            self.X_train,
            self.y_train,
            self.X_test,
            self.y_test
        )

    def random_forest(self):
        return RandomForest(
            self.X_train,
            self.y_train,
            self.X_test,
            self.y_test
        )

    def naive_bayes(self):
        return NaiveBayes(
            self.X_train,
            self.y_train,
            self.X_test,
            self.y_test
        )

    def support_vector(self):
        return SupportVector(
            self.X_train,
            self.y_train,
            self.X_test,
            self.y_test
        )

    def multi_layer_perceptron(self):
        return MLPerceptron(
            self.X_train,
            self.y_train,
            self.X_test,
            self.y_test
        )

    def logistic_regression(self):
        return LogRegression(
            self.X_train,
            self.y_train,
            self.X_test,
            self.y_test
        )


def print_metrics(model, model_name):
    print(f"{model_name} accuracy: ", model.score())
    print(f"{model_name} precision: ", model.precision())
    print(f"{model_name} recall: ", model.recall())

