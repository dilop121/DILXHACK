import env
import os
import random
from telethon.tl.custom import Button
from telethon.tl.types import InputMediaPhoto
from DILXHACK import bot
from DILXHACK.helpers import MENU1, KEYBOARD1
from DILXHACK.database import DB

from telethon import events


async def hack(event):
    if not event.is_private:
        return await event.reply("You can't use me in groups.")
    await event.reply(MENU1, buttons=KEYBOARD1)


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    id = event.sender_id
    mention = f"[{event.sender.first_name}](tg://user?id={id})"
    TEXT = "ʀᴀᴍ ʀᴀᴍ {} 🚩,\n ɪ ᴀᴍ sᴇssɪᴏɴ ʜᴀᴄᴋ ʙᴏᴛ ғᴏʀ ʙᴏᴛʜ ᴘʏʀᴘɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ sᴛʀɪɴɢs.\n ᴛʏᴘᴇ /hack ᴏʀ ᴄʟɪᴄᴋ ᴏɴ ʜᴀᴄᴋ ʙᴜᴛᴛᴏɴ ᴛᴏ sᴇᴇ ᴛʜᴇ ᴍᴇɴᴜ"
    
    buttons = [
        [Button.inline("ʜᴀᴄᴋ", data="hack")],
        [Button.inline("ᴏᴡɴᴇʀ", data="owner"), Button.inline("sᴜᴘᴘᴏʀᴛ", data="support")]      
    ]
    
    photo_urls = [
        "https://graph.org/file/210751796ff48991b86a3.jpg",
        "https://graph.org/file/7b4924be4179f70abcf33.jpg",
        "https://graph.org/file/f6d8e64246bddc26b4f66.jpg",
        "https://graph.org/file/9f12dc2a668d40875deb5.jpg",
    ]
    
    random_photo_url = random.choice(photo_urls)
    
    await bot.send_message(event.chat_id, TEXT.format(mention), buttons=buttons, file=random_photo_url)
    
    if DB:
        await DB.add_user(id)
    
    if env.LOG_GROUP_ID:
        await bot.send_message(env.LOG_GROUP_ID, f'{mention} Has Just Started The Bot')

@bot.on(events.CallbackQuery())
async def callback_handler(event):
    data = event.data.decode("utf-8")
    chat_id = event.chat_id

    if data == "owner":
        await bot.send_message(chat_id, "This is the owner link: [Owner Link](https://t.me/dil_sagar_121)")
    
    elif data == "support":
        await bot.send_message(chat_id, "This is the support link: [Support Link](https://t.me/alonegroup121)")

    elif data == "hack":
        await hack(event)



@bot.on(events.NewMessage(pattern="/hack"))
async def hack(event):
    if not event.is_private:
        return await event.reply("You can't use me in groups.")
    await event.reply(MENU1, buttons=KEYBOARD1)
