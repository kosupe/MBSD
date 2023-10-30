import flet as ft

def main(page: ft.Page):
    #テキスト
    t = ft.Text(value="Hello")
    page.add(t)
    
    #チェックボックス
    todo_check = ft.Checkbox(
        label="ToDo",
        value=False,
    )
    page.add(todo_check)
    
    #ボタン
    def button_clickde(e):
        page.add(ft.Text("Clicked!"))
    #                          ボタンのテキスト      押された時に実行されるメソッド
    page.add(ft.ElevatedButton(text="Click me",      on_click=button_clickde))
    
    
ft.app(target=main)