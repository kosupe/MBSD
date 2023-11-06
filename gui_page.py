import flet as ft

def main(page:ft.Page):
    target_domain = ft.Ref[ft.TextField]()
    start_URL = ft.Ref[ft.TextField]()


    def button_clicked(e):

        # Results = Main(start_URL,target_domain)
        pass

    page.add(
        ft.TextField(ref=target_domain, label="対象のドメインを入力してください", autofocus=True),
        ft.TextField(ref=start_URL, label="探索を開始するURLを入力してください"),
        ft.ElevatedButton("探索開始", on_click=button_clicked),
    )
    
ft.app(target=main)