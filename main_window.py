from PyQt5.QtWidgets import QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToriViz")
        self.setGeometry(100, 100, 800, 600)
        label = QLabel("ここにメイン画面の内容", self)
        label.move(50, 50)