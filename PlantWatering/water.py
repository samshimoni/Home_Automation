# External module imp
import RPi.GPIO as GPIO
import datetime
import time

init = False
GPIO.setmode(GPIO.BOARD)    # Broadcom pin-numbering scheme


def get_last_watered():
    try:
        f = open("last_watered.txt", "r")
        return f.readline()
    except FileNotFoundError:
        return "NEVER!"


def get_status(pin=8):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)


def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)


def auto_water(delay=5, pump_pin=7, water_sensor_pin=8):
    consecutive_water_count = 0
    init_output(pump_pin)
    print("Here we go! Press CTRL+C to exit")
    try:
        wet = get_status(pin = water_sensor_pin) == 0

        while wet is False and consecutive_water_count < 10:
            time.sleep(delay) 
            pump_on(pump_pin, 1)
            consecutive_water_count += 1
            wet = get_status(pin=water_sensor_pin) == 0

        GPIO.cleanup()
        print('Plant is no Longer dry... satisfied after {} times'.format(consecutive_water_count))

    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPI


def pump_on(pump_pin=7, delay=1):
    init_output(pump_pin)
    f = open("last_watered.txt", "w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH)

#auto_water()
