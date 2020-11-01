import discord
import json
import random
import asyncio

from random_word import RandomWords

client = discord.Client()
r = RandomWords()

@client.event
async def on_ready():
    print('Welcome Bot has logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" for new players since 2020"))
    print('Status updated!')
    print('Listening has begun...')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.split() == []:
        return
    if message.content.split()[0] == "&#@$%BeginInitiation":
        if(len(message.content.split()) != 3):
            await message.channel.send("Incorrect syntax. The correct command syntax is `&#@$%BeginInitiation <member mention> <number of attempts>`")
        else: 
            if(len(message.mentions) != 1 or not message.content.split()[2].isdigit()):
                await message.channel.send("Incorrect syntax. The correct command syntax is `&#@$%BeginInitiation <member mention> <number of attempts>`")
            else:
                guild = message.guild
                for channel in guild.text_channels:
                    if(channel.name == "general"):
                        await beginOnslaught(channel, message.mentions[0], int(message.content.split()[2]))

@client.event
async def on_member_join(member):
    guild = member.guild
    for channel in guild.text_channels:
        if(channel.name == "general"):
            def check(message):
                return message.author.id == member.id and message.channel == channel                    
            msg = await client.wait_for('message', check=check, timeout=30)
            if msg:
                await msg.add_reaction('\N{HEAVY BLACK HEART}')
            await asyncio.sleep(6)
            await channel.send("Welcome {} to Techers! Here is the general chat. Join in on the conversation!".format(member.mention))
    roles = guild.roles
    for role in roles:
        if(role.name == "Welcomer"):
            await ping(guild, role, member)

async def ping(guild, role, joinMember):
    pingString = ""
    for member in role.members:
        pingString += member.mention + " "
    pingString += " a new user has joined! Welcome them! Their name is "
    pingString += joinMember.name
    print(pingString + " -- " + guild.name)
    pingString += "\nAlso remember to link #rule and #roles!"
    for channel in guild.text_channels:
        if(channel.name == "welcomers"):
            message = await channel.send(pingString)
        
async def beginOnslaught(channel, member, length):
    await channel.send("Let the initiation for {0} begin!".format(member.mention))
    print("Initiation successfully intiated for {}!".format(member.name))
    for i in range(length):
        await channel.send(generateWelcomeMessage() + " ({0}/{1})".format(i + 1, length))
        def checkResponse(message):
            return message.author == member and message.channel == channel
        role = False
        rule = False
        while(not role or not rule):
            msg = await client.wait_for('message', check=checkResponse)
            if "#roles" in msg.clean_content:
                role = True
            if "#rules" in msg.clean_content:
                rule = True
    await channel.send("{0}'s Initiation is complete! {0}, wait for the WelcomeBots to evaluate your work.".format(member.mention))
    print("Initiation successfully completed for {}!".format(member.name))


def generateWelcomeMessage():
    name = r.get_random_word()
    name = "__**" + name  + "**__"
    return chooseRandomJoinMessage().format(name)

def chooseRandomJoinMessage():
    with open('./joinMessages.json') as f:
        messages = json.load(f)
    randomNum = random.randrange(0,len(messages))
    return messages[randomNum]

client.run('token_here')