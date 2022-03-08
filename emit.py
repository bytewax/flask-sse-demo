import time
import random

import requests


if __name__ == '__main__':
    actions = ['view','click','close']

    while True:
        action = actions[random.randint(0,2)]
        answer = requests.get(f'http://127.0.0.1:5000/event/{action}')
        print(answer.status_code)
        time.sleep(1)