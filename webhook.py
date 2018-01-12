from pprint import pprint
import requests

bot_token = '546577892:AAFsE6ZyvMl2ktCE0MgI2WtyieJNSzNjAKM'
test_url = "https://4f9d6af6.ngrok.io/{}".format(bot_token)

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

r = requests.get(get_url("setWebhook"), data={"url": test_url})
r = requests.get(get_url("getWebhookInfo"))
pprint(r.status_code)
pprint(r.json())