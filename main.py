from PySide6.QtWidgets import QApplication
from iris_species_predictor import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
