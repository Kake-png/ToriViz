from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QHBoxLayout, QWidget, QVBoxLayout
from widgets.csv_loader_window import CsvWindow
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToriViz")
        self.setGeometry(100, 100, 100, 100)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout) 

        button_load = QPushButton("CSV読み込み")
        button_formula = QPushButton("数式入力")
        button_bind = QPushButton("対応付け")
        button_plot = QPushButton("描画")
        
        main_layout.addWidget(button_load)
        main_layout.addWidget(button_formula)
        main_layout.addWidget(button_bind)
        main_layout.addWidget(button_plot)

        button_load.clicked.connect(self.open_csv_loader)

    def open_csv_loader(self):
        self.csv_window = CsvWindow(parent=None)  # ← 参照保持
        self.csv_window.show()
