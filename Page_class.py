import pprint

class Page():
    def __init__(self, URL, parameters, title, keyword) -> None:
        self.URL       :list[str] = URL
        self.title     :list[str] = title
        self.keyword   :list[str] = keyword
        self.parameters:dict      = parameters


pages = [Page(URL        = ["https://www.youtube.com/watch?v=B5tSZr_QqXw&t=1715s","https://www.youtube.com/watch?v=6SLMB7BPG9E&t=1160s"],
              title      = ["【GitHub入門】初心者向け！GitHubでチーム開発するための基本操作を解説！"],
              keyword    = ["xxx", "xxx", "xxx"],
              parameters = {
                                "id"  : 1001,
                                "key" : "value"
                            }
              ),
         Page(URL        = ["https://www.youtube.com/watch?v=6SLMB7BPG9E&t=1160s"],
              title      = ["【Docker入門】初心者向け！Dockerの基本を学んでコンテナ型の仮想環境を作ろう！"],
              keyword    = ["xxx", "xxx"],
              parameters = {
                                "id"  : 2023,
                                "key" : "value"
                            }
              )
         ]

pprint.pprint([vars(page) for page in pages])
