from user import client as cl
from random import randint
from time import sleep
from decorator import timer

username = "parsarh82"
password = "parsa1981"
client = cl(username, password)

users = { 'parsa' : 'parsariuyahj',
        'lklksadsafsfdsfsdfsdfsafsfa' : 'jflkdsjfsdjfkdlsajfskjf',
        'lksjfsiuoioiipipoiipoip' : 'oiiooiooiioiioiioiio',
        'poploplopppopppopppoop' : 'ppp;p;pppp;pppp;;p;pp',
        'ksajkfdjsa' : 'jflkdsjfsdjfkdlsajfskjf',
}

json = client.json_parser(users)
print(json)
print(type(json))

#print(client.random_follow_n_from_followers('ali.prkhn', 29))
