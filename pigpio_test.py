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

    def set_PWM(self, pwm_duty, pwm_dir=True):
        """
        pwm_duty <= 1000(default)
        """
        self.pwm_duty = pwm_duty
        self.pwm_dir = pwm_dir
        pi.write(self.dir_pin, self.pwm_dir)
        if(self.pwm_duty <= self.pwm_range):
            pi.set_PWM_dutycycle(self.pwm_pin, self.pwm_duty)
        else:
            pass


moter1 = Moter(dir_pin=27, pwm_pin=18)

try:
    while True:
        # ここに、Ctrl-C で止めたい処理を書く
        moter1.set_PWM(pwm_duty=900, pwm_dir=True)
except KeyboardInterrupt:
    # Ctrl-C を捕まえた！
    print('interrupted! stop pigpio')
    pi.stop()
    pass
