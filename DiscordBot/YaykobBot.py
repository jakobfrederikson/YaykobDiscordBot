import os
import discord
import csv
import random
from dotenv import load_dotenv
load_dotenv(dotenv_path = os.path.abspath(os.getcwd()) + "\discordbot.env")
TOKEN = os.getenv("CLIENT_TOKEN")
print("Absolute path = " + os.path.abspath(os.getcwd()))
client = discord.Client()

phrases = []
with open("RedditTopPosts.csv", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        phrases.append(row[2]) # 2 index is the title

@client.event
async def on_ready():
    print(f"{client.user} is live!")
    #channel = client.get_channel(328796156240986114)
    #await channel.send("I am awake :D")

@client.event
async def on_message(message):
    if message.content.startswith("$yayk_greet"):
        await message.channel.send(f"Hello {message.author}! You sent your message from {message.channel.name}.")
    elif message.content.startswith("$yayk_reddit"):
        response = phrases[random.randint(0,len(phrases)-1)]
        await message.channel.send(f"Thoughts on this, {message.author}?\n`" + response + "`")

@client.event
async def on_disconnect():
    channel = client.get_channel(328796156240986114)
    await channel.send("I'm shutting down peeps, peace out.")

client.run(TOKEN)