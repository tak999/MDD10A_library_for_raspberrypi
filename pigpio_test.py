import time
import sys
import pigpio  # pigpioライブラリをインポートする
import pygame

pi = pigpio.pi()  # GPIOにアクセスするためのインスタンスを作成します

# 初期化
pygame.init()
pygame.joystick.init()

# ゲームパッドを列挙する（複数つなぐ場合があるので）
joysticks = [pygame.joystick.Joystick(x)
             for x in range(pygame.joystick.get_count())]

# ゲームパッドを認識しているか？
if pygame.joystick.get_count() == 0:
    print("ゲームパッドがありません。")
    sys.exit("終了")
else:
    print("ゲームパッドが" + str(len(joysticks)) + "個見つかりました。")

# ゲームパッドを初期化
print("ゲームパッドを初期化します...")
joysticks[0].init()
print("名称:%s" % (joysticks[0].get_name()))

# ゲームパッドに軸はいくつあるの？ => 6軸
n_axis = joysticks[0].get_numaxes()
print("軸の数(axis):" + str(n_axis))

# ゲームパッドにボタンはいくつあるの？ => 11個
n_button = joysticks[0].get_numbuttons()
print("ボタンの数(buttons):" + str(n_button))


class Moter:
    def __init__(self, dir_pin, pwm_pin, frequency=20000, pwm_range=1000, isSMB=True):
        self.dir_pin = dir_pin
        self.pwm_pin = pwm_pin
        self.frequency = frequency
        self.pwm_range = pwm_range

        if(isSMB is True):
            pi.set_mode(self.dir_pin, pigpio.OUTPUT)
            pi.set_mode(self.pwm_pin, pigpio.OUTPUT)

            set_PWM_frequency_return = pi.set_PWM_frequency(
                self.pwm_pin, self.frequency)
            print('Your set_PWM_frequency is configured the numerically closest frequency:',
                  set_PWM_frequency_return)

            pi.set_PWM_range(self.pwm_pin, self.pwm_range)
        else:
            pass

    def set_PWM(self, pwm_duty):
        """
        pwm_duty <= 1000(default)
        """
        self.pwm_duty = pwm_duty
        if(abs(self.pwm_duty) <= self.pwm_range):
            if(self.pwm_duty > 0):
                pi.set_PWM_dutycycle(self.pwm_pin, self.pwm_duty)
                pi.write(self.dir_pin, True)
            else:
                pi.set_PWM_dutycycle(self.pwm_pin, -1 * self.pwm_duty)
                pi.write(self.dir_pin, False)
        else:
            pass


moter1 = Moter(dir_pin=19, pwm_pin=16)
moter2 = Moter(dir_pin=13, pwm_pin=12)
moter3 = Moter(dir_pin=23, pwm_pin=22)
moter4 = Moter(dir_pin=27, pwm_pin=18)

try:
    while True:
        # ここに、Ctrl-C で止めたい処理を書く

        a = int(joysticks[0].get_axis(2)*100)      # aは左右移動
        b = int(joysticks[0].get_axis(1)*-100)     # bは前後移動
        c = int(joysticks[0].get_axis(3)*-100)     # cは上下移動
        d = int(joysticks[0].get_axis(0)*100)      # dは旋回

        print(a, b, c, d)

        moter1.set_PWM(pwm_duty=a)
        moter2.set_PWM(pwm_duty=a)
        moter3.set_PWM(pwm_duty=a)
        moter4.set_PWM(pwm_duty=a)

except KeyboardInterrupt:
    # Ctrl-C を捕まえた！
    moter1.set_PWM(pwm_duty=0)
    moter2.set_PWM(pwm_duty=0)
    moter3.set_PWM(pwm_duty=0)
    moter4.set_PWM(pwm_duty=0)
    print('interrupted! stop pigpio')
    pi.stop()
    pass
