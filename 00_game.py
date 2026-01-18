import tkinter
import random

# --- 変数定義 ---
key = ""
flag = 0  # ゲーム開始前。スペースキーを受け付ける。
player_total = 0
dealer_total = 0
dealer_card_1 = 0
dealer_card_2 = 0
dealer_card_3 = 0
dealer_card_4 = 0
dealer_card_5 = 0

# --- ウィンドウの作成 ---
root = tkinter.Tk()
root.title("ブラックジャック")
root.resizable(False, False)
root.minsize(1024, 577)

# canvasの作成
canvas = tkinter.Canvas(bg="black", width=1024, height=577)
canvas.place(x=0, y=0)

# --- 画像の読み込み ---
table = tkinter.PhotoImage(file="image/table.png")
card_back = tkinter.PhotoImage(file="image/cards_back.png")
cards = [card_back]
for i in range(1, 14):
  cards.append(tkinter.PhotoImage(file=f"image/{i}.png"))

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# --- 関数定義 ---

def deal_cards(X, Y, dealt_card):
  # 重なっている裏面画像を消去
  canvas.delete("card_back_1", "card_back_2", "card_back_3")
  canvas.create_image(X, Y, image=cards[dealt_card])

def check_hit():
  global player_total
  if player_total > 21:
    canvas.create_text(512, 180, text="バーストしました\nあなたの負けです",
                       fill="red", font=("system", 65), tags="result")
    hit_btn["state"] = "disable"
    stand_btn["state"] = "disable"

def check_stand():
  global player_total, dealer_total
  hit_btn["state"] = "disable"
  stand_btn["state"] = "disable"

  msg = ""
  color = "white"

  if dealer_total > 21:
    msg = "ディーラーがバースト！\nあなたの勝ちです"
    color = "yellow"
  elif player_total > dealer_total:
    msg = "あなたの勝ちです"
    color = "yellow"
  elif player_total == dealer_total:
    msg = "引き分けです"
    color = "orange"
  else:
    msg = "ディーラの勝ちです"
    color = "blue"

  canvas.create_text(512, 100, text=msg, fill=color,
                     font=("system", 60, "bold"), tags="result")

def start_game(e):
  global flag, player_total, dealer_total, dealer_card_1, dealer_card_2
  if flag == 0:
    hit_btn["state"] = "normal"
    stand_btn["state"] = "normal"
    reset_btn["state"] = "normal"

    canvas.delete("start_game_message", "d_label",
                  "p_label", "result", "total_score")

    p1 = random.choice(card)
    p2 = random.choice(card)
    d1 = random.choice(card)
    d2 = random.choice(card)

    deal_cards(239, 300, p1)
    deal_cards(300, 300, p2)
    deal_cards(239, 180, d1)
    canvas.create_image(300, 180, image=card_back, tag="card_back_4")

    dealer_card_1, dealer_card_2 = d1, d2

    # スコア計算（10以上を10、Aを調整）
    def score(c): return 10 if c > 10 else c

    player_total = score(p1) + score(p2)
    dealer_total = score(d1) + score(d2)

    canvas.create_text(160, 300, text=player_total, fill="white",
                       font=("system", 40), tags="total_score")
    flag = 1  # ゲーム進行中。スペースキーが押されても何も起きない

def hit_action():
  global player_total, flag
  new_card = random.choice(card)
  x = 300 + (flag * 61)
  deal_cards(x, 300, new_card)

  val = 10 if new_card > 10 else new_card
  player_total += val

  canvas.delete("total_score")
  canvas.create_text(160, 300, text=player_total, fill="white",
                     font=("system", 40), tags="total_score")

  flag += 1
  check_hit()

def stand_action():
  global dealer_card_2, dealer_total
  canvas.delete("card_back_4")
  deal_cards(300, 180, dealer_card_2)
  canvas.create_text(160, 180, text=dealer_total, fill="white",
                     font=("system", 40), tags="total_score")
  check_stand()

def reset_game():
  global flag
  canvas.delete("all")
  canvas.create_image(512, 283, image=table)
  canvas.create_text(512, 283, text="スペースキーでゲームスタート", font=(
      "system", 50), fill="white", tags="start_game_message")
  flag = 0
  hit_btn["state"] = "disabled"
  stand_btn["state"] = "disabled"

# --- 画面構成とボタン ---
canvas.create_image(512, 283, image=table)
canvas.create_text(512, 283, text="スペースキーでゲームスタート", font=(
    "system", 34, "bold"), fill="white", tags="start_game_message")

hit_btn = tkinter.Button(root, text="ヒット", font=(
    "system", 24), bg="gold", command=hit_action)
hit_btn.place(x=300, y=420)
hit_btn["state"] = "disabled"

stand_btn = tkinter.Button(root, text="スタンド", font=(
    "system", 24), bg="silver", command=stand_action)
stand_btn.place(x=450, y=420)
stand_btn["state"] = "disabled"

reset_btn = tkinter.Button(root, text="もう1回", font=(
    "system", 24), bg="#ac6b25", command=reset_game)
reset_btn.place(x=660, y=420)
reset_btn["state"] = "disabled"

root.bind("<space>", start_game)
root.mainloop()
