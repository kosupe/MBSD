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
    
    #入力フォーム
    new_task = ft.TextField(hint_text="Whats needs to be done?")
    
    
    def add_clicked(e):
        if new_task.value == "":
            return
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()
        
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))
    
    #ボタン
    def button_clickde(e):
        page.add(ft.Text("Clicked!"))
    #                          ボタンのテキスト      押された時に実行されるメソッド
    page.add(ft.ElevatedButton(text="Click me",      on_click=button_clickde))
    
    
    
ft.app(target=main)