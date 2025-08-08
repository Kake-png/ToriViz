# ToriViz開発日誌

---

## 8/5
***DearPyGUIについて***
    モダンなGUIを作るライブラリ(2020~)<br>
    gptの勉強量足りないかも<br>

    **DPGの使い方**
        画面に表示するウィンドウ自体はviewportと呼ぶ
        その中にwindowと呼ばれる単位の枠を収める
        windowはデフォルトで
            上部に名前付き
            ドラッグ可能
            ×ボタンとかも実装
        withでひとつのwindowに何を書くかをまとめる
    
    **コード例**
        dpg.create_context() #初期化

        with dpg.font_registry(): #日本語設定
            jp_font = dpg.add_font("Noto_Sans_JP/static/NotoSansJP-Regular.ttf",  24, pixel_snapH=True)
            dpg.add_font_range_hint(parent=jp_font, hint=dpg.mvFontRangeHint_Japanese) #"これは日本語フォント"という宣言

        dpg.create_viewport(title="ToriViz", width=800, height=600) #viewport設定
        dpg.set_viewport_clear_color([255, 255, 255, 255])

        with dpg.window(label="ToriViz"): #window作る
            dpg.add_button(label="Button",  callback=button_callback, pos=[200,120]) 

        dpg.bind_font(jp_font) #フォント指定

        dpg.setup_dearpygui() #描画
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

        with dpg.theme() as window_theme1: #windowの色
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (247,247,247,255), category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme(Toriviz,       window_theme1) <-これをwindowの中に書く

***全体の設計について***
最初は表示する計器を固定して、ファイル選択->範囲選択->描画　だけ

---
## 8/8
***ファイル読み込み部制作開始***
ファイル読み込みUI：
    with dpg.file_dialog(directory_selector=False, show=False, callback=file_selected, tag="file_dialog_id"):
        dpg.add_file_extension(".*")
        dpg.add_file_extension(".csv", color=(255, 0, 0, 255))
file_dialog:ソフトでファイル読み出しとかの処理をするときに出てくるfinderとかのあの画面
これをwindowのボタンで呼び出す
