import flet as ft

def main(page:ft.Page):
    page.window_width = 650
    page.window_height = 1000
    target_domain = ft.Ref[ft.TextField]()
    start_URL = ft.Ref[ft.TextField]()
    #page.bgcolor = ft.colors.TRANSPARENT
    page.title = "ごとうぐみ"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    

    def button_clicked(e):

        # Results = Main(start_URL,target_domain)
        pass

    def addbutton_clicked(e):
        stack = page.controls.pop()
        page.update()
        page.add(ft.TextField(ref=target_domain, label="対象のドメインを入力してください",width=300,height=60))
        page.add(stack)
        
        
        
    page.add(
        ft.TextField(ref=start_URL,label="探索を開始するURLを入力してください",width=550,height=80,autofocus=True,max_length=200),#autofocus=True　初期カーソル
        ft.TextField(ref=target_domain, label="対象のドメインを入力してください",width=300,height=60),
        ft.Row([
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
        )
    )
    # page.add(ft.FloatingActionButton(icon=ft.icons.ADD, on_click=addbutton_clicked))

ft.app(target=main)