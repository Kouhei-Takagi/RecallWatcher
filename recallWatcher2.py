from bs4 import BeautifulSoup
import requests
import tkinter as tk
from threading import Thread
import time

url = "https://www.mlit.go.jp/jidosha/news.html"
search_word = "リコールの届出について"  # 検索したい単語
should_continue = True

def has_search_word(text):
    return text.find(search_word) != -1

def animate_title():
    while should_continue:
        for c in ['|', '/', '-', '\\']:
            if not should_continue:
                break
            window.title("リコール監視" + c)
            time.sleep(0.25)
        window.title("リコール監視")

def monitor():
    global should_continue
    while should_continue:
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.body(text=has_search_word)
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

        time.sleep(300)  # 300秒ごとにチェック

def start_monitor():
    global should_continue, monitor_thread, animate_thread
    should_continue = True
    monitor_thread = Thread(target=monitor)
    monitor_thread.start()
    animate_thread = Thread(target=animate_title)
    animate_thread.start()
    control_button.config(text="Stop", command=stop_monitor)

def stop_monitor():
    global should_continue
    should_continue = False
    control_button.config(text="Start", command=start_monitor)

window = tk.Tk()

label = tk.Label(window, text="ウェブサイトの更新状況を監視中...")
label.pack()

text_widget = tk.Text(window)
text_widget.pack()

control_button = tk.Button(window, text="Stop", command=stop_monitor)
control_button.pack()

# 初期化時に監視を開始
start_monitor()

window.mainloop()
