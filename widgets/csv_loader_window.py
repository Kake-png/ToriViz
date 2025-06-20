from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                             QFileDialog, QHBoxLayout, QWidget, QVBoxLayout, 
                             QRadioButton, QButtonGroup, QLineEdit, 
                             )
#from PyQt5.QtGui import QIntValidator 
import sys

class CsvWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CSV_loader")
        self.setGeometry(300, 100, 400, 400)
        csv_main_widget = QWidget(self)
        self.setCentralWidget(csv_main_widget)

        csv_main_layout = QVBoxLayout()
        csv_main_widget.setLayout(csv_main_layout)

        self.radio_folder = QRadioButton("フォルダ選択")
        self.radio_file = QRadioButton("ファイル選択")
        self.radio_folder.setChecked(True)  # 初期選択

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_folder, id=0)
        self.button_group.addButton(self.radio_file, id=1)

        csv_main_layout.addWidget(self.radio_folder)

        # フォルダ選択用の行（ラジオボタン1のオプション）
        folder_layout = QHBoxLayout()
        self.interval_input = QLineEdit()
        #self.interval_input.setValidator(QIntValidator())
        self.interval_input.setPlaceholderText("間隔(ms)")
        folder_layout.addWidget(QLabel("間隔:"))
        folder_layout.addWidget(self.interval_input)
        csv_main_layout.addLayout(folder_layout)

        csv_main_layout.addWidget(self.radio_file)

        # 実行ボタン
        exec_button = QPushButton("実行")
        exec_button.clicked.connect(self.run_action)
        csv_main_layout.addWidget(exec_button)

    def run_action(self):
        print("実行ボタンが押されたよ")


