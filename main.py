#importing discord package
import os
import discord
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()
my_token =os.getenv('TOKEN')
my_channel=os.getenv('CHANNEL')

# from discord.ext import commands
# client=commands.Bot(command_prefix='!')

# @client.command(name='about')
# async def about(context):
#     general_channel = client.get_channel(my_channel)
#     my_embed = discord.Embed(title="Creator's name", description="Naitik Patil", color=0x00ff00)
#     my_embed.add_field(name="Education", value="2nd Year Student at IIIT Surat", inline=False)
#     my_embed.add_field(name="Extra Info", value="Python Lover", inline=False)
#     my_embed.set_footer(text="LLM Bot",
#                         icon_url="https://media-exp1.licdn.com/dms/image/C4E03AQE6F2DNev849A/profile-displayphoto-shrink_800_800/0/1617857843029?e=1635984000&v=beta&t=PvAn8gXsdMmVl6y509dV4Ff6JdbHjOaZKTX6gFJxYqU")
#
#     await context.message.channel.send(embed=my_embed)

@client.event
async def on_ready():
    general_channel= client.get_channel(int(my_channel))
    await general_channel.send('Hello myself LLM')


@client.event
async def on_message(message):
    if message.content =='!hello':
        general_channel = client.get_channel(int(my_channel))
        await general_channel.send('Hello! how can I help you?')

    elif message.content == '!about':
        general_channel = client.get_channel(int(my_channel))
        my_embed = discord.Embed(title="Creator's name", description="Naitik Patil", color=0x00ff00)
        my_embed.add_field(name="Education", value="2nd Year Student at IIIT Surat", inline=False)
        my_embed.add_field(name="Extra Info", value="Python Lover", inline=False)
        my_embed.set_footer(text="LLM Bot",icon_url="https://media-exp1.licdn.com/dms/image/C4E03AQE6F2DNev849A/profile-displayphoto-shrink_800_800/0/1617857843029?e=1635984000&v=beta&t=PvAn8gXsdMmVl6y509dV4Ff6JdbHjOaZKTX6gFJxYqU")
        await general_channel.send(embed=my_embed)


@client.event
async def on_disconnect():

    general_channel = client.get_channel(int(my_channel))
    await general_channel.send('Bye All')







#running client on the server
client.run(my_token)



