import flet as ft
addcounter = 0
class Top(ft.View):
    def __init__(self):
        data ={}
        start_URL          = ft.Ref[ft.TextField]()
        target_domains     = [ft.Ref[ft.TextField]()]
        controls = [
            ft.AppBar(title=ft.Text("Top Page"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.TextField(ref=start_URL,label="URL",on_change=self.changed),
            ft.TextField(ref=target_domains[0], label="ドメイン"),
            ft.Row([
            ft.ElevatedButton(
            "-",on_click=self.delbutton_clicked),
            ft.ElevatedButton(
            "+",on_click=self.addbutton_clicked),
            ft.ElevatedButton("探索開始", on_click=self.button_clicked),
        ],alignment=ft.MainAxisAlignment.START,
        ),
        ]
        super().__init__("/", controls=controls)
        self.data = start_URL
        self.start_URL = start_URL
        self.target_domains = target_domains
        """
        ↑よくわからん事なってる
        多分消しても問題ない
        """
        
    def delbutton_clicked(self,e):
        global addcounter
        if addcounter <= 0:#ドメイン入力欄を削除する。最低１つは残す
            return
        stack = self.controls.pop()#ボタン一時退避
        self.controls.pop()
        addcounter -= 1
        self.controls.append(stack)#ボタン再配置
        self.update()

    def addbutton_clicked(self,e):
        global addcounter
        addcounter += 1 
        """
        追加した回数をカウント
        マイナスボタンクリックした時に減らしていく
        最低限のドメイン入力欄を確保するために０ならばマイナス処理は行わない
        """
        stack = self.controls.pop()#ボタン一時退避
        self.target_domains.append(ft.Ref[ft.TextField]())
        self.controls.append(ft.TextField(ref=self.target_domains[len(self.target_domains)-1], label="対象のドメインを入力してください",width=300,height=60))
        self.controls.append(stack)#ボタン再配置
        self.update()

    def button_clicked(self,e):
        global addcounter
        domains = []
        for target_domain in self.target_domains:
            if target_domain.current.value in domains:
                continue
            domains.append(target_domain.current.value)
        self.data = {self.start_URL.current.value:domains}#値１つしか渡せないから辞書にぶち込んだ
        e.page.go("/view1")
    
    def changed(self, e):
        self.data = e.control.value
        self.update()
    """
    ↑多分使ってない
    """


class View1(ft.View):
    def __init__(self,data:dict):
        controls = [
            ft.AppBar(title=ft.Text("Top Page"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text(f'探索URL: {data}'),
            
            # ft.Text(f'探索対象ドメイン: {_target_domains}'),
        ]
        """
        URLとドメインの値を保持したままページ遷移する方法が分からないです
        辞書でまとめて持ってきたら取り出せなくなっちゃったwww
        """
        super().__init__("/view1", controls=controls)
        



def main(page: ft.Page):
    page.title         = "ごとうぐみ"
    page.window_width  = 650
    page.window_height = 1000

    pop_flag = False

    def route_change(e):
        nonlocal pop_flag

        if pop_flag:
            pop_flag = False
        else:
            if page.route == "/":
                page.views.clear()
                page.views.append(
                    Top()
                )
            elif page.route == "/view1":
                page.views.append(
                    View1(page.views[-1].data)
                )
        
    def view_pop(e):
        nonlocal pop_flag
        pop_flag = True
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.views.clear()
    page.go("/")


if __name__ == '__main__':
    ft.app(target=main)