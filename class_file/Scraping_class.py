from bs4 import BeautifulSoup
import urllib.parse
import requests
import re


class Scraping():
    def __init__(self) -> None:
        self.URL :str
    
    def check_valid_URL(URL):
        try:
            html_text = requests.get(URL).text
            return True
        except:
            return False
        
    
    def set_URL(self, URL):
        self.URL = URL
   
    def https_adder(self, href:str):
        path = re.sub('^/', '', href)
        return urllib.parse.urljoin(self.URL, path)
   
    
    def scraping_URLs(self):
        html_text = requests.get(self.URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        element_a = soup.find_all("a")
        hrefs     = [a_tag.get("href") for a_tag in element_a]
        
        urls  = [self.https_adder(href) for href in hrefs if href not in [None, 'javascript:void(0);']]
        return urls


    def scraping_title(self):
        html_text = requests.get(self.URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        element_title = soup.find_all("title")
        
        return [title.text for title in element_title]

    
    def scraping_keyword(self):
        html_text = requests.get(self.URL).text
        
        return re.findall(r'(?<=MBSD\{)[^\}]+(?=\})', html_text)
    
if __name__ == "__main__":
    URL:str = 'https://animestore.docomo.ne.jp/animestore/tp_pc'
    
    scraping = Scraping()
    scraping.set_URL(URL)
    
    URL ="a"
    Scraping.check_valid_URL(URL)
    
    