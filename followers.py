from user import client as cl
from random import randint
from time import sleep
import json
from decorator import timer

@timer
def run_followers () :
    username = "funny.green.smile"
    password = "fun1382greensmile8990"

    client = cl(username, password)
    js = {}
    for users in client.followers("mhmwdhsyny767") :
        js.update(users)
    a = json.dumps(js)
    print(a)

#run_followers()
