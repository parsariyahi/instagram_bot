from user import client as cl
from random import randint
from time import sleep
import errors


username = "your username"
password = "your pass"

bot = cl(username, password)

def get_comments() :
    for id in bot.get_post_media_id("ali.prkhn"):
        print(id , "------------------------------")
        try :
            for comment in bot.get_post_comments(id) :
                print(comment, "\n")
        except errors.NoComments :
            print("!!!!!!!!!!!!post has no comment!!!!!!!!!!!!")
        except errors.ClosedComments :
            print("!!!!!!!!!!!!comments for this post are closed!!!!!!!!!!!!")
        break
