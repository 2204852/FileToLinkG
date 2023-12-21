from pyrogram.errors import UserNotParticipant
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from FileStream.utils.translation import LANG
from FileStream.utils.database import Database
from FileStream.utils.human_readable import humanbytes
from FileStream.config import Telegram, Server
from FileStream.bot import FileStream

db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)

async def is_user_joined(bot, message: Message):
    try:
        user = await bot.get_chat_member(Telegram.UPDATES_CHANNEL, message.chat.id)
        if user.status == "BANNED":
            await message.reply_text(
                text=LANG.BAN_TEXT,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True

            )
            return False
    except UserNotParticipant:
        await message.reply_photo("https://graph.org/file/ea80f7cdbc7a9bfd9378c.jpg",
            caption="<i>🔒 𝗝𝗼𝗶𝗻 𝗠𝘆 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲 🔒</i>",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔑", url=f"https://t.me/{Telegram.UPDATES_CHANNEL}")
                ]] 
            ),
            parse_mode=ParseMode.HTML
        )
        return False
    except Exception:
        await message.reply_photo("https://graph.org/file/001d95bd8cafdf05e9d8b.jpg",
            caption=f"<i>Sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</i> <b><a href='https://t.me/gk_botz'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>",
          )
        return False
    return True

#---------------------[ PRIVATE GEN LINK + CALLBACK ]---------------------#

async def gen_link(_id):
    file_info = await db.get_file(_id)
    file_name = file_info['file_name']
    file_size = humanbytes(file_info['file_size'])
    mime_type = file_info['mime_type']

    page_link = f"{Server.URL}watch/{_id}"
    stream_link = f"{Server.URL}dl/{_id}"
    file_link = f"https://t.me/{FileStream.username}?start=file_{_id}"

    if "video" in mime_type:
        stream_text = LANG.STREAM_TEXT.format(stream_link, page_link, file_link)
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("𝙎𝙏𝙍𝙀𝘼𝙈 🖥", url=page_link), InlineKeyboardButton("𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿 📥",url=stream_link)],
                [InlineKeyboardButton("𝘾𝙇𝙊𝙎𝙀 ❌", callback_data="close")]
            ]
        )
    else:
        stream_text = LANG.STREAM_TEXT_X.format( stream_link, file_link)
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿 📥", url=stream_link)],
                [InlineKeyboardButton("𝘾𝙇𝙊𝙎𝙀 ❌", callback_data="close")]
            ]
        )
    return reply_markup, stream_text

#---------------------[ GEN STREAM LINKS FOR CHANNEL ]---------------------#

async def gen_linkx(m:Message , _id, name: list):
    file_info = await db.get_file(_id)
    file_name = file_info['file_name']
    mime_type = file_info['mime_type']
    file_size = humanbytes(file_info['file_size'])

    page_link = f"{Server.URL}watch/{_id}"
    stream_link = f"{Server.URL}dl/{_id}"
    file_link = f"https://t.me/{FileStream.username}?start=file_{_id}"

    if "video" in mime_type:
        stream_text= LANG.STREAM_TEXT_X.format( stream_link, page_link)
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("𝙎𝙏𝙍𝙀𝘼𝙈 🖥", url=page_link), InlineKeyboardButton("𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿 📥", url=stream_link)]
            ]
        )
    else:
        stream_text= LANG.STREAM_TEXT_X.format( stream_link, file_link)
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿 📥", url=stream_link)]
            ]
        )
    return reply_markup, stream_text

#---------------------[ USER BANNED ]---------------------#

async def is_user_banned(message):
    if await db.is_user_banned(message.from_user.id):
        await message.reply_text(
            text=LANG.BAN_TEXT.format(Telegram.OWNER_ID),
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return True
    return False

#---------------------[ CHANNEL BANNED ]---------------------#

async def is_channel_banned(bot, message):
    if await db.is_user_banned(message.chat.id):
        await bot.edit_message_reply_markup(
            chat_id=message.chat.id,
            message_id=message.id,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(f"ᴄʜᴀɴɴᴇʟ ɪs ʙᴀɴɴᴇᴅ", callback_data="N/A")]])
        )
        return True
    return False

#---------------------[ USER AUTH ]---------------------#

async def is_user_authorized(message):
    if hasattr(Telegram, 'AUTH_USERS') and Telegram.AUTH_USERS:
        user_id = message.from_user.id

        if user_id == Telegram.OWNER_ID:
            return True

        if not (user_id in Telegram.AUTH_USERS):
            await message.reply_text(
                text="You are not authorized to use this bot.",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
            return False

    return True

#---------------------[ USER EXIST ]---------------------#

async def is_user_exist(bot, message):
    if not bool(await db.get_user(message.from_user.id)):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Telegram.LOG_CHANNEL,
            f"**#NᴇᴡUsᴇʀ**\n**⬩ ᴜsᴇʀ ɴᴀᴍᴇ :** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n**⬩ ᴜsᴇʀ ɪᴅ :** `{message.from_user.id}`"
        )

async def is_channel_exist(bot, message):
    if not bool(await db.get_user(message.chat.id)):
        await db.add_user(message.chat.id)
        members = await bot.get_chat_members_count(message.chat.id)
        await bot.send_message(
            Telegram.LOG_CHANNEL,
            f"**#NᴇᴡCʜᴀɴɴᴇʟ** \n**⬩ ᴄʜᴀᴛ ɴᴀᴍᴇ :** `{message.chat.title}`\n**⬩ ᴄʜᴀᴛ ɪᴅ :** `{message.chat.id}`\n**⬩ ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs :** `{members}`"
        )

async def verify_user(bot, message):
    if not await is_user_authorized(message):
        return False

    if await is_user_banned(message):
        return False

    await is_user_exist(bot, message)

    if Telegram.FORCE_UPDATES_CHANNEL:
        if not await is_user_joined(bot, message):
            return False

    return True
    
