from user import client as cl
from random import randint
from time import sleep
import json
from decorator import timer

username = "funny.green.smile"
password = "fun1382greensmile8990"

client = cl(username, password)

print(client.random_follow_from_followers('ali.prkhn', 29))
