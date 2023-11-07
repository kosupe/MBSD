from class_file.Page_class     import Page
from class_file.Scraping_class import Scraping

class Crawler():
    def crawler(start_URL:str, target_domins:list[str]):
        #変数
        Pages:list[Page] = []
        NO_searched_URLs = [start_URL]
        URL = start_URL
        
        scraping = Scraping()
        while True:
            scraping.set_URL(NO_searched_URLs.pop(0))
            urls = scraping.scraping_URL()
            
            #重複しないURLを
            [NO_searched_URLs.append(url) for url in urls 
             if url in target_domins]
            
            #未探索のURLが無くなったら終了
            if NO_searched_URLs == []:
                break
            
            
if __name__ == "__main__":
    start_URL = ""
    target_domins = ["", ""]
    Crawler.crawler(
        start_URL     = start_URL,
        target_domins = staticmethod
    )