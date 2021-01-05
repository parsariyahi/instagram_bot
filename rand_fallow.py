from user import client as cl
from random import randint
from time import sleep
from decorator import timer
import defs as df
username = "parsarh82"
password = "parsa1981"

client = cl(username, password)

print(client.random_follow_n_from_followers('ali.prkhn', n=10))
