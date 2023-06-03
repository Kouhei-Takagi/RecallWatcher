# RecallWatcher
国土交通省の リコール情報を監視するアプリケーション
# 使い方
pythonインタプリタがある環境で必要ライブラリをインストールして起動してください。
```bash
# インストール
$ python3 -m pip install requirements.txt

# Ubuntu等Linux環境の方はtkinterをOSにインストールしてください
# PythonGUI系モジュールがOSにプリインストールされていないため
$ sudo apt-get install -y python3-tk

# 起動
$ python3 recallWatcher2.py
```
アプリを起動すれば監視を自動的に開始します。
stopボタンを押すと停止し、startボタンを押すと再開します。
# 変数
URLは、https://www.mlit.go.jp/jidosha/news.html
検索ワードは、「リコールの届出について」
監視間隔は、300秒間です。
# 注意
アプリの終了に時間がかかるかもです。。。
