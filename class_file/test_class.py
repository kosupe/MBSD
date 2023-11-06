import flet as ft

def main(page:ft.Page):
    t= ft.Text(value="Hello world!")
    page.add(t)

    todo_check = ft.Checkbox(
        label="ToDo",
        value=False,
    )
    page.add(todo_check)

    def button_clicked(e):
        page.add(ft.Text("Clicled!"))

    page.add(ft.ElevatedButton(text="Click me",on_click=button_clicked))

ft.app(target=main)






"""def main(page:ft.Page):
    t = ft.Text(value="Hello,world!")
    # page.controls.append(t)
    # page.update()
    page.add(t)


ft.app(target=main)"""