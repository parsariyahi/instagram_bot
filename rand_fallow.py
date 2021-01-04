from user import client as cl
from random import randint
from time import sleep
from decorator import timer

username = "parsarh82"
password = "parsa1981"
users = { 'parsa' : 'parsariuyahj',
        'lklksadsafsfdsfsdfsdfsafsfa' : 'jflkdsjfsdjfkdlsajfskjf',
        'lksjfsiuoioiipipoiipoip' : 'oiiooiooiioiioiioiio',
        'poploplopppopppopppoop' : 'ppp;p;pppp;pppp;;p;pp',
        'ksajkfdjsa' : 'jflkdsjfsdjfkdlsajfskjf',
}

json = cl.json_parser(users)
print(json)
print(type(json))
#client = cl(username, password)

#print(client.random_follow_n_from_followers('ali.prkhn', 29))
