from user import client as cl
from random import randint
from time import sleep
#ali.prkhn
username = "funny.green.smile"
password = "fun1382greensmile8990"

bot = cl(username, password)
for id in bot.get_post_media_id("ali.prkhn") :
    for comment in bot.get_post_comments(id) :
        print(comment, "\n")
    print(id , "------------------------------")
input()
