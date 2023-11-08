import flet as ft
import time
addcounter = 0
def main(page:ft.Page):
    page.title = "ごとうぐみ"
    page.window_width = 650
    page.window_height = 1000
   
    target_domain = ft.Ref[ft.TextField]()
    start_URL = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()#プリントテスト用
    #page.bgcolor = ft.colors.TRANSPARENT
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def button_clicked(e):
        global addcounter
        target_domains = []
        stack = page.controls.pop()
        stack2 = page.controls.pop()
        for endpoint,_ in enumerate(range(addcounter+1)):
            # if target_domain.current.value ==  target_domains:
            #     print('true')
            #     page.controls.pop()
            #     page.update()
            #     continue
            """
            ドメインを格納した配列の中身と一致するドメインが入力された場合に
            処理をスキップしたいけど完全一致を検証する方法が分からない
            """
            target_domains.append(target_domain.current.value)
            if (endpoint + 1) == (addcounter+1):
                break
            page.controls.pop()
            page.update()
            time.sleep(1)
            # if (endpoint+1) < (addcounter+1):
            #     page.controls.pop()

        page.add(stack)
        page.add(stack2)
        greetings.current.controls.append(
            ft.Text(f"{start_URL.current.value}{target_domains}  ")
        )
        print(target_domains)
        start_URL.current.value = ""
        target_domain.current.value = ""
        page.update()
        # Results = Main(start_URL,target_domain)
        pass

    def addbutton_clicked(e):
        global addcounter
        addcounter += 1 
        """
        追加した回数をカウント
        マイナスボタンクリックした時に減らしていく
        最低限のドメイン入力欄を確保するために０ならばマイナス処理は行わない
        """
        stack = page.controls.pop()#ボタン一時退避
        stack2 = page.controls.pop()
        page.controls.append(ft.TextField(ref=target_domain, label="対象のドメインを入力してください",width=300,height=60))
        page.add(stack)#ボタン再配置
        page.add(stack2)
        
        
    def delbutton_clicked(e):
        global addcounter
        stack = page.controls.pop()#ボタン一時退避
        if addcounter > 0:#ドメイン入力欄を削除する。最低１つは残す
            page.controls.pop()
            addcounter -= 1
        page.add(stack)#ボタン再配置
        
    page.add(
        ft.TextField(ref=start_URL,label="探索を開始するURLを入力してください",width=550,height=80,autofocus=True,max_length=200),#autofocus=True　初期カーソル
        ft.Column(controls=[
            ft.TextField(ref=target_domain, label="対象のドメインを入力してください",width=300,height=60),
        ]),
        ft.Row([
            ft.ElevatedButton(
            "-",
            style=ft.ButtonStyle(
                side={
                    ft.MaterialState.DEFAULT:ft.BorderSide(1,ft.colors.BLACK),
                    ft.MaterialState.HOVERED:ft.BorderSide(2,ft.colors.BLACK12),
                },
                shape={
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=10),
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
                }),on_click=delbutton_clicked),
            ft.ElevatedButton(
            "+",
            style=ft.ButtonStyle(
                side={
                    ft.MaterialState.DEFAULT:ft.BorderSide(1,ft.colors.BLACK),
                    ft.MaterialState.HOVERED:ft.BorderSide(2,ft.colors.BLACK12),
                },
                shape={
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=10),
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
                }),on_click=addbutton_clicked),
            ft.ElevatedButton("探索開始", on_click=button_clicked),
        ],alignment=ft.MainAxisAlignment.START,
        ),
        ft.Column(ref=greetings),
    )
    # page.add(ft.FloatingActionButton(icon=ft.icons.ADD, on_click=addbutton_clicked))

ft.app(target=main)