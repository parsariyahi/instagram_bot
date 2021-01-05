from instagram_private_api import Client, ClientCompatPatch
from random import randint, choice
from time import sleep
import errors
import json
import decorator
import defs as df

class client:
    def __init__(self, username ,password):
        self.user = Client(username, password, timeout=30)
        self.uuid = self.user.generate_uuid()
        self.selfid = self.user.authenticated_user_id

    def get_user_id (self, username) :
        return self.user.username_info(username)["user"]["pk"]

    def followers(self, username) -> dict:
        user_id = self.get_user_id(username)
        followers = self.user.user_followers(user_id ,self.uuid)

        yield dict(map(lambda user: [user['pk'] , user["username"]] , followers["users"]))

        while followers["next_max_id"] :
            sleep(5)
            followers = self.user.user_followers(user_id ,self.uuid, max_id=followers["next_max_id"])
            yield dict(map(lambda user: [user['pk'] , user["username"]] , followers["users"]))

    def followings(self, username):
       user_id = self.get_user_id(username)
       followings = self.user.user_following(user_id ,self.uuid)

       yield dict(map(lambda user: [user['pk'] , user["username"]] , followings["users"]))

       while followings["next_max_id"] :
           sleep(randint(2,4))
           followings = self.user.user_following(user_id ,self.uuid, max_id=followings["next_max_id"])
           yield dict(map(lambda user: [user['pk'] , user["username"]] , followings["users"]))

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

        return True if userid_needle in users else False

    def random_follow_n_from_followers(self, username, n=25):
        dict_users = {}
        for users in self.followers(username) :
            dict_users.update(users)
        for _ in range(n + 1) :
            to_follow = dict_users.popitem()
            sleep(randint(2, 5))
            if self.user.friendships_create(to_follow[0]) :
                print(to_follow[1])

    def random_follow_n_from_followings(self, username, n=25):
        dict_users = {}
        final_dict = {}
        for users in self.followings(username) :
            dict_users.update(users)
        for _ in range(n + 1) :
            to_follow = dict_users.popitem()
            sleep(randint(2, 5))
            if self.user.friendships_create(to_follow[0]) :
                final_dict.update(to_follow[0], to_follow[1])

            return json.dumps(final_dict)

