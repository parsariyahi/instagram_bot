from user import client as cl

username = "your username"
password = "your pass"

client = cl(username, password)

# follow n users randomly
print(client.random_follow_n_from_followers('ali.prkhn', n=10))
