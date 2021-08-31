#importing discord package
import random
from datetime import date
import os
from colors import colors
import discord
from profile import GET_PROFILE
from dotenv import load_dotenv
from googleapiclient.discovery import build
from discord.ext import commands


client = commands.Bot(command_prefix="!")

load_dotenv()
my_token =os.getenv('TOKEN')
API_KEY=os.getenv('API_KEY')
CUSTOM_SEARCH_ENGINE_ID=os.getenv('CUSTOM_SEARCH_ENGINE_ID')
pfp_path =GET_PROFILE()

fp = open(pfp_path, 'rb')
pfp = fp.read()
# today=date.today()
# d1 = today.strftime("%d/%m/%Y")
# from discord.ext import commands
# client=commands.Bot(command_prefix='!')

# @client.command(name='about')
# async def about(context):
#
#     my_embed = discord.Embed(title="Creator's name", description="Naitik Patil", color=0x00ff00)
#     my_embed.add_field(name="Education", value="2nd Year Student at IIIT Surat", inline=False)
#     my_embed.add_field(name="Extra Info", value="Python Lover", inline=False)
#     my_embed.set_footer(text="LLM Bot",
#                         icon_url="")
#
#     await context.message.channel.send(embed=my_embed)

# @client.event
# async def on_ready():
#     general_channel= client.get_channel(int(my_channel))
#     await general_channel.send('Hello myself LLM')
@client.event
async def on_ready():
    print('Bot has logged in as {0.user}'.format(client))


@client.command(aliases=["show"])
async def showpic(ctx, *,search):

    ran = random.randint(0, 9)
    resource=build("customsearch", "v1",developerKey=API_KEY).cse()
    result=resource.list(q=f"{search}",cx=CUSTOM_SEARCH_ENGINE_ID,searchType="image").execute()
    url=result["items"][ran]["link"]
    print(url)
    embed1 = discord.Embed(title=f"Here is your image({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)


# @client.event
# async def on_message(message):
#
#     if message.content.startswith('!help'):
#         await message.reply('Tere baap ka naukar nai me')
#
#     elif message.content.startswith('!hello'):
#         await message.reply('Hello! how can I help you?')
#
#     elif message.content.startswith('!about'):
#         x=random.randint(0,len(colors))
#         my_embed = discord.Embed(title="Creator's name", description="Naitik Patil", color=colors[x])
#         my_embed.add_field(name="Education", value="2nd Year Student at IIIT Surat", inline=False)
#         my_embed.add_field(name="Extra Info", value="Python Lover", inline=False)
#         my_embed.set_footer(text="LLM Bot",icon_url="")
#         await message.reply(embed=my_embed)
#
#     elif message.content == ('!private'):
#         await message.author.send("Hello")
#
#     elif message.content.startswith('!change_profile'):
#        await client.user.edit(avatar=pfp)
# #



@client.event
async def on_disconnect():
    await client.send_message('Bye All!')




#running client on the server
client.run(my_token)



