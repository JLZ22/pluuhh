import discord 
import dotenv
import os
import re
import yaml

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
pluh_pattern = "plu+h+"

dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'keywords.yaml'), 'r') as f:
    config = yaml.safe_load(f)
    assert isinstance(config, dict), 'keywords.yaml is not a dictionary'
    
def sanitize(msg):
    return re.sub(r'[^a-zA-Z0-9\s]', '', msg.lower())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if not re.search(pluh_pattern, message.channel.name.lower()):
        return

    msg = sanitize(message.content)
    if not msg:
        return
    for word, link in config.items():
        if word in msg:
            try:
                await message.channel.send(link)
            except Exception as e:
                print(f"Error sending message: {e}")
            return

if 'DISCORD_TOKEN' in os.environ:
    del os.environ['DISCORD_TOKEN']    

dotenv.load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client.run(token)