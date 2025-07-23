import RPi.GPIO as GPIO
import time
import csv

f = open("box.csv", "r")
reader = csv.reader(f)
f.seek(0)

f_w = open("write.txt", "w")

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

char = ""

try:
    while True:
        if GPIO.input(17) == GPIO.HIGH:
            time.sleep(0.2)
            char = "1"
        elif GPIO.input(27) == GPIO.HIGH:
            time.sleep(0.2)
            char = "2"
        elif GPIO.input(22) == GPIO.HIGH:
            time.sleep(0.2)
            char = "3"
        elif GPIO.input(10) == GPIO.HIGH:
            time.sleep(0.2)
            char = "4"
        elif GPIO.input(9) == GPIO.HIGH:
            time.sleep(0.2)
            char = "5"
        elif GPIO.input(11) == GPIO.HIGH:
            time.sleep(0.2)
            char = "6"
        elif GPIO.input(5) == GPIO.HIGH:
            time.sleep(0.2)
            char = "7"
        
        if char != "":
            print(f"Pressed: {char}")
            f_w.write(char + "\n")
            f_w.flush()
            char = ""

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()
    f.close()
    f_w.close()
