import tkinter
import random
import pygame

# 変数定義
key = ""
フラグ = 0
賞金 = 0
プレイヤカード合計 = 0
ディーラカード合計 = 0
ディーラカード1 = 0
ディーラカード2 = 0
ディーラカード3 = 0
ディーラカード4 = 0
ディーラカード5 = 0

# pygameの初期化
pygame.init()

# 音声ファイルのアップロード
BGM = pygame.mixer.Sound("sound\BGM.mp3")
カード配布音 = pygame.mixer.Sound("sound\カード配布.mp3")

# 音声ファイルのボリューム調整
BGM.set_volume(0.1)
# BGM再生
BGM.play(-1)

# ウィンドウの作成
root = tkinter.Tk()
root.title("ブラックジャック")
root.resizable(False, False)
root.minsize(720, 400)

# キャンバスの作成
キャンバス = tkinter.Canvas(root, width=720, height=400, bg="#2f4f4f")
キャンバス.place(x=0, y=0)

# 画像のアップロード
ポーカーテーブル = tkinter.PhotoImage(file="image\ポーカーテーブル.png")
トランプ_裏 = tkinter.PhotoImage(file="image\トランプ_裏.png")
トランプ1 = tkinter.PhotoImage(file=r"image\1.png")
トランプ2 = tkinter.PhotoImage(file=r"image\2.png")
トランプ3 = tkinter.PhotoImage(file=r"image\3.png")
トランプ4 = tkinter.PhotoImage(file=r"image\4.png")
トランプ5 = tkinter.PhotoImage(file=r"image\5.png")
トランプ6 = tkinter.PhotoImage(file=r"image\6.png")
トランプ7 = tkinter.PhotoImage(file=r"image\7.png")
トランプ8 = tkinter.PhotoImage(file=r"image\8.png")
トランプ9 = tkinter.PhotoImage(file=r"image\9.png")
トランプ10 = tkinter.PhotoImage(file=r"image\10.png")
トランプ11 = tkinter.PhotoImage(file=r"image\11.png")
トランプ12 = tkinter.PhotoImage(file=r"image\12.png")
トランプ13 = tkinter.PhotoImage(file=r"image\13.png")

# リスト定義
# トランプの数字をリスト化
トランプ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 画像変数をリスト化
トランプカード = [
    トランプ_裏, トランプ1, トランプ2, トランプ3,
    トランプ4, トランプ5, トランプ6, トランプ7,
    トランプ8, トランプ9, トランプ10, トランプ11,
    トランプ12, トランプ13
]

# 関数定義
# トランプの画像を表示させる関数
def カード配布(x座標, y座標, 配布カード):
  キャンバス.delete("トランプ_裏1")
  キャンバス.delete("トランプ_裏2")
  キャンバス.delete("トランプ_裏3")
  キャンバス.create_image(x座標, y座標, image=トランプカード[配布カード])
  カード配布音.play()

# スペースキーでスタートさせる関数
def スタート(e):
  global key, 賞金, フラグ, プレイヤカード合計, ディーラカード合計, ディーラカード1, ディーラカード2
  key = e.keysym
  if key == "space" and フラグ == 0:  # スペースキーを何度も押せないようにするためにフラグで管理
    ヒット["state"] = "normal"
    スタンド["state"] = "normal"
    もう1回["state"] = "normal"

    キャンバス.delete("スタートメッセージ")
    キャンバス.delete("ディーラ")
    キャンバス.delete("プレイヤ")
    key = ""
    プレイヤカード1 = random.choice(トランプ)
    プレイヤカード2 = random.choice(トランプ)
    ディーラカード1 = random.choice(トランプ)
    ディーラカード2 = random.choice(トランプ)

    カード配布(239, 197, プレイヤカード1)
    カード配布(300, 197, プレイヤカード2)
    カード配布(239, 80, ディーラカード1)
    キャンバス.create_image(300, 80, image=トランプ_裏, tag="トランプ_裏4")

    プレイヤカード合計 = プレイヤカード1 + プレイヤカード2
    ディーラカード合計 = ディーラカード1 + ディーラカード2

    if プレイヤカード1 > 10:  # 絵札が出たら10にする処理
      プレイヤカード1 = 10
    elif プレイヤカード1 == 1:  # 1(エース)が出た時の処理
      if プレイヤカード合計 < 11:  # 1(エース)は合計が10以下のときは11にする
        プレイヤカード1 = 11
        プレイヤカード合計 = プレイヤカード1 + プレイヤカード2  # Aが2枚でたときの調整

    if プレイヤカード2 > 10:  # 絵札が出たら10にする処理
      プレイヤカード2 = 10
    elif プレイヤカード2 == 1:  # 1(エース)が出た時の処理
      if プレイヤカード合計 < 11:  # 1(エース)は合計が10以下のときは11にする
        プレイヤカード2 = 11

    if ディーラカード1 > 10:  # 絵札が出たら10にする処理
      ディーラカード1 = 10
    elif ディーラカード1 == 1:  # 1(エース)が出た時の処理
      if ディーラカード合計 < 11:  # 1(エース)は合計が10以下のときは11にする
        ディーラカード1 = 11
        ディーラカード合計 = ディーラカード1 + ディーラカード2  # Aが2枚でたときの調整

    if ディーラカード2 > 10:  # 絵札が出たら10にする処理
      ディーラカード2 = 10
    elif ディーラカード2 == 1:  # 1(エース)が出た時の処理
      if ディーラカード合計 < 11:  # 1(エース)は合計が10以下のときは11にする
        ディーラカード2 = 11

    プレイヤカード合計 = プレイヤカード1 + プレイヤカード2
    ディーラカード合計 = ディーラカード1 + ディーラカード2
    # プレイヤカード合計を表示
    キャンバス.create_text(160, 200, text=プレイヤカード合計, fill="white",
                      font=("system", 40), tag="プレイヤカード合計")
    # 獲得賞金の表示
    キャンバス.create_text(70, 20, text="獲得賞金" + str(賞金) + "円",
                      fill="white", font=("system", 20), tag="獲得賞金")

    フラグ = 1


def 判定_ヒット():
  global プレイヤカード合計, ディーラカード合計, 賞金
  if プレイヤカード合計 > 21:
    キャンバス.create_text(360, 100, text="バーストしました\nあなたの負けです",
                      fill="red", font=("system", 65), tag="バースト")
    ヒット["state"] = "disable"
    スタンド["state"] = "disable"
    キャンバス.delete("獲得賞金")
    # バーストした際、賞金を10減らす
    賞金 = 賞金 - 10
    キャンバス.create_text(70, 20, text="獲得賞金" + str(賞金) + "円",
                      fill="white", font=("system", 20), tag="獲得賞金")

def 判定_スタンド():
  global プレイヤカード合計, ディーラカード合計, スコア, 賞金
  if プレイヤカード合計 == ディーラカード合計:
    キャンバス.create_text(360, 120, text="引き分けです", fill="orange",
                      font=("system", 65), tag="バースト")
    ヒット["state"] = "disable"
    スタンド["state"] = "disable"

  elif ディーラカード合計 > 21 and プレイヤカード合計 < 22:
    キャンバス.create_text(360, 120, text="あなたの勝ちです",
                      fill="orange", font=("system", 65), tag="バースト")
    ヒット["state"] = "disable"
    スタンド["state"] = "disable"
    キャンバス.delete("獲得賞金")
    賞金 = 賞金 + 10
    キャンバス.create_text(70, 20, text="獲得賞金" + str(賞金) + "円",
                      fill="white", font=("system", 20), tag="獲得賞金")

  elif プレイヤカード合計 < 22 and ディーラカード合計 < 22:
    if 21 - プレイヤカード合計 < 21 - ディーラカード合計:
      キャンバス.create_text(360, 120, text="あなたの勝ちです",
                        fill="yellow", font=("system", 65), tag="勝ち")
      ヒット["state"] = "disable"
      スタンド["state"] = "disable"
      キャンバス.delete("獲得賞金")
      賞金 = 賞金 + 10
      キャンバス.create_text(70, 20, text="獲得賞金" + str(賞金) +
                        "円", fill="white", font=("system", 20), tag="獲得賞金")
    else:
      キャンバス.create_text(360, 120, text="ディーラの勝ちです",
                        fill="blue", font=("system", 55), tag="負け")
      ヒット["state"] = "disable"
      スタンド["state"] = "disable"
      キャンバス.delete("獲得賞金")
      賞金 = 賞金 - 10
      キャンバス.create_text(70, 20, text="獲得賞金" + str(賞金) +
                        "円", fill="white", font=("system", 20), tag="獲得賞金")

def ヒット():
  global プレイヤカード合計, ディーラカード合計, フラグ, ディーラカード3, ディーラカード4, ディーラカード5
  # ヒット1回目
  if フラグ == 1:
    プレイヤカード3 = random.choice(トランプ)
    カード配布(361, 197, プレイヤカード3)
    if プレイヤカード3 > 10:
      プレイヤカード3 = 10
    elif プレイヤカード3 == 1:
      if プレイヤカード合計 < 11:
        プレイヤカード3 = 11

    プレイヤカード合計 = プレイヤカード合計 + プレイヤカード3
    キャンバス.delete("プレイヤカード合計")
    キャンバス.create_text(160, 200, text=プレイヤカード合計, fill="white",
                      font=("system", 40), tag="プレイヤカード合計")

    # ディーラ側の処理
    if ディーラカード合計 < 18:  # ディーラは17になるまでカードをひく
      ディーラカード3 = random.choice(トランプ)
      カード配布(361, 80, 0)
      if ディーラカード3 > 10:
        ディーラカード3 = 10
      elif ディーラカード3 == 1:
        if ディーラカード合計 < 11:
          ディーラカード3 = 11

      ディーラカード合計 = ディーラカード合計 + ディーラカード3

  # ヒット2回目
  if フラグ == 2:
    プレイヤカード4 = random.choice(トランプ)
    カード配布(422, 197, プレイヤカード4)
    if プレイヤカード4 > 10:
      プレイヤカード4 = 10
    elif プレイヤカード4 == 1:
      if プレイヤカード合計 < 11:
        プレイヤカード4 = 11

    プレイヤカード合計 = プレイヤカード合計 + プレイヤカード4
    キャンバス.delete("プレイヤカード合計")
    キャンバス.create_text(160, 200, text=プレイヤカード合計, fill="white",
                      font=("system", 40), tag="プレイヤカード合計")

    # ディーラ側の処理
    if ディーラカード合計 < 18:
      ディーラカード4 = random.choice(トランプ)
      カード配布(422, 80, 0)
      if ディーラカード4 > 10:
        ディーラカード4 = 10
      elif ディーラカード4 == 1:
        if ディーラカード合計 < 11:
          ディーラカード4 = 11
      ディーラカード合計 = ディーラカード合計 + ディーラカード4

  # ヒット3回目
  if フラグ == 3:
    プレイヤカード5 = random.choice(トランプ)
    カード配布(483, 197, プレイヤカード5)
    if プレイヤカード5 > 10:
      プレイヤカード5 = 10
    elif プレイヤカード5 == 1:
      if プレイヤカード合計 < 11:
        プレイヤカード5 = 11

    プレイヤカード合計 = プレイヤカード合計 + プレイヤカード5
    キャンバス.delete("プレイヤカード合計")
    キャンバス.create_text(160, 200, text=プレイヤカード合計, fill="white",
                      font=("system", 40), tag="プレイヤカード合計")

    # ディーラ側の処理
    if ディーラカード合計 < 18:
      ディーラカード5 = random.choice(トランプ)
      カード配布(483, 80, 0)
      if ディーラカード5 > 10:
        ディーラカード5 = 10
      elif ディーラカード5 == 1:
        if ディーラカード合計 < 11:
          ディーラカード5 = 11

      ディーラカード合計 = ディーラカード合計 + ディーラカード5

  フラグ = フラグ + 1
  判定_ヒット()

def スタンド():
  global フラグ, ディーラカード2, ディーラカード3, ディーラカード4, ディーラカード5, ディーラカード合計
  キャンバス.delete("トランプ_裏4")
  カード配布(300, 80, ディーラカード2)  # カード２を表にむける
  if ディーラカード3 > 0:  # カード3を引いていれば、表にむける
    カード配布(361, 80, ディーラカード3)
  if ディーラカード4 > 0:
    カード配布(422, 80, ディーラカード4)
  if ディーラカード5 > 0:
    カード配布(483, 80, ディーラカード5)
  フラグ = 4
  キャンバス.create_text(160, 85, text=ディーラカード合計, fill="white",
                    font=("system", 40), tag="ディーラカード合計")
  判定_スタンド()

def リプレイ():
  global key, 賞金, フラグ, プレイヤカード合計, ディーラカード合計, ディーラカード1, ディーラカード2, ディーラカード3, ディーラカード4, ディーラカード5
  フラグ = 0
  ディーラカード3 = 0
  ディーラカード4 = 0
  ディーラカード5 = 0
  ディーラカード合計 = 0

  ヒット["state"] = "normal"
  スタンド["state"] = "normal"

  if フラグ == 0:
    キャンバス.delete("all")
    key = ""
    プレイヤカード1 = random.choice(トランプ)
    プレイヤカード2 = random.choice(トランプ)
    ディーラカード1 = random.choice(トランプ)
    ディーラカード2 = random.choice(トランプ)

    キャンバス.create_image(360, 200, image=ポーカーテーブル)
    カード配布(239, 197, プレイヤカード1)
    カード配布(300, 197, プレイヤカード2)
    カード配布(239, 80, ディーラカード1)
    カード配布(300, 80, 0)

    プレイヤカード合計 = プレイヤカード1 + プレイヤカード2
    ディーラカード合計 = ディーラカード1 + ディーラカード2

    if プレイヤカード1 > 10:
      プレイヤカード1 = 10
    elif プレイヤカード1 == 1:
      if プレイヤカード合計 < 11:
        プレイヤカード1 = 11
        プレイヤカード合計 = プレイヤカード1 + プレイヤカード2  # Aが2枚でたときの調整

    if プレイヤカード2 > 10:
      プレイヤカード2 = 10
    elif プレイヤカード2 == 1:
      if プレイヤカード合計 < 11:
        プレイヤカード2 = 11

    if ディーラカード1 > 10:
      ディーラカード1 = 10
    elif ディーラカード1 == 1:
      if ディーラカード合計 < 11:
        ディーラカード1 = 11
        ディーラカード合計 = ディーラカード1 + ディーラカード2  # Aが2枚でたときの調整

    if ディーラカード2 > 10:
      ディーラカード2 = 10
    elif ディーラカード2 == 1:
      if ディーラカード合計 < 11:
        ディーラカード2 = 11

    プレイヤカード合計 = プレイヤカード1 + プレイヤカード2
    ディーラカード合計 = ディーラカード1 + ディーラカード2

    キャンバス.create_text(160, 200, text=プレイヤカード合計, fill="white",
                      font=("system", 40), tag="プレイヤカード合計")
    フラグ = 1

    キャンバス.delete("獲得賞金")
    キャンバス.create_text(70, 20, text="獲得賞金" + str(賞金) + "円",
                      fill="white", font=("system", 20), tag="獲得賞金")


# キャンバスに画像を配置
キャンバス.create_image(360, 200, image=ポーカーテーブル)
キャンバス.create_image(239, 197, image=トランプ_裏, tag="トランプ_裏1")
キャンバス.create_image(300, 197, image=トランプ_裏, tag="トランプ_裏2")
キャンバス.create_image(239, 80, image=トランプ_裏, tag="トランプ_裏3")
キャンバス.create_image(300, 80, image=トランプ_裏, tag="トランプ_裏4")

# 文字の描画
キャンバス.create_text(420, 200, text="プレイヤのカード", fill="white",
                  font=("system", 20), tag="プレイヤ")
キャンバス.create_text(420, 80, text="ディーラのカード", fill="white",
                  font=("system", 20), tag="ディーラ")

# スタートの合図
キャンバス.create_text(370, 270, text="スペースキーでスタート", font=(
    "system", 34), fill="blue", tag="スタートメッセージ")

# ボタンの配置
ヒット = tkinter.Button(root, text="ヒット", font=24, bg="gold", command=ヒット)
ヒット.place(x=200, y=320)
ヒット["state"] = "disabled"
スタンド = tkinter.Button(root, text="スタンド", font=24, bg="silver", command=スタンド)
スタンド.place(x=280, y=320)
スタンド["state"] = "disabled"
もう1回 = tkinter.Button(root, text="もう1回", font=24, bg="#ac6b25", command=リプレイ)
もう1回.place(x=380, y=320)
もう1回["state"] = "disabled"

# 関数との紐づけ
root.bind("", スタート)
root.mainloop()
