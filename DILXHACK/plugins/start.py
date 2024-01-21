import env
import os
import random
from telethon.tl.custom import Button
from telethon.tl.types import InputMediaPhoto
from DILXHACK import bot
from DILXHACK.helpers import MENU1, KEYBOARD1
from DILXHACK.database import DB

from telethon import events


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    id = event.sender_id
    mention = f"[{event.sender.first_name}](tg://user?id={id})"
    TEXT = "Hey {}, I am a Session Hacker Bot Supporting Both Pyrogram and Telethon Session String. Type /hack to see menu"
    
    buttons = [
        [Button.inline("Owner", data="owner"), Button.inline("Support", data="support")],
    ]
    
    photo_urls = [
        "https://graph.org/file/37077de233a43b6da9cee.jpg",
        "https://graph.org/file/acb802ec1b54e02d4e692.jpg",
        "https://graph.org/file/2e84b98fe4bdb0b53807e.jpg",
        "https://graph.org/file/8883ddb847f34cdf0420d.jpg",
    ]
    
    random_photo_url = random.choice(photo_urls)
    
    await bot.send_message(event.chat_id, TEXT.format(mention), buttons=buttons, file=random_photo_url)
    
    if DB:
        await DB.add_user(id)
    
    if env.LOG_GROUP_ID:
        await bot.send_message(env.LOG_GROUP_ID, f'{mention} Has Just Started The Bot')



@bot.on(events.NewMessage(pattern="/hack"))
async def hack(event):
    if not event.is_private:
        return await event.reply("You can't use me in groups.")
    await event.reply(MENU1, buttons=KEYBOARD1)
