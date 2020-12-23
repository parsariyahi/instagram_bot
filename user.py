from instagram_private_api import Client, ClientCompatPatch
from random import randint
from time import sleep
import errors

class client:

    def __init__(self, username ,password):
        self.user = Client(username, password)
        self.uuid = self.user.generate_uuid()
        self.selfid = self.user.authenticated_user_id
    
    def followers(self, username):
        user_id = self.user.username_info(username)["user"]["pk"]
        
        followers = self.user.user_followers(user_id ,self.uuid)

        #for index in range(0, len(followers["users"])) :
            #followers_list.append(followers["users"][index]["username"])
        yield list(map(lambda user: user["username"] , followers["users"]))

        while followers["next_max_id"] :
            sleep(5)
            followers = self.user.user_followers(user_id ,self.uuid, max_id=followers["next_max_id"])
            #for index in range(0, len(followers["users"])) :
                #followers_list.append(followers["users"][index]["username"])
            yield list(map(lambda user: user["username"] , followers["users"]))

    def followings(self, username):
       user_id = self.user.username_info(username)["user"]["pk"]
        
       followings = self.user.user_following(user_id ,self.uuid)
       yield list(map(lambda user: user["username"] , followings["users"]))

       while followings["next_max_id"] :
           sleep(randint(2,4))
           followings = self.user.user_following(user_id ,self.uuid, max_id=followings["next_max_id"])
           yield list(map(lambda user: user["username"] , followings["users"]))

    def get_user_comments(self):

        pass
    def get_post_media_id(self, username):
        user_id = self.user.username_info(username)["user"]["pk"]
        post = self.user.user_feed(user_id)
        for id in list(map(lambda media_id : media_id['pk'] , post['items'])) :
            yield id

    def get_post_comments (self, media_id) :
        post = self.user.media_comments(media_id)
        try :
            comments = list(map(lambda comments : comments["text"], post["comments"]))
            if comments :
                for comment in comments :
                    yield comment
            else :
                raise errors.NoComments
        except KeyError :
            raise errors.ClosedComments

    def random_follow(self):
        
        pass

