from bs4 import BeautifulSoup
import requests

class Scraping():
    def scraping_href(URL):
        
        html_text = requests.get(URL).text
        soup = BeautifulSoup(html_text, 'html.parser')
        
        element_a = soup.find("a")
        print(element_a)
        
        print(element_a.get("href"))

if __name__ == "__main__":
    URL = f'https://animestore.docomo.ne.jp/animestore/tp_pc'
    
    Scraping.scraping_href(URL=URL)