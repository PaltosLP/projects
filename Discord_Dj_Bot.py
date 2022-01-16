import os
import discord
from discord.ext import commands ,tasks
import music
from random import choice


token = os.environ['token']
client = commands.Bot(command_prefix="$")


cogs = [music]
for i in range(len(cogs)):
  cogs[i].setup(client)

status = ["doin dj stuff", "sleepin", "bein breezy"]

@client.event
async def on_ready():
  change_status.start()
  print("Bot is online!")


@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
  await ctx.send(f'**Pong!** Latency : {round(client.latency * 1000)}ms')


@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
  responses = ['***grumble*** Why did u wake me up???!!', 'Salut', 'Mornin', 'Aight']
  await ctx.send(choice(responses))

@tasks.loop(seconds=20)
async def change_status():
  await client.change_presence(activity=discord.Game(choice(status)))


client.run(token)
