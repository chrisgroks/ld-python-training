import ldclient
from ldclient.config import Config

ldclient.set_config(Config("sdk-key"))
ld_client = ldclient.get()

user = {"key": "1234"}


flag = ld_client.variation("punchline", user, False)

print("How does Nasa throw a party?")

if flag:
    print("They planet!")
else:
    print("flag is false")
ld_client.close()
