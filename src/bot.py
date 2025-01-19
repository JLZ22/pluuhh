import discord 
import dotenv
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'git' in message.content.lower():
        await message.channel.send('https://github.com/JLZ22/Git-Tutorial-for-New-Users')
        
        
dotenv.load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client.run(token)