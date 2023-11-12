import flet as ft
from class_file.Page_class    import Page
from class_file.Crawler_class import Crawler

addcounter = 0
class Top(ft.View):
    def __init__(self):
        self.addcounter = 0
        start_URL          = ft.Ref[ft.TextField]()
        target_domains     = [ft.Ref[ft.TextField]()]
        controls = [
            ft.AppBar(title=ft.Text("Top Page"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.TextField(ref=start_URL,label="探索を開始するURLを入力してください",on_change=self.changed),
            ft.TextField(ref=target_domains[0], label="対象とするドメインを入力してください",width=300,height=60),
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
        self.start_URL = start_URL
        self.target_domains = target_domains
        
    def delbutton_clicked(self,e):
        if self.addcounter <= 0:#ドメイン入力欄を削除する。最低１つは残す
            return
        stack = self.controls.pop()#ボタン一時退避
        self.controls.pop()
        self.addcounter -= 1
        self.controls.append(stack)#ボタン再配置
        self.update()

    def addbutton_clicked(self,e):
        self.addcounter += 1 
        """
        追加した回数をカウント
        マイナスボタンクリックした時に減らしていく
        最低限のドメイン入力欄を確保するために０ならばマイナス処理は行わない
        """
        stack = self.controls.pop()#ボタン一時退避
        self.target_domains.append(ft.Ref[ft.TextField]())
        self.controls.append(ft.TextField(ref=self.target_domains[len(self.target_domains)-1], label="対象とするドメインを入力してください",width=300,height=60))
        self.controls.append(stack)#ボタン再配置
        self.update()

    def button_clicked(self,e):
        domains = []
        for target_domain in self.target_domains:
            if target_domain.current.value in domains:
                continue
            domains.append(target_domain.current.value)
            
        self.data = [self.start_URL.current.value, domains]
        e.page.go("/view1")
    
    def changed(self, e):
        self.data = e.control.value
        self.update()

class View1(ft.View):
    def __init__(self, pages:dict):
        page_count = int(1)#ページ数
        controls = [ft.AppBar(title=ft.Text("Top Page"), bgcolor=ft.colors.SURFACE_VARIANT),]      
        super().__init__("/view1", controls=controls)
        for view_page in pages:#全てのデータを出力するための２重ループ
            controls.append(ft.Text(f'{page_count}回目'))#何ページかを表示)
            
            for URL in view_page.URL:#URLの表示
                controls.append(ft.Text(f'URL:{URL}'))
                
            for title in view_page.title:#タイトルの表示
                controls.append(ft.Text(f'title:{title}'))

            for keyword in view_page.keyword:#キーワードの表示                
                controls.append(ft.Text(f'keyword:{keyword}'))

            for parameters in view_page.parameters:#パラメータの表示
                controls.append(ft.Text(f'{parameters}'))

            page_count += 1#カウントアップ
        
def main(page: ft.Page):
    page.title         = "ごとうぐみ"
    page.window_width  = 650
    page.window_height = 1000
    pop_flag = False

    def route_change(route):
        nonlocal pop_flag

        if pop_flag:
            pop_flag = False
        else:
            if page.route == "/":
                print('top')
                page.views.clear()
                page.update()
                page.views.append(
                    Top()
                )
            elif page.route == "/view1":
                print('view1')
                pages = Crawler.crawler(start_URL = page.views[-1].data[0], target_domins=page.views[-1].data[1])
                page.views.append(
                    View1(pages)
                )
        
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

if __name__ == '__main__':
    ft.app(target=main)