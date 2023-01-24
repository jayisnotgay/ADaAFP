from PySide6.QtWidgets import QApplication
from iris_species_predictor_DecisionTree import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
