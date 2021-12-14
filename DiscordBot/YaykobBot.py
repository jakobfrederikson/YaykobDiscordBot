import os
import discord
from dotenv import load_dotenv
load_dotenv(dotenv_path = os.path.abspath(os.getcwd()) + "\DiscordBot\discordbot.env")
TOKEN = os.getenv("CLIENT_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} is live!")
    #channel = client.get_channel(328796156240986114)
    #await channel.send(":flushed:")

@client.event
async def on_message(message):
    if message.content.startswith("$yaykob"):
        await message.channel.send(f"Hello {message.author}, you sent your message from {message.channel.name}!")

@client.event
async def on_disconnect():
    channel = client.get_channel(328796156240986114)
    await channel.send("I'm shutting down peeps, peace out.")

client.run(TOKEN)