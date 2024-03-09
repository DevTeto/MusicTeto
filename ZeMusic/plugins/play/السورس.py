import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","تيتو","السورس", "سورس تيتو"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/146c98707d56259c476b1.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ ᥉᥆ᥙᖇᥴᥱ ƚᥱƚ᥆ ](t.me/WX_PM)
么 [َ ძᥱ᥎ ƚᥱƚ᥆ ](t.me/wzaere)
么 [َ ᥉υρρ᥆ᖇƚ ](t.me/Teto_Support)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹  ძᥱ᥎ ƚᥱƚ᥆ . 🕷 › ", url=f"https://t.me/wzaere"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ›", url=f"https://t.me/WX_PM"), 
                    InlineKeyboardButton(
                        "‹ ᥉υρρ᥆ᖇƚ›", url=f"https://t.me/Teto_Support"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/UUIYBOT?startgroup=true"),
            ]
        ]
         ),
     )
  
