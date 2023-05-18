from bs4 import BeautifulSoup
import requests
import tkinter as tk
from threading import Thread
import time

url = "https://www.mlit.go.jp/jidosha/news.html"
search_word = "リコールの届出について"  # 検索したい単語

def has_search_word(text):
    return text.find(search_word) != -1

def monitor():
    while True:
        response = requests.get(url)
        response.encoding = 'utf-8'
        print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.body(text=has_search_word)
        print(results)
        text_widget.delete('1.0', tk.END)  # 既存のテキストをクリア

        for result in results:
            pos = 0
            while True:
                pos = result.find(search_word, pos)
                if pos == -1:
                    break
                start = pos + len(search_word)
                following_text = result[start:start+30]
                text_widget.insert(tk.END, f"{search_word}:{following_text}\n")
                pos = start

        time.sleep(900)  # 900秒ごとにチェック

# tkinterのウィンドウを作成
window = tk.Tk()
window.title("https://www.mlit.go.jp/jidosha/news.html 「リコールの届出について」　900秒間隔で監視")
label = tk.Label(window, text="ウェブサイトの更新状況を監視中...")
label.pack()
text_widget = tk.Text(window)
text_widget.pack()

# 別スレッドでウェブサイトの監視を開始
t = Thread(target=monitor)
t.start()

# GUIを表示
window.mainloop()
