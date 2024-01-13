from pyrogram import Client, filters
import re
from pyrogram.enums import ChatType
import asyncio
from random import randint
import datetime

api_id = 2815084
api_hash = "6e64163bfb52621e86c0d4d6137a66d1"
app = Client("my_acc", api_id, api_hash)

channel_username = "PROXYZAPASS"

async def send_post(post):
    async for dialog in app.get_dialogs():
        if (dialog.chat.type == ChatType.SUPERGROUP) or (dialog.chat.type == ChatType.GROUP):
            try:
                await app.copy_message(from_chat_id=channel_username, chat_id=dialog.chat.id, message_id=post.id)
                print("Message sent to: " + str(dialog.chat.id))
                await asyncio.sleep(randint(1, 10))
            except:
                pass

async def get_last_10_posts():
    posts = []
    i=0
    async for post in app.get_chat_history(channel_username):
        if i == 10:
            break
        last_post = str(post)
        proxys = []

        regex = r'https://t\.me/proxy\?server=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}&port=\d{1,5}&secret=[a-zA-Z0-9]+'
        for match in re.findall(regex, last_post):
            proxys.append(match)
        if len(proxys) > 0:
            posts.append(post)
            i+=1
    return posts
        
        
import random
async def main():
    while True:
        posts = await asyncio.create_task(get_last_10_posts())
        await asyncio.sleep(randint(0,60))
        post_list = []
        for post in posts:
            post_list.append(post)
        random.shuffle(post_list)
        for post in post_list:
            await asyncio.create_task(send_post(post))
            await asyncio.sleep(randint(300,600))
with app:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
