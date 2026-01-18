import tkinter
import random

# --- 変数定義 ---
key = ""
flag = 0  # ゲーム開始前。スペースキーを受け付ける。
プレイヤカード合計 = 0
ディーラカード合計 = 0
ディーラカード1 = 0
ディーラカード2 = 0
ディーラカード3 = 0
ディーラカード4 = 0
ディーラカード5 = 0

# --- ウィンドウの作成 ---
root = tkinter.Tk()
root.title("ブラックジャック")
root.resizable(False, False)
root.minsize(1024, 577)

# canvasの作成
canvas = tkinter.Canvas(bg="black", width=1024, height=577)
canvas.place(x=0, y=0)

# --- 画像の読み込み ---
ポーカーテーブル = tkinter.PhotoImage(file="image\table.png")
トランプ_裏 = tkinter.PhotoImage(file="image\cards_back.png")
トランプカード = [トランプ_裏]
for i in range(1, 14):
  トランプカード.append(tkinter.PhotoImage(file=f"image/{i}.png"))

トランプ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# --- 関数定義 ---

def カード配布(x座標, y座標, 配布カード):
  # 重なっている裏面画像を消去
  canvas.delete("トランプ_裏1", "トランプ_裏2", "トランプ_裏3")
  canvas.create_image(x座標, y座標, image=トランプカード[配布カード])

def 判定_ヒット():
  global プレイヤカード合計
  if プレイヤカード合計 > 21:
    canvas.create_text(512, 180, text="バーストしました\nあなたの負けです",
                       fill="red", font=("system", 65), tag="結果")
    ヒットボタン["state"] = "disable"
    スタンドボタン["state"] = "disable"

def 判定_スタンド():
  global プレイヤカード合計, ディーラカード合計
  ヒットボタン["state"] = "disable"
  スタンドボタン["state"] = "disable"

  msg = ""
  color = "white"

  if ディーラカード合計 > 21:
    msg = "ディーラーがバースト！\nあなたの勝ちです"
    color = "yellow"
  elif プレイヤカード合計 > ディーラカード合計:
    msg = "あなたの勝ちです"
    color = "yellow"
  elif プレイヤカード合計 == ディーラカード合計:
    msg = "引き分けです"
    color = "orange"
  else:
    msg = "ディーラの勝ちです"
    color = "blue"

  canvas.create_text(512, 100, text=msg, fill=color,
                     font=("system", 60), tag="結果")

def スタート(e):
  global flag, プレイヤカード合計, ディーラカード合計, ディーラカード1, ディーラカード2
  if flag == 0:
    ヒットボタン["state"] = "normal"
    スタンドボタン["state"] = "normal"
    もう1回ボタン["state"] = "normal"

    canvas.delete("スタートメッセージ", "ディーラ文字", "プレイヤ文字", "結果", "合計数字")

    p1 = random.choice(トランプ)
    p2 = random.choice(トランプ)
    d1 = random.choice(トランプ)
    d2 = random.choice(トランプ)

    カード配布(239, 300, p1)
    カード配布(300, 300, p2)
    カード配布(239, 180, d1)
    canvas.create_image(300, 180, image=トランプ_裏, tag="トランプ_裏4")

    ディーラカード1, ディーラカード2 = d1, d2

    # スコア計算（10以上を10、Aを調整）
    def score(c): return 10 if c > 10 else c

    プレイヤカード合計 = score(p1) + score(p2)
    ディーラカード合計 = score(d1) + score(d2)

    canvas.create_text(160, 300, text=プレイヤカード合計, fill="white",
                       font=("system", 40), tag="合計数字")
    flag = 1  # ゲーム進行中。スペースキーが押されても何も起きない

def ヒット_アクション():
  global プレイヤカード合計, flag
  new_card = random.choice(トランプ)
  x = 300 + (flag * 61)
  カード配布(x, 300, new_card)

  val = 10 if new_card > 10 else new_card
  プレイヤカード合計 += val

  canvas.delete("合計数字")
  canvas.create_text(160, 300, text=プレイヤカード合計, fill="white",
                     font=("system", 40), tag="合計数字")

  flag += 1
  判定_ヒット()

def スタンド_アクション():
  global ディーラカード2, ディーラカード合計
  canvas.delete("トランプ_裏4")
  カード配布(300, 180, ディーラカード2)
  canvas.create_text(160, 180, text=ディーラカード合計, fill="white",
                     font=("system", 40), tag="合計数字")
  判定_スタンド()

def リプレイ():
  global flag
  canvas.delete("all")
  canvas.create_image(512, 283, image=ポーカーテーブル)
  canvas.create_text(512, 283, text="スペースキーでスタート", font=(
      "system", 50), fill="white", tag="スタートメッセージ")
  flag = 0
  ヒットボタン["state"] = "disabled"
  スタンドボタン["state"] = "disabled"

# --- 画面構成とボタン ---
canvas.create_image(512, 283, image=ポーカーテーブル)
canvas.create_text(512, 283, text="スペースキーでスタート", font=(
    "system", 34, "bold"), fill="white", tag="スタートメッセージ")

ヒットボタン = tkinter.Button(root, text="ヒット", font=24, bg="gold", command=ヒット_アクション)
ヒットボタン.place(x=390, y=420)
ヒットボタン["state"] = "disabled"

スタンドボタン = tkinter.Button(root, text="スタンド", font=24,
                         bg="silver", command=スタンド_アクション)
スタンドボタン.place(x=470, y=420)
スタンドボタン["state"] = "disabled"

もう1回ボタン = tkinter.Button(root, text="もう1回", font=24, bg="#ac6b25", command=リプレイ)
もう1回ボタン.place(x=570, y=420)
もう1回ボタン["state"] = "disabled"

root.bind("<space>", スタート)
root.mainloop()
