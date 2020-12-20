from user import client as cl
from random import randint
from time import sleep

username = "funny.green.smile"
password = "fun1382greensmile8990"

client = cl(username, password)
user = client.get_post_comments('ali.prkhn')
input("---")


comments =list(map(lambda post : post['pk'] , user['items']))

for comment in comments : 
    print(comment, '\n')

#media_n_comments(media_id, n=150, reverse=False, **kwargs)
