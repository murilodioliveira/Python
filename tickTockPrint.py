import sys
import time
def tick_tock(seconds):
    print('Tick')
    time.sleep(1)
    for i in range(seconds-1):
        if i%2 != 0:
            print('Tick')
            time.sleep(1)
        else:
            print('Tock')
            time.sleep(1) 

tick_tock(3)