from os import error
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

            pi.set_PWM_dutycycle(self.pwm_pin, self.pwm_range)
        else:
            pass

    def set_PWM(self, pwm_duty, pwm_dir=True):
        """
        docstring
        """
        self.pwm_duty = pwm_duty
        self.pwm_dir = pwm_dir
        if(self.pwm_duty <= self.pwm_range):
            pi.set_PWM_dutycycle(dir_1, 2000)
        else:
            pass


pwm_1 = 18
dir_1 = 27
'''pwm_2 = 23
dir_2 = 22
pwm_3 = 12
dir_3 = 13
pwm_4 = 16
dir_4 = 19'''

# GPIOのモードを設定します他にINPUTとかある。ex:18はGPIO18の18番です。
pi.set_mode(pwm_1, pigpio.OUTPUT)
pi.set_mode(dir_1, pigpio.OUTPUT)
'''pi.set_mode(pwm_2, pigpio.OUTPUT)
pi.set_mode(dir_2, pigpio.OUTPUT)
pi.set_mode(pwm_3, pigpio.OUTPUT)
pi.set_mode(dir_3, pigpio.OUTPUT)
pi.set_mode(pwm_4, pigpio.OUTPUT)
pi.set_mode(dir_4, pigpio.OUTPUT)'''

# GPIO18: 2Hz、duty比0.5
pi.write(pwm_1, 0)
set_PWM_frequency_return = pi.set_PWM_frequency(dir_1, 20000)
if(set_PWM_frequency_return == 'OK'):
    print('Your set_PWM_frequency is configured accurately')
else:
    print('Your set_PWM_frequency is configured the numerically closest frequency, sorry man!',
          set_PWM_frequency_return)
pi.set_PWM_range(dir_1, 2000)
pi.set_PWM_dutycycle(dir_1, 2000)
# pi.hardware_PWM(pwm_1, 20000, 100000)
# GPIO19: 8Hz、duty比0.1(ppm(百万分率)で数値を記入する)
'''pi.hardware_PWM(pwm_2, 20000, 500000)
'''
time.sleep(10)

pi.stop()
