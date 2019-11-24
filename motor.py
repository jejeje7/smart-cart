import RPi.GPIO as GPIO
import time
import os







md4 = 26
ms4  = 19
md3  = 13
ms3 = 6

md2 = 21
ms2 = 20
md1 = 16
ms1 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(md1, GPIO.OUT)
GPIO.setup(ms1, GPIO.OUT)
GPIO.setup(md2, GPIO.OUT)
GPIO.setup(ms2, GPIO.OUT)
GPIO.setup(md3, GPIO.OUT)
GPIO.setup(ms3, GPIO.OUT)
GPIO.setup(md4, GPIO.OUT)
GPIO.setup(ms4, GPIO.OUT)

def back():
    GPIO.output(md1, 0)
    GPIO.output(ms1, 0)

    GPIO.output(md2, 0)
    GPIO.output(ms2, 1)

    GPIO.output(md3, 0)
    GPIO.output(ms3, 0)

    GPIO.output(md4, 1)
    GPIO.output(ms4, 0)
    

def go():
    GPIO.output(md1, 0)
    GPIO.output(ms1, 0)

    GPIO.output(md2, 1)
    GPIO.output(ms2, 0)

    GPIO.output(md3, 0)
    GPIO.output(ms3, 0)

    GPIO.output(md4, 0)
    GPIO.output(ms4, 1)

def right():
    GPIO.output(md2, 0)
    GPIO.output(ms2, 0)

    GPIO.output(md1, 1)
    GPIO.output(ms1, 0)

    GPIO.output(md4, 0)
    GPIO.output(ms4, 0)

    GPIO.output(md3, 0)
    GPIO.output(ms3, 1)

def left():
    GPIO.output(md2, 0)
    GPIO.output(ms2, 0)

    GPIO.output(md1, 0)
    GPIO.output(ms1, 1)

    GPIO.output(md4, 0)
    GPIO.output(ms4, 0)

    GPIO.output(md3, 1)
    GPIO.output(ms3, 0)

def stop():
    GPIO.output(md2, 0)
    GPIO.output(ms2, 0)

    GPIO.output(md1, 0)
    GPIO.output(ms1, 0)

    GPIO.output(md4, 0)
    GPIO.output(ms4, 0)

    GPIO.output(md3, 0)
    GPIO.output(ms3, 0)


if __name__ == '__main__':
    go()
    time.sleep(1)
    back()
    time.sleep(1)


    left()
    time.sleep(1)
    right()
    time.sleep(1)
    stop()

    '''
    GPIO.output(md1, 1)
    GPIO.output(ms1, 0)
    time.sleep(1)
    GPIO.output(md1, 0)
    GPIO.output(ms1, 0)
    '''
