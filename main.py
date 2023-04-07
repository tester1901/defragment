# Defragment is still in still in its alpha stages
# its not a going to work %100
# expect to have to re-arange the payload variable

import time
import requests

from threading import Thread
from random import choice as ran
from names import list_of_names as lof

def main():
    f_choice = ran(lof.fname)
    l_choice = ran(lof.lname)

    url = input("URL: ")
    # spam = input("how manys requests? >>> ")
    payload = {
        'card': 79927398713,
        'first name': f_choice,
        'last name': l_choice,
        'billing address': 'hell, michigan',
        'zip code': 48169

    }
    act = ['y', 'n']
    act_choice = None

    while act_choice not in act:
        act_choice = input('all info is correct? y/n >>> ').lower()
    
    if act_choice == 'y':
        for i in range(4000):
            r = requests.get(url, params=payload)
            if r.status_code == 200:
                continue
                print("success!")
            else:
                print('response code [' + r.status_code +']')
                break

    

def start():
    print("\n")
    print("#          _       __                                      _   ")
    print("#         | |     / _|                                    | |  ")
    print("#       __| | ___| |_ _ __ __ _  __ _ _ __ ___   ___ _ __ | |_ ")
    print("#      / _` |/ _ \  _| '__/ _` |/ _` | '_ ` _ \ / _ \ '_ \| __|")
    print("#     | (_| |  __/ | | | | (_| | (_| | | | | | |  __/ | | | |_ ")
    print("#      \__,_|\___|_| |_|  \__,_|\__, |_| |_| |_|\___|_| |_|\__|")
    print("#                               __/ |                         ")
    print("#                              |___/                          ")
    print('\n')
    
    time.sleep(2)
    
    print("Only use if you know what you are doing")
    print("you assume all responsiblity when using this program")

    act = ['y', 'n']
    act_choice = None

    while act_choice not in act:
        act_choice = input('continue? y/n >>> ').lower()

    if act_choice == 'y':   
        print("starting")
        t1 = Thread(target=main)
        t1.start()
        t1.join()
    
start()