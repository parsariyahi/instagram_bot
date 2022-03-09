from user import client as cl
from random import randint
from time import sleep

def run_following ():
    username = "your username"
    password = "your pass"

    client = cl(username, password)

    with open("./followings.txt", "w") as file :
        for usernames in client.followings("mhmwdhsyny767") :
            for username in usernames:
                file.write(username + "-")
