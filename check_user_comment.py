from user import client as cl
from random import randint
from time import sleep
import errors


username = "your username"
password = "your pass"

bot = cl(username, password)

print(bot.check_user_comment("parsariyahi82", "ali.prkhn"))
