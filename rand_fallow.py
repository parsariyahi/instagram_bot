from user import client as cl
from random import randint
from time import sleep
import json
from decorator import timer

username = "parsarh82"
password = "parsa1981"

client = cl(username, password)

print(client.random_follow_from_followers('ali.prkhn', 29))
