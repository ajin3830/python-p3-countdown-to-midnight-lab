# your code goes here!
import time
# import ipdb

# ipdb.set_trace()

def countdown(num):
    while num:
        print(f'{num} SECOND(S)!')
        num -= 1 

    print('HAPPY NEW YEAR!')

def countdown_with_sleep(num):
    while num:
        print(f'{num} SECOND(S)!')
        num -= 1
        time.sleep(1)

    print('HAPPY NEW YEAR!')
