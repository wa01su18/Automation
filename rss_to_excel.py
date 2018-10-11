#複数のWEBサイトから記事タイトルとURLをスクレイピングしてEXCELに出力します
import pandas as pd
from web_scraping import WEB_scraping

#インスタンスの定義
item1=WEB_scraping("gizmood","https://www.gizmodo.jp/articles/","h3","p-archive-cardTitle")
item2=WEB_scraping("gigazine","http://gigazine.net/","h2",None)
item3=WEB_scraping("TechCrunch","https://jp.techcrunch.com/","h2","post-title")
item4=WEB_scraping("zdnet","https://japan.zdnet.com/archives/","h3",None)
item5=WEB_scraping("hatenaIT","http://b.hatena.ne.jp/hotentry/it","h3","entrylist-contents-title")

items=[item1,item2,item3,item4,item5]

#excelシート作成
columns=["タイトル","Url"] #列の作成
excel_writer = pd.ExcelWriter('result.xlsx')

#itemのループ
for item in items:
    df=pd.DataFrame(columns=columns)
    soup=item.response()
    contents=soup.find_all(item.tag,class_=item.detail)
    #contentのループ
    for content in contents:
        title=content.a.string
        #gizmoodとzdnetだけhttps～がget(href)で返ってこないから足す
        if item.name=="gizmood":
            link="https://www.gizmodo.jp"+content.a.get("href")
        elif item.name=="zdnet":
            link="https://japan.zdnet.com"+content.a.get("href")
        else:
            link=content.a.get("href")

        #df作成
        se=pd.Series([title,link],columns)
        print(se)
        df=df.append(se,columns)
    df.to_excel(excel_writer,item.name)

excel_writer.save()
