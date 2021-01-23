import time
import pigpio  # pigpioライブラリをインポートする

pi = pigpio.pi()  # GPIOにアクセスするためのインスタンスを作成します


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
        moter1.set_PWM(pwm_duty=-200)
        moter2.set_PWM(pwm_duty=-200)
        moter3.set_PWM(pwm_duty=-200)
        moter4.set_PWM(pwm_duty=-200)

except KeyboardInterrupt:
    # Ctrl-C を捕まえた！
    moter1.set_PWM(pwm_duty=0)
    moter2.set_PWM(pwm_duty=0)
    moter3.set_PWM(pwm_duty=0)
    moter4.set_PWM(pwm_duty=0)
    print('interrupted! stop pigpio')
    pi.stop()
    pass
