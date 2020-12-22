from user import client as cl
from random import randint
from time import sleep
#ali.prkhn
username = "funny.green.smile"
password = "fun1382greensmile8990"

client = cl(username, password)

for media_id in client.get_post_media_id('ali.prkhn') :
    print(media_id)
#media_n_comments(media_id, n=150, reverse=False, **kwargs)
