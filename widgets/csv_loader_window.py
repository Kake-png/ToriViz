from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                             QFileDialog, QHBoxLayout, QWidget, QVBoxLayout, 
                             QRadioButton, QButtonGroup, QLineEdit, 
                             QCheckBox)
from PyQt5.QtGui import QIntValidator 
import sys
import utils.file_loader

class CsvWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CSV_loader")
        self.setGeometry(250, 100, 400, 200)
        csv_main_widget = QWidget(self)
        self.setCentralWidget(csv_main_widget)

        csv_main_layout = QVBoxLayout()
        csv_main_widget.setLayout(csv_main_layout)

        self.radio_folder = QRadioButton("フォルダ読み込み")
        self.radio_file = QRadioButton("ファイル読み込み")
        self.radio_folder.setChecked(True)  # 初期選択

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_folder, id=0)
        self.button_group.addButton(self.radio_file, id=1)

        csv_main_layout.addWidget(self.radio_folder)

        # フォルダ選択UI
        folder_layout = QHBoxLayout()
        self.folder_path_label = QLabel("フォルダを選択してください")
        self.folder_select_btn = QPushButton("フォルダ選択")
        folder_layout.addWidget(self.folder_select_btn)
        folder_layout.addWidget(self.folder_path_label)
        csv_main_layout.addLayout(folder_layout)

         # 間隔入力
        interval_layout = QHBoxLayout()
        interval_layout.addWidget(QLabel("間隔 (ms):"))
        self.interval_input = QLineEdit()
        self.interval_input.setValidator(QIntValidator())
        interval_layout.addWidget(self.interval_input)
        csv_main_layout.addLayout(interval_layout)

        output_layout = QHBoxLayout()
        checkbox = QCheckBox("出力")
        #checkbox.setChecked(True)  # ← 初期状態でチェックを入れる場合
        self.folder_path_label = QLabel("フォルダを選択してください")
        self.folder_select_btn = QPushButton("フォルダ選択")

        output_layout.addWidget(checkbox)
        output_layout.addWidget(self.folder_select_btn)
        output_layout.addWidget(self.folder_path_label)

        csv_main_layout.addLayout(output_layout)


        line_layout = QHBoxLayout()
        self.line_label = QLabel("\n---------------------------------------------------------\n")
        line_layout.addWidget(self.line_label)
        csv_main_layout.addLayout(line_layout)
       



        csv_main_layout.addWidget(self.radio_file)


        # ファイル選択UI
        file_layout = QHBoxLayout()
        self.file_path_label = QLabel("ファイルを選択してください")
        self.file_select_btn = QPushButton("ファイル選択")
        file_layout.addWidget(self.file_select_btn)
        file_layout.addWidget(self.file_path_label)
        csv_main_layout.addLayout(file_layout)

        # 実行ボタン
        self.exec_button = QPushButton("実行")
        csv_main_layout.addWidget(self.exec_button)

        

    def run_action(self):
        print("実行ボタンが押されたよ")


