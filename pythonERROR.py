#! python3
# pythonERROR.py - エラー検索

import webbrowser,requests,shelve
import pyperclip as py
from bs4 import BeautifulSoup

error_shelf=shelve.open('pyERROR')
error_texts=py.paste()
print('SEARCHING ERROR>>> '+error_texts)

def y_or_n():
    print('yかnで入力してください')
    print('-'*20)

def query_string_remove(url):
    return url[:url.find('&')]

def googling(query,selector,num):
    url='https://www.google.co.jp/search?q='+query
    res=requests.get(url).text
    soup=BeautifulSoup(res,'html.parser')
    tags=soup.select(selector)
    open_num=min(num,len(tags))
    print('serching...')
    for i in range(open_num):
        url=tags[i].get('href').replace('/url?q=','')
        open_link=query_string_remove(url)
        webbrowser.open(open_link)

def mk_error_contents():
    print('エラーの内容を入力してください')
    error_contents=input(':')
    return error_contents

def mk_error_sol_list():
    sol_list=[]
    while True:
        print('解決策を追加してください(Enterで終了)')
        sol=input(':')
        sol_list.append(sol)
        if sol=='':
            del sol_list[-1]
            break
    return sol_list

def append_error_dictionary(error_contents,error_sol_list):
    error_dictionary={}
    error_dictionary['contents']=error_contents
    error_dictionary['solutions']=error_sol_list
    return error_dictionary

def display_error(error_contents,error_sol_list):
    print(' ')
    print('ERROR->:'+error_texts)
    print('CONTENTS:'+error_contents)
    print('-'*20)
    for sol in error_sol_list:
        print('・'+sol)
    print('-'*20)


if error_texts in error_shelf.keys():
    print(error_texts+'を確認しました')
    contents=error_shelf[error_texts]['contents']
    sol_list=error_shelf[error_texts]['solutions']

    if contents=='':
        print('エラーの内容が登録されていません')
        while True:
            print('Google検索しますか？(y/n)')
            yn=input(':')
            if yn=='y':
                googling(error_texts,'.r a',5)
                break
            elif yn=='n':
                break
            else:
                y_or_n()
        contents=mk_error_contents()

    if sol_list==[]:
        print('解決策が登録されていません')
        while True:
            print('Google検索しますか？(y/n)')
            yn=input(':')
            if yn=='y':
                googling(error_texts,'.r a',5)
                break
            elif yn=='n':
                break
            else:
                y_or_n()
        sol_list=mk_error_sol_list()

    display_error(contents,sol_list)
    error_shelf[error_texts]=append_error_dictionary(contents,sol_list)


else:
    while True:
        print('登録されてないエラーです\nGoogle検索しますか？(y/n)')
        yn=input(':')
        if yn=='y':
            googling(error_texts,'.r a',5)
            break
        elif yn=='n':
            break
        else:
            y_or_n()

    contents=mk_error_contents()
    sol_list=mk_error_sol_list()
    display_error(contents,sol_list)

    error_shelf[error_texts]=append_error_dictionary(contents,sol_list)

error_shelf.close()
