import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_member_join(user=discord.Member):
    
    global bot

    channel = discord.Object('445125257062252564')
    server = user.server
    memer = discord.utils.get(server.roles, name="Regular Cunts (New niggas that should be welcomed with a tit pic (in dm of course) ok?)",)
    await bot.add_roles(user, memer)
    msg = "Yo {} you play Fortnite?".format(user.mention)
    await bot.send_message(channel, msg)

@bot.command()
@commands.has_role("Super Sexy Admins (Suck them off if you want to stay in this server)")
async def say(*, message:str):
    await bot.send_message(discord.Object('445125257062252564'), content=message)


@bot.command()
@commands.has_role("Super Sexy Admins (Suck them off if you want to stay in this server)")
@commands.cooldown(1, 30, commands.BucketType.user)
async def spam(times : int, *,content:str):
    for i in range(times):
        await bot.say(content)

@bot.command()
async def roll(number: int):
    dice = random.randint(1,number)
    await bot.say("The dice rolled " + str(dice))

bot.run("NDQ1MTQ4MzE1MjAyNjE3MzQ0.DdsfCA.984mb9zb_nxHPpEOd2ekqrkGOzA")
