import numpy as np
import pandas as pd
from PySide6.QtWidgets import QMainWindow
from ui_iris_species_predictor import Ui_MainWindow
from sklearn import svm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        df = pd.read_csv("dataset.csv")
        X, y = df.iloc[:, 1:-1].to_numpy(), df.iloc[:, -1].to_numpy()

        self.classifier = svm.SVC(kernel='linear', random_state=1, gamma=0.001, C=10)
        self.classifier.fit(X, y)
        predictions = self.classifier.predict(X)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.accuracy_score.setText(self.__accuracy(y, predictions))
        self.ui.predict_button.clicked.connect(self.__predict_button)

    def __accuracy(self, test, predictions):
        return f"{(np.sum(test == predictions) / len(test)) * 100}%"

    def __predict_button(self):
        try:
            petal_length = eval(self.ui.petal_length_lineedit.text())
            petal_width = eval(self.ui.petal_width_lineedit.text())
            sepal_width = eval(self.ui.sepal_width_lineedit.text())
            sepal_length = eval(self.ui.sepal_length_lineedit.text())
            result = self.classifier.predict(
                [[sepal_length, sepal_width, petal_length, petal_width]])[0]

            self.ui.result_label.setText(result)
        except:
            print("Error, input need to be number")
