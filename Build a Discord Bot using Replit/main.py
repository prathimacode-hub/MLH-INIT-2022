import discord
import os
from keep_alive import keep_alive
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('wipe'):
        await message.channel.send('**Wipe date is Friday March 26th**')

    if message.content.startswith('pure'):
        await message.channel.send('**pure is a badmod**')    
   
    if message.content.startswith('$botdev'):
        await message.channel.send('𝕃𝕒𝕔𝕚𝕘𝕒𝕞#1495')  

    if message.content.startswith('who is god'):
        await message.channel.send('taz.') 

    if message.content.startswith('$invite'):
        await message.channel.send('[INVITE](https://discord.com/api/oauth2/authorize?client_id=821174933182218300&permissions=8&scope=bot)') 

    if message.content.startswith('evolh'):
        await message.channel.send('evolh is a sus admin') 

    if message.content.startswith('$help'):
        await message.channel.send(os.getenv('HELP')) 

    if message.content.startswith('$help'):
        await message.channel.send('`$botdev - Shows Bot Devoloper`') 

    if message.content.startswith('$help'):
        await message.channel.send('`$wipe - Shows Insidious Wipe Date`') 

    if message.content.startswith('$help'):
        await message.channel.send('`$invite - Shows Bot Invite Link`') 

    if message.content.startswith('hazard'):
        await message.channel.send('I3ioHazard is kinda cute tho') 

keep_alive()
token = os.environ.get("TOKEN")
client.run(os.getenv('TOKEN'))
