import time
import random

import requests


if __name__ == '__main__':
    # simulate some actions being taken as if they were requests
    actions = ['view','click','close']

    while True:
        # randomly pick from the list of actions
        # and make a request to the event/ endpoint
        action = actions[random.randint(0,2)]
        answer = requests.get(f'http://127.0.0.1:5000/event/{action}')
        print(answer.status_code)
        time.sleep(1)