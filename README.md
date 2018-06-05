# なにができる？
* http://www.fe-siken.com/
* https://www.ap-siken.com/
<br>
上記のサイトに掲載されている問題のページにインタラクティブにアクセスできる。

# 起動方法
```
./talk [someone]
```
or
```
python talk.py [someone]
```
someoneとして指定できるのは"feam(基本情報午前), fepm(基本情報午後), apam(応用情報午前), appm(応情報午後)"。

# 使い方
```
[feam]問題を入力してください: [西暦][春期or秋期][問題番号]
```
たとえば以下のように入力する。

* 2013年春期問4
```
[feam]問題を入力してください: 2013h6
```

* 2017年秋期問16
```
[feam]問題を入力してください: 2013a16
```

# 終了方法
```
[feam]問題を入力してください: exit
```

# ヘルプ
```
./talk -h
```
or
```
python talk.py -h
```
