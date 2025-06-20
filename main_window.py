from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToriViz")
        self.setGeometry(100, 100, 800, 600)
        label = QLabel("ここにメイン画面の内容", self)
        label.move(50, 50)
        label.adjustSize()
        button_load = QPushButton("CSV読み込み")
        button_bind = QPushButton("対応付け")
        button_formula = QPushButton("数式入力")
        button_plot = QPushButton("描画")