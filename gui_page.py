import flet as ft
import time
addcounter = 0
def main(page:ft.Page):
    page.title         = "ごとうぐみ"
    page.window_width  = 650
    page.window_height = 1000
    target_domains     = [ft.Ref[ft.TextField]()]
    start_URL          = ft.Ref[ft.TextField]()
    greetings          = ft.Ref[ft.Column]()#プリントテスト用
    #page.bgcolor = ft.colors.TRANSPARENT
    
    def button_clicked(e):
        global addcounter
        stack = page.controls.pop()
        stack2 = page.controls.pop()
        domains = []
        for target_domain in target_domains:
            if target_domain.current.value in domains:
                continue
            domains.append(target_domain.current.value)
        
        print(domains)

        page.add(stack2)
        page.add(stack)
        greetings.current.controls.append(
            ft.Text(f"{start_URL.current.value}{domains}")
        )
        page.update()
        # Results = Main(start_URL,target_domains)
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
        target_domains.append(ft.Ref[ft.TextField]())
        page.controls.append(ft.TextField(ref=target_domains[len(target_domains)-1], label="対象のドメインを入力してください",width=300,height=60))
        page.add(stack2)#ボタン再配置
        page.add(stack)
        
        
    def delbutton_clicked(e):
        global addcounter
        if addcounter <= 0:#ドメイン入力欄を削除する。最低１つは残す
            return
        stack = page.controls.pop()#ボタン一時退避
        stack2 = page.controls.pop()
        page.controls.pop()
        addcounter -= 1
        page.add(stack2)#ボタン再配置
        page.add(stack)
        
    page.add(
        ft.TextField(ref=start_URL,label="探索を開始するURLを入力してください",width=550,height=80,autofocus=True,max_length=200),#autofocus=True　初期カーソル
        ft.Column(controls=[
            ft.TextField(ref=target_domains[0], label="対象のドメインを入力してください",width=300,height=60),
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