from user import client as cl
from random import randint
from time import sleep
import errors
#ali.prkhn
#programmingofficial
username = "funny.green.smile"
password = "fun1382greensmile8990"

bot = cl(username, password)
for id in bot.get_post_media_id("ali.prkhn"):
    print(id , "------------------------------")
    try :
        for comment in bot.get_post_comments(id) :
            print(comment, "\n")
    except errors.NoComments :
        print("!!!!!!!!!!!!post have no comment!!!!!!!!!!!!")
    except errors.ClosedComments :
        print("!!!!!!!!!!!!comments for this post are closed!!!!!!!!!!!!")
    break
