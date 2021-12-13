import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} logged in now!")

@client.event
async def on_message(message):
    print(message.content)
    print(dir(message))
    await message.delete()

my_secret = "OTIwMDYxNTEyMTg4NTc5ODYx.Ybe4Dg.S8KoYuj-GUjkthWZt9gxiL3YwmQ"
client.run(my_secret)