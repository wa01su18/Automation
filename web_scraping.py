import requests
from bs4 import BeautifulSoup
import pandas as pd

#タイトル、URL、拾うタグ、classを変数にする
class WEB_scraping:
    def __init__(self,name,url,tag,detail):
        self.name=name
        self.url=url
        self.tag=tag
        self.detail=detail
#webページのHTMLをかえす
    def response(self):
        html = requests.get(self.url).text
        return BeautifulSoup(html, 'html.parser')

    def find(self,html):
        return html.find_all(self.tag,class_=self.detail)
