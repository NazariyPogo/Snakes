import discord
import os
import requests
import json
import time

from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print("IT'S YA BOI AGAIN")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send('WAAAZZZAAAAAA')

    if message.content.startswith('$sadge'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('WE DA BEST MUSIC'):
        time.sleep(2)
        await message.channel.send("ANOTHA' ONE")

bot.run('MTE0OTgwNDI5NTkxMTM4NzE1Ng.Gg_YCE._QCyOV16Au7ShRDPNyiTDKzGP8sLFlbD-TmXYc')
