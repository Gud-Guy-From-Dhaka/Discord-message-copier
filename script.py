import os import discord from 
discord import Webhook import 
aiohttp from dotenv import 
load_dotenv load_dotenv() TOKEN = 
os.getenv('DISCORD_TOKEN') 
WEBHOOK_URL = 
os.getenv('WEBHOOK_URL') 
SOURCE_CHANNELS = [int(id.strip()) 
for id in 
os.getenv('SOURCE_CHANNELS').split(',')] 
intents = 
discord.Intents.default() 
intents.message_content = True 
client = 
discord.Client(intents=intents) 
@client.event async def 
on_ready():
    print(f'Mirroring active as 
    {client.user}')
@client.event async def 
on_message(message):
    if message.author.bot: return 
    if message.channel.id in 
    SOURCE_CHANNELS:
        async with 
        aiohttp.ClientSession() as 
        session:
            webhook = 
            Webhook.from_url(WEBHOOK_URL, 
            session=session)
            
            files = [] for 
            attachment in 
            message.attachments:
                files.append(await 
                attachment.to_file())
            await webhook.send( 
                content=message.content, 
                username=message.author.display_name, 
                avatar_url=message.author.display_avatar.url, 
                embeds=message.embeds, 
                files=files
            ) client.run(TOKEN)
