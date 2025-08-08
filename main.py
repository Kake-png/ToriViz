from dataclasses import dataclass
import dearpygui.dearpygui as dpg
import pandas as pd

filename = ""


@dataclass
class Data:
    name: str
    data: pd.DataFrame

dpg.create_context()

def button_callback():
      print("Pushied!!")

def do():
    global filename
    

def file_selected(sender, app_data):
    print("選択されたファイル:", app_data['file_path_name'])

def file_selected_callback(sender, app_data):
    global filename
    # ファイルのフルパスを取得
    selected_path = app_data['file_path_name']
    filename = selected_path
    print("選択されたファイル:", selected_path)
    dpg.set_value("file_path_text", selected_path)  # テキストに表示

# フォントを読み込んで登録
with dpg.font_registry():
    jp_font = dpg.add_font("Noto_Sans_JP/static/NotoSansJP-Regular.ttf",  24, pixel_snapH=True)
    dpg.add_font_range_hint(parent=jp_font, hint=dpg.mvFontRangeHint_Japanese)

# ★ テーマを作る
with dpg.theme() as window_theme1:
          with dpg.theme_component(dpg.mvAll):
                  dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (247,247,247,255), category=dpg.mvThemeCat_Core)
# ビューポート作成
dpg.create_viewport(title="ToriViz", width=800, height=600)
dpg.set_viewport_clear_color([255, 255, 255, 255])


with dpg.window(label="ToriViz", 
    no_move=True,
    no_resize=True,
    no_close=True,
    no_collapse=True,
    no_title_bar=True,
    width=800,
    height=600,
    pos=[0, 0]) as Toriviz:
    dpg.add_text("Hello, world", color=[150,200,255])
    dpg.bind_item_theme(Toriviz,       window_theme1)
    dpg.add_input_text(label="選択されたファイル", tag="file_path_text", readonly=True, width=500)
    dpg.add_button(label="Button",  callback=button_callback, pos=[200,120])
    dpg.add_spacer(height=10)

    # ファイル選択ボタン
    dpg.add_button(label="ファイルを選択", callback=lambda: dpg.show_item("file_dialog_id"))

    # 非表示のファイルダイアログ（FinderやExplorerみたいなの）
    with dpg.file_dialog(directory_selector=False, show=False, callback=file_selected_callback, tag="file_dialog_id"):
        dpg.add_file_extension(".csv", color=(0, 255, 0, 255))  # CSVだけ表示
        dpg.add_file_extension(".*", color=(255, 255, 255, 255))  # 全部表示（保険）

    
dpg.bind_font(jp_font)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
