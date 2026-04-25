import joblib
from sklearn.svm import LinearSVC

def train_model(X_train, y_train):
    model = LinearSVC()
    model.fit(X_train, y_train)
    joblib.dump(model, "models/model.pkl")
    return model

def load_model():
    return joblib.load("models/model.pkl")