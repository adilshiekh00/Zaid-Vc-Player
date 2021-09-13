from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **ℍ𝕚𝕚𝕚𝕚𝕚 ꜱɪʀ, ɪ ᴍ {query.message.from_user.mention}** \n
💭 ** 𝕀 𝕒𝕞 𝕧𝕖𝕣𝕪 𝕤𝕨𝕖𝕖𝕥 𝕞𝕦𝕤𝕚𝕔 𝕓𝕠𝕥 𝕗𝕠𝕣 𝕪𝕠𝕦𝕣 𝕤𝕨𝕖𝕖𝕥 𝕤𝕞𝕚𝕝𝕖 ☺️❤️ 𝕛𝕠𝕚𝕟 𝕞𝕖 𝕚𝕟 𝕪𝕠𝕦𝕣 𝕘𝕣𝕠𝕦𝕡 𝕒𝕟𝕕 𝕗𝕖𝕖𝕝 𝕓𝕖𝕥𝕥𝕖𝕣 👀❤️⚡️ 𝕞𝕒𝕕𝕖 𝕓𝕪 @HARAMI_BACHA_HU_SAMBHAL_KAR 👿♥️
𝕁𝕆𝕀ℕ https://t.me/official_learning_zone ⚡️♥️ !**

💡 ** 𝙁𝙊𝙍 𝙆𝙉𝙊𝙒𝙄𝙉𝙂 𝙈𝙔 𝘾𝙊𝙈𝙈𝘼𝙉𝘿 𝘾𝙇𝙄𝘾𝙆 𝙊𝙉 » 📚 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗯𝘂𝘁𝘁𝗼𝗻 !**

❓ **𝗙𝗼𝗿 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝗮𝗹𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁, 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗲 /help**

   ** https://telegra.ph/file/3f2400fa5eeec4ba0a80d.jpg **
   """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ᴄʜᴀᴛꜱ 😄", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "😢 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "😄 ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "💝 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/HARAMI_BACHA_HU_SAMBHAL_KAR")
                ],[
                    InlineKeyboardButton(
                        "👥 ᴏꜰꜰɪᴄɪᴀʟ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/official_learning_zone"
                    ),
                    InlineKeyboardButton(
                        "🔥 ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/offical_learning_zone")
                ],[
                    InlineKeyboardButton(
                        "😁 ᴏꜰꜰɪᴄɪᴀʟ ᴢᴀɪᴅ ᴄʜᴀᴛ", url="https://t.me/Lolgrpbc")
                ],[
                    InlineKeyboardButton(
                        "😉 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ😍", url="https://github.com/adilshiekh00/Zaid-Vc-Player"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **crush ɪꜱ ʀᴜɴɴɪɴɢ**\n<b>💠 **ᴜᴘᴛɪᴍᴇ:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ ɢʀᴏᴜᴘ", url=f"https://t.me/official_learning_zone"
                    ),
                    InlineKeyboardButton(
                        "📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/offical_learning_zone"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands powered By Zaid!**

⚡ __Powered by {BOT_NAME} ADIL""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❔ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} ADIL__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ ʙᴀꜱɪᴄ ᴄᴍᴅꜱ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "❣️ ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴍᴅꜱ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "😏 ᴀᴅᴍɪɴ ᴄᴍᴅꜱ", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "⏲️ ꜱᴜᴅᴏ ᴄᴍᴅꜱ", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🙂 ᴏᴡɴᴇʀ ᴄᴍᴅꜱ", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "😍 ꜰᴜɴ ᴄᴍᴅꜱ", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴢ ᴘɪɴɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "𝚣 `ᴘᴏɴɢ!!`\n"
        f"🇿  `{delta_ping * 1000:.3f} ᴍꜱ`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 CRUSH ꜱᴛᴀᴛᴜꜱ:\n"
        f"• **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"• **ꜱᴛᴀʀᴛ ᴛɪᴍᴇ:** `{START_TIME_ISO}`"
    )
