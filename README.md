GeoDjangoではじめる地理空間情報
=====
WebGISアプリ開発入門として、PythonのWebフレームワークであるDjangoとDjangoのGeoDjangoモジュールを使ったWebGISアプリを0から作成していきます。

# 対象読者

このドキュメントは、次の方にお読みいただくことを前提に説明しています。<br>
民間企業社員, 地方自治体職員, 中学高校の教職員、高校生、大学生でプログラミングに興味がある方にお勧めです。

* 地理空間情報のプログラミングは初めてという方
* Pythonの文法はある程度理解している方
* HTML, CSS, JacaScriptはある程度理解している方
* Djangoを使うのは初めてという方
* Webアプリの開発の初級者の方

# ライセンス

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />この資料は <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">クリエイティブ・コモンズ 表示 - 継承 4.0 国際 ライセンス</a>の下に提供されています。
* コモンズ証 - https://creativecommons.org/licenses/by-sa/4.0/deed.ja
* リーガルコード - https://creativecommons.org/licenses/by-sa/4.0/legalcode.ja

## 参考にしたサイト
この資料は下記のサイトを参考に作成をしています。<br>
資料の一部に参考、引用、転載をしています。

* [Django documentation](https://docs.djangoproject.com/en/2.0/)
* [Django ドキュメント](https://docs.djangoproject.com/ja/2.0/)
* [Django Girls Tutorial 英語版](https://tutorial.djangogirls.org/en/)
* [Django Girls Tutorial 日本語版](https://djangogirlsjapan.gitbooks.io/workshop_tutorialjp/content/)
* [GeoDjango Tutorial](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/tutorial/)
* [PostGISとGeoDjangoを使ってLeafletでGeoJSON Tile Layerを表示してみる(1) – インストール編 –](https://blog.bitmeister.jp/?p=3467)
* [モダンDjango入門](https://codezine.jp/article/corner/723)
* [Django Rest Framework GISで誰でも簡単RESTful Geo API](http://monomoti.hatenablog.jp/entry/2015/12/15/000000)

# 免責

* 内容に関しては万全を期しておりますが、その内容の正確性、安全性、合法性、適切性、合目的性を保証するものではありません。
* 当該情報に基づいて、利用者が被る一切の損害について、何等責任を負いません。
* 他のウェブサイトやリソースへのリンクを記述している場合がありまが、リンク先の内容や真偽等につきまして一切責任を負いかねます。
* 予告なしに内容の変更または廃止する場合があります

# 使用データ
国土数値情報　ダウンロードサービス - <http://nlftp.mlit.go.jp/ksj/index.html>の北海道のデータを使用します
* 国土交通省国土政策局「国土数値情報（行政区域データ）」 (N03-170101_01_GML)
    - <http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_3.html>
* 国土交通省国土政策局「国土数値情報（小学校区データ）」 (A27-16_01_GML)
    - <http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A27-v2_1.html>
* 国土交通省国土政策局「国土数値情報（公共施設データ）」 (P02-06_01_GML)
    - <http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P02-v4_0.html>
* 国土交通省国土政策局「国土数値情報（バス停留所データ）」 (P11-10_01_GML)
    - <http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P11.html>
