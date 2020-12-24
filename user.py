from instagram_private_api import Client, ClientCompatPatch
from random import randint
from time import sleep
import errors

class client:

    def __init__(self, username ,password):
        self.user = Client(username, password)
        self.uuid = self.user.generate_uuid()
        self.selfid = self.user.authenticated_user_id

    def get_user_id (self, username) :
        return self.user.username_info(username)["user"]["pk"]

    def followers(self, username):
        user_id = self.get_user_id(username)
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
       user_id = self.get_user_id(username)
       followings = self.user.user_following(user_id ,self.uuid)

       yield list(map(lambda user: user["username"] , followings["users"]))

       while followings["next_max_id"] :
           sleep(randint(2,4))
           followings = self.user.user_following(user_id ,self.uuid, max_id=followings["next_max_id"])
           yield list(map(lambda user: user["username"] , followings["users"]))

    def get_post_media_id(self, username):
        user_id = self.get_user_id(username)
        post = self.user.user_feed(user_id)
        for id in list(map(lambda media_id : media_id['pk'] , post['items'])) :
            yield id

    def get_last_post_media_id(self, username):
        user_id = self.get_user_id(username)
        post = self.user.user_feed(user_id)

        return post["items"][0]["pk"]

    def get_post_comments (self, media_id) :
        post = self.user.media_n_comments(media_id, n=200)
        try :
            comments = list(map(lambda comments : comments["text"], post))
            if comments :
                for comment in comments :
                    yield comment
            else :
                raise errors.NoComments
        except KeyError :
            raise errors.ClosedComments

    def check_user_have_comment (self, uname_needle, uname_haystack) :
        userid_needle = self.get_user_id(uname_needle)
        media_id = self.get_last_post_media_id(uname_haystack)
        post = self.user.media_n_comments(media_id, n=100)

        users = list(map(lambda comments : comments["user_id"], post))
        if userid_needle in users :
            return True

        return False

    def random_follow(self):
        pass

