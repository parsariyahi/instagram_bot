from user import client as cl
from random import randint
from time import sleep

def run_followers () :
    username = "funny.green.smile"
    password = "fun1382greensmile8990"

    client = cl(username, password)

    with open("./followers.txt", "w") as file :
        for usernames in client.followers("mhmwdhsyny767") :
            for username in usernames:
                file.write(username + "-")
