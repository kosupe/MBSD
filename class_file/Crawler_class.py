from class_file.Page_class     import Page
from class_file.Scraping_class import Scraping

class Crawler():
    
    def domain_include_check(domains:list, URL):
        for domain in domains:
            if URL[:8+len(domain)] == "https://"+domain:
                return True
            
            if URL[:7+len(domain)] == "http://"+domain:
                return True
        
        return False
    
    
    def crawler(start_URL:str, target_domins:list[str]):
        
        searched_URLs   :list[str]  = []
        NO_searched_URLs:list[str]  = [start_URL]
        
        title    :list[str]  = []
        keyword  :list[str]  = []
        parameter:dict[str]  = []
        pages    :list[Page] = []
        
        URL      :str        = start_URL
        scraping :Scraping   = Scraping()
        
        
        
        while True:
            URL = NO_searched_URLs.pop(0)
            print(f"URL:{URL}")
            scraping.set_URL(URL)
            searched_URLs.append(URL)
            
            #URLを取得
            urls  = [url for url in scraping.scraping_URLs() 
                     if Crawler.domain_include_check(domains=target_domins, URL=url) and url not in searched_URLs] 
            
            #titleを取得
            title = scraping.scraping_title()
            
            #parameterを取得
            parameter = scraping.scraping_parameters()
            
            #keywordを取得
            keyword = scraping.scraping_keyword()
            
            #pagesに格納
            pages.append(Page(
                my_URL     = URL,
                URL        = urls,
                title      = title,
                keyword    = keyword,
                parameters = parameter                
            ))
            
            print(searched_URLs)
            #探し出したURLを追加
            [NO_searched_URLs.append(url) for url in urls 
             if url not in searched_URLs and url not in NO_searched_URLs]
            
            print(searched_URLs)
                
            
            
            #未探索のURLが無くなったら終了
            if NO_searched_URLs == []:
                return pages
            
            
            
    
            
if __name__ == "__main__":
    start_URL     = "https://animestore.docomo.ne.jp/animestore/tp_pc"
    target_domins = ["animestore.docomo.ne.jp", 
                     "https://animestore.docomo.ne.jp/animestore/ci_pc?workId=26636"]
    target_domins = []
    pages = Crawler.crawler(
        start_URL     = start_URL,
        target_domins = target_domins
    )
    
    print([vars(page) for page in pages])