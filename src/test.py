import dotenv
import os

if 'DISCORD_TOKEN' in os.environ:
    del os.environ['DISCORD_TOKEN']
dotenv.load_dotenv('../.env')
print(os.getenv('DISCORD_TOKEN'))
print(os.getenv('TEST'))