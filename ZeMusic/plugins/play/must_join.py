from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZeMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/Teto_Support":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("Teto_Support", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/Teto_Support".isalpha():
                link = "https://t.me/Teto_Support"
            else:
                chat_info = await bot.get_chat("UI_VM")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ\n⌯︙قناة البوت: @Teto_Support .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ᯓ 𝚂𝙾𝚄𝚁𝙲𝙴 𝚃𝙴𝚃𝙾 𝅘𝅥𝅯", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @WX_PM !")
