import discord
import random
from discord.ext import commands

a = random.randint(1,100)


client = commands.Bot(command_prefix = "$")
TOKEN = "ODQ5MzAzNzg4OTA0MzgyNTI0.YLZNyg.vrx1rQgkGvI8YkUxvphzfQfd568"
credit = "Bot made by Sparsh.py🔨"



@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Faded (Northern Tiesto Lights Remix)"))
    print("The bot is ready as {0.user}!".format(client))

@client.command()
async def hi(ctx):
    await ctx.send("Hello, I am w41k3r#0")

@client.command()
async def credits(ctx):
    await ctx.send(credit)

@client.command()
async def random(ctx):
    await ctx.send(a)




client.run(TOKEN)
