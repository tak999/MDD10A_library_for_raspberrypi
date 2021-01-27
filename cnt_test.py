import time         # time.sleepを使いたいので
import pygame       # pygameでジョイスティックを読む

# pygameの初期化とジョイスティックの初期化
pygame.init()
joy = pygame.joystick.Joystick(0)   # ジョイスティック番号はjstest-gtkで確認しておく
joy.init()

# Ctrl+cが押されるまでループ
try:
    while True:
        # Joystickの読み込み
        #   get_axisは　-1.0〜0.0〜+1.0 で変化するので100倍して±100にする
        #   プラスマイナスの方向が逆の場合は-100倍して反転させる
        a = int(joy.get_axis(2)*100)      # aは左右移動
        b = int(joy.get_axis(1)*-100)     # bは前後移動
        c = int(joy.get_axis(3)*-100)     # cは上下移動
        d = int(joy.get_axis(0)*100)      # dは旋回
        # pygame.event.pump()     # イベントの更新

        print(a, b, c, d)

except(KeyboardInterrupt, SystemExit):    # Ctrl+cが押されたら離脱
    print("SIGINTを検知")
