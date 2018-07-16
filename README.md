Welcome to questalker
===
なにができる？
---
* http://www.fe-siken.com/
* https://www.ap-siken.com/

上記のサイトに掲載されている問題のページにインタラクティブにアクセスできる。

起動方法
---
```
./talk [someone]
```
or
```
python3 talk.py [someone]
```

以下を[someone]として指定できる。

* feam(基本情報午前)
* fepm(基本情報午後)
* apam(応用情報午前)
* appm(応用情報午後)

使い方
---
```
[feam]問題を入力してください: [西暦][春期or秋期][問題番号]
```
たとえば以下のように入力する。

* 2013年春期問6
```
[feam]問題を入力してください: 2013h6
```

* 2017年秋期問16
```
[feam]問題を入力してください: 2013a16
```

終了方法
---
```
[feam]問題を入力してください: exit
```

ヘルプ
---
```
./talk -h
```
or
```
python3 talk.py -h
```
