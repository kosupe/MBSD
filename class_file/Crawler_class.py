from class_file.Page_class     import Page
from class_file.Scraping_class import Scraping

class Crawler():
    def crawler(start_URL:str, target_domins:list[str]):
        
        searched_URLs   :list[str] = []
        NO_searched_URLs:list[str] = [start_URL]
        title           :list[str] = []
        keyword         :list[str] = []
        parameter       :dict[str] = []
        
        
        pages   :list[Page] = []
        URL     :str        = start_URL
        scraping:Scraping   = Scraping()
        
        while True:
            URL = NO_searched_URLs.pop(0)
            scraping.set_URL(URL)
            searched_URLs.append(URL)
            
            #URLを取得
            urls  = [url for url in scraping.scraping_URLs() if url in target_domins]
            
            #titleを取得
            title = scraping.scraping_title()
            
            #parameterを取得
            
            
            #keywordを取得
            keyword = scraping.scraping_keyword()
            
            #pagesに格納
            pages.append(Page(
                URL        = urls,
                title      = title,
                keyword    = keyword,
                parameters = parameter                
            ))
            
            #探し出したURLを追加
            [NO_searched_URLs.append(url) for url in urls 
             if url not in searched_URLs]
            
            #未探索のURLが無くなったら終了
            if NO_searched_URLs == []:
                return pages
        
            
if __name__ == "__main__":
    start_URL     = "https://animestore.docomo.ne.jp/animestore/tp_pc"
    target_domins = ["https://animestore.docomo.ne.jp/animestore/CF/about-cookie-page", 
                     "https://animestore.docomo.ne.jp/animestore/ci_pc?workId=26636"]
    pages = Crawler.crawler(
        start_URL     = start_URL,
        target_domins = target_domins
    )
    
    print([vars(page) for page in pages])