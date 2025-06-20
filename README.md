# ToriViz

ファイル構成
2025/6/20
ToriViz/
├── main.py                     # 起動スクリプト
├── main_window.py              # アプリのメインウィンドウ
│
├── widgets/
│   ├── csv_loader_window.py    # CSV読み込み専用ウィンドウ（QDialog）
│   ├── formula_input_widget.py # 数式入力UI（今後）
│   ├── binding_widget.py       # 対応付けUI（今後）
│   └── graph_display_widget.py # グラフ描画UI（今後）
│
├── utils/
│   ├── file_loader.py          # ファイル読み込み関連
│   ├── data_processing.py      # 時間補正・切り捨て・統合処理
│   ├── video_generator.py      # （動画生成処理 → moviepy + ffmpeg 想定）
│   ├── path_utils.py           # パス処理・保存先管理（必要なら）
│   └── logger.py               # ログ出力（必要なら）
│
├── templates/
│   ├── formulas/
│   └── bindings/
│
├── output/                     # デフォルトの出力フォルダ（自動生成ファイル保存）
│   ├── processed/              # 結合・補正済みデータ保存
│   ├── graphs/                 # グラフ描画ファイル
│   └── videos/                 # 動画出力ファイル
│
├── resources/                  # アイコンや設定ファイルなど
│   └── config.json             # 設定ファイル（保存先記憶など）
│
├── README.md
├── .gitignore
├── LICENSE