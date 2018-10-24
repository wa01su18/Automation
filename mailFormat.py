#! python3
#MailTexts.py - メールの定型文管理プログラム
import sys,shelve
import pyperclip as py

address=shelve.open('address')
mailto=sys.argv[1]

format_list=[' ',
            'いつもお世話になっております。',
            '広報部メディア担当課のMです。',
            ' ',
            'よろしくお願いします']
format='\r\n'.join(format_list)

def addresser(name):
    return address[name]+' '+name

def copy_total_format(name):
    total_format=addresser(name)+'\r\n'+format
    py.copy(total_format)
    print('定型文をコピーしました')

def save_address():
    print('名前を入力してください')
    name=input()
    print('所属を入力してください（○○部　××課）')
    dev=input()
    address[name]=dev
    return name

if len(sys.argv)<2:
    print("使用方法：python MailTexts.py '宛先'")
    print('定型文をコピーします')

if mailto in address:
    copy_total_format(mailto)
else:
    print('宛先がありません\n \n新しく登録しますか？(y/n)')
    save_yn=input()
    if save_yn=='y':
        print('アドレスに追加します')
        name=save_address()
        print('登録しました')
        print('定型文をコピーしますか？(y/n)')
        copy_yn=input()
        if copy_yn=='y':
            copy_total_format(name)
        else:
            print('処理を終了しました')
    else:
        print('定型文をコピーしますか？(y/n)')
        copy_yn=input()
        if copy_yn=='y':
            name=save_address()
            copy_total_format(name)
            address.pop(name)
        else:
            print('処理を終了しました')
