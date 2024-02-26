# Code for a discord bot that sends leetcode questions 

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, File
from responses import get_response

# Used https://www.youtube.com/watch?v=UYJDKSah-Ww to set up Discord bot

# Load Discord Token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up bot
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# Allow bot to send messages
async def send_message(message : Message, user_message : str) -> None:
    # Set to trigger on either "!leetcode" or "?leetcode"
    if not user_message or (user_message[:9] != "!leetcode" and user_message[:9] != "?leetcode"):
        return
    
    is_private = user_message[:9] == "?leetcode" # Do they want the question directly messaged to them
    user_message = user_message[10:]     
    try:
        response, has_img  = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        if has_img:
            await message.author.send(file=File('img.png')) if is_private else await message.channel.send(file=File('img.png'))
    except Exception as e:
        raise(e) # modify 
    
# Startup the bot
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")

# Handle incoming messages
@client.event
async def on_message(message : Message) -> None:
    if message.author == client.user: # so bot does not respond to itself
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f"[{channel}] {username}: {user_message}")
    await send_message(message, user_message)

# main
def main() -> None:
    client.run(token=TOKEN)
    # send_message("LEETCODE_QUESTION_BOT#5944 is now running!", None)

if __name__ == "__main__":
    main()