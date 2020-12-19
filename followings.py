from user import client
from random import randint
from time import sleep

username = "funny.green.smile"
password = "fun1382greensmile8990"

client = client(username, password)


for usernames in client.followings("pyclass_net") :
    for username in usernames:
        print(username)
