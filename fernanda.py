import random
import telepot
import time
import pprint
import requests
import apiai

exhortations = [
    "Your friends won't believe you've been here until you take those photos!",
    "Take selfies at these places!",
    "Take those selfies and move on! Quick quick quick!",
    "How exciting!",
    "Isn't this just wonderful?",
    "What nice weather to be taking selfies...",
    "Hurry up, we need to get to the next monument"
]


def geonames(chat_id, lat, lon):
    params = {'lat': lat, 'lng': lon, 'username': 'randomshinichi'}
    r = requests.get(
        'http://api.geonames.org/findNearbyWikipediaJSON', params=params)
    results = r.json()['geonames']
    for r in results[:3]:  # limit to 3
        message = r['title'] + '\n' + r['wikipediaUrl']
        bot.sendMessage(chat_id, message)
    bot.sendMessage(
        chat_id, random.choice(exhortations))
    return


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print("____________________________")
    pprint.pprint(msg)
    if content_type == 'location':
        lat = msg.get('location').get('latitude')
        lon = msg.get('location').get('longitude')
        geonames(chat_id, lat, lon)
    else:
        bot.sendMessage(chat_id, 'eh?')

bot = telepot.Bot('220397560:AAGvgsTCJ0xh_m0Q4RGkm0wfYbqlZwAcLg4')
# ai = apiai.ApiAI('a0ce2e901d0a45ffbd230e886373b79d')
bot.message_loop(handle)

print("Listening...")
while True:
    time.sleep(10)
