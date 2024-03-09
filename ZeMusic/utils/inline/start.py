from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᗩᗪᗪ ᗰE TO YOᑌᖇ GᖇOᑌᑭ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="父 الأوامر 父", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="˹ ᴏɢ ✗ ᴛᴇᴛᴏ ˼", url=f"https://t.me/wzaere"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᗩᗪᗪ ᗰE TO YOᑌᖇ GᖇOᑌᑭ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="父 الأوامر 父", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="ᗪEᐯEᒪOᑭEᖇ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="˹ ᴏɢ ✗ ᴛᴇᴛᴏ ˼", url=f"https://t.me/wzaere"),
        ],
    ]
    return buttons
