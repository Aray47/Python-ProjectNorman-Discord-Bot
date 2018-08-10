from discord.ext.commands import Bot
import random
from discord import Game
import requests
import urllib.request
import urllib.parse
import re
import asyncio
import normansResponses
import normansMusic
import sys
import time
import json
import forecastio
import datetime
with open('cities.json') as f:
    data = json.load(f)

BOT_PREFIX = ("?", "!")
TOKEN = 'ENTER-TOKEN-KEY-HERE'
api_key = 'ENTER-API-KEY-HERE'

dtEast2 = datetime.datetime.today()
timeNow = dtEast2.strftime('%B %d, %Y, %I:%M %p')

client = Bot(command_prefix=BOT_PREFIX)

#basic 8ball game, imported responses and aliases from another module
@client.command(name='8ball',
                description="Answers YES or NO questions. Example: !8ball am I cool?",
                brief="Answers from the beyond",
                aliases= normansResponses.alias,
                pass_context=True)
async def eight_ball(context):
    possible_response = normansResponses.eightBallResponses
    await client.say(random.choice(possible_response) + ', ' + context.message.author.mention)


#simple square function
@client.command(brief="A simple square function.",
                description="Square two integers. Example: !square 33 44")
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


#pulling from bitcoin API 
@client.command(brief="Got Bitcoin?",
                description="Simple. Type !bitcoin to get the current rate of bitcoin")
async def bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" + value)

#background task that loops current servers said bot is integrated in
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers: ")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(30)

@client.command(brief="A random Grunge searcher")
async def grunge():
    sleepItABitLess()
    possible_answer = normansResponses.searchingResponses
    await client.say(random.choice(possible_answer))
    sleepItABit()
    possible_response = normansMusic.grungeSearch
    await client.say(random.choice(possible_response))

@client.command(brief="A random Metal searcher")
async def metal():
    sleepItABitLess()
    possible_answer = normansResponses.searchingResponses
    await client.say(random.choice(possible_answer))
    sleepItABit()
    possible_response = normansMusic.metalSearch
    await client.say(random.choice(possible_response))

@client.command(brief="A random Rap searcher")
async def rap():
    sleepItABitLess()
    possible_answer = normansResponses.searchingResponses
    await client.say(random.choice(possible_answer))
    sleepItABit()
    possible_response = normansMusic.rapSearch
    await client.say(random.choice(possible_response))

@client.command(brief="A random Hip-Hop searcher")
async def hip_hop():
    sleepItABitLess()
    possible_answer = normansResponses.searchingResponses
    await client.say(random.choice(possible_answer))
    sleepItABit()
    possible_response = normansMusic.hipHopSearch
    await client.say(random.choice(possible_response))

@client.command(brief="A random Classic Rock searcher")
async def classic_rock():
    sleepItABitLess()
    possible_answer = normansResponses.searchingResponses
    await client.say(random.choice(possible_answer))
    sleepItABit()
    possible_response = normansMusic.classicRockSearch
    await client.say(random.choice(possible_response))

#user ideas go in text file botIdeas.txt
@client.command(pass_context = True, brief='Log your ideas inside the developer notes!',
                description="Ideas are gret, lets hear 'em. Type !bot_ideas [Enter your idea here], and it will be logged")
async def bot_ideas(context, *idea):
    slam = (' '.join(idea))
    with open('botIdeas.txt', 'a+') as f:
        for s in slam:
            f.write(s)
        f.write('\n')
        possible_response = normansResponses.feedBackResponses
        sleepItABit()
        await client.say(random.choice(possible_response) + ', ' + context.message.author.mention)

def sleepItABit():
    time.sleep(2)

def sleepItABitLess():
    time.sleep(1)

@client.command(pass_context = True, brief='Check the weather near you.',
                description="Searches top 1,0000 US cities. You have to be near one of them. Type: !weather yourCityHere to find current conditions near you")
async def weather(context, *city):
    possible_response = normansResponses.searchingResponses
    await client.say(random.choice(possible_response) + ', ' + context.message.author.mention)
    uI = (' '.join(city))
    x = 0
    try:
        for c in data['cities']:
            if c['city'].lower() in uI.lower():
                x = 1
                userLat = c['latitude']
                userLong = c['longitude']
                forecast = forecastio.load_forecast(api_key, userLat, userLong)
                byCurr = forecast.currently()
                byDay = forecast.daily()
                await client.say('\n---Weather Information for %s---'% uI.title())
                await client.say('Time: %s'% timeNow)
                await client.say('Current Temperature: %d°F'% byCurr.temperature)
                await client.say('Daily Summary: %s'% byDay.summary)
                await client.say('\n')
                break
    except:
        pass
    if x == 0:
        await client.say('No matches were found')

@client.command(brief="A custom youtube searcher, look up anything!")
async def searchYT(*search):
    query_string = urllib.parse.urlencode({"search_query" : search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    await client.say("The top result is: ")
    await client.say("http://www.youtube.com/watch?v=" + search_results[0])
    # await client.say("http://www.youtube.com/watch?v=" + search_results[1])
    # await client.say("http://www.youtube.com/watch?v=" + search_results[2])



#showing the bot logged in, changing his game presence
@client.event
async def on_ready():
    await client.change_presence(game=Game (name="L2 Human"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(list_servers())
client.run(TOKEN)
