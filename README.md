# Automation

※編集中です
色々な面倒なことを自動化するコード集です

## 1.Mailformat.py
ローカルに保存したアドレス帳から宛先を検索して、定型文をコピーします。
### 1.1.何ができるのか
アドレス帳に保存してあるshelfファイルから宛先を検索して定型文をコピーします。
![mailFlow](https://github.com/wa01su18/Automation/blob/images/addressFlow.png)
上の図のように、適宜YES/NOによって処理を分けられるようになっています。
### 1.2.Usage
ターミナルから、宛先名を引数にして実行します。
```
> Mailformat.py A部長
```
宛先による定型文をクリップボードにコピーします。
```
企画部 A部長

いつもお世話になっております。
広報部メディア担当課のMです。

よろしくお願いします。
```

### 1.3 Example
1.1の画像に習い、処理を分けた実行例です。
```
> Mailformat.py D主任
宛先がありません

新しく登録しますか？(y/n)
y
アドレスに追加します
名前を入力してください
D主任
所属を入力してください
技術部　試作第1課
登録しました
定型文をコピーしますか？(y/n)
y
定型文をコピーしました
```
```
技術部　試作第1課 D主任

いつもお世話になっております。
広報部　メディア担当課のMです。

よろしくお願いします
```
## 2.pw.py
インターネットに接続しないパスワード管理プログラムです。
### 2.1.何ができるのか
ローカルに保存しているパスワードを検索して、クリップボードにコピーします。パスワードが登録されていない場合、強力なパスワードを生成し、登録します。パスワードの登録名がわからなくなってしまったら、listと入力することによって登録名を一覧で見ることができます。
![pwFlow](https://github.com/wa01su18/Automation/blob/images/pwFlow.png)
### 2.2.Usage
ターミナルから登録名を引数に実行します。
```
> pw.py google
```
と実行すると登録してるパスワードをクリップボードにコピーします
```
wK]r4EC&W%5<vAu)H^e$ 
```

### 2.3 Example
2.1の画像に習い、処理を分けた実行例です。
```
> pw.py facebook
facebookのパスワードが登録されていません
パスワードを生成して登録しますか？(y/n)
y
パスワードを生成します
パスワードの文字数を入力してください
30
パスワードの登録とコピーが完了しました
```
```
kL@}1N;4!79xXi~Qbf{p]:Tvsm8cOg
```
引数にlistを渡して登録名を確認した実行例です。
```
> pw.py list
------アルファベット順------
amazon
facebook
google
Twitter
ふるさと納税
楽天
----------------------------
```

## 3.pythonERROR.py
Pythonのエラー管理を自動化するプログラムです。登録名にエラーの内容と解決策を紐づけます。

### 3.1.何ができるのか
まず、ローカルに保存しているshelfファイルからエラー名を検索します。
![flow1](https://github.com/wa01su18/Automation/blob/images/Flow1.png)

エラーの内容（どんなエラーなのか？）とその解決策が登録されている場合、表示します（①）。登録されてない場合（前にエラーが出た時入力するのがダルかったとか）、Google検索をするかどうか聞きます。「Google検索をする？」でYESとすると、エラー名（SyntaxErrorとか）をクエリとしてGoogle検索に投げ、さらに検索結果の上位5つのURLを新しいタブで開きます（②）。
![flow2](https://github.com/wa01su18/Automation/blob/images/Flow2.png)

### 3.2.Usage
ターミナルからエラー名をコピーしてる状態で実行します。
```
> pythonERROR.py
SEARCHING ERROR>>> SyntaxError: invalid syntax
SyntaxError: invalid syntaxを確認しました

ERROR->:SyntaxError: invalid syntax
CONTENTS:構文間違い
--------------------
・();:,'"らへんを確認
--------------------
```

### 3.3 Example
### エラーの名前は登録されているが、内容と解決策が登録されていない場合
```
> pythonERROR.py
SEARCHING ERROR>>> SyntaxError: keyword argument repeated
SyntaxError: keyword argument repeatedを確認しました
エラーの内容が登録されていません
Google検索しますか？(y/n)
:y
serching...
エラーの内容を入力してください
:引数のキーワードが重複している
解決策が登録されていません
Google検索しますか？(y/n)
:n
解決策を追加してください(Enterで終了)
:関数を呼んでいる場所をチェック
解決策を追加してください(Enterで終了)
:

ERROR->:SyntaxError: keyword argument repeated
CONTENTS:引き数のキーワードが重複している
--------------------
・関数を呼んでいる場所をチェック
--------------------
```


google検索の結果です。
![result1](https://github.com/wa01su18/Automation/blob/images/result1.png)



### エラーの名前が登録されていない場合
1.YESの場合
の「Google検索をするか？」からの流れと一緒になります。検索する場合はURLを開き、しない場合はパスします。どちらを選んでも「エラーの内容と解決策」を登録するように促します。

```
SEARCHING ERROR>>> SyntaxError: EOL while scanning string literal
登録されてないエラーです
Google検索しますか？(y/n)
:y
serching...
エラーの内容を入力してください
:文字列が閉められていない
解決策を追加してください(Enterで終了)
:’”を確認する
解決策を追加してください(Enterで終了)
:

ERROR->:SyntaxError: EOL while scanning string literal
CONTENTS:文字列が閉められていない
--------------------
・’”を確認する
--------------------
```
