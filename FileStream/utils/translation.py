from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT =  """
𝙃𝙞 👋, {}\n 
𝐈 𝐀𝐦 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 <a href= 'https://t.me/gk_file2link_bot'>𝐅𝐢𝐥𝐞 𝐓𝐨 𝐋𝐢𝐧𝐤</a> 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫, 𝐉𝐮𝐬𝐭 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐀𝐧𝐲 𝐌𝐞𝐝𝐢𝐚 𝐎𝐫 𝐕𝐢𝐝𝐞𝐨 𝐓𝐨 𝐆𝐞𝐭 𝐃𝐢𝐫𝐞𝐜𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐀𝐧𝐝 𝐒𝐭𝐫𝐞𝐚𝐦 𝐋𝐢𝐧𝐤...\n\n

      𝐌𝐚𝐝𝐞 𝐁𝐲 ❤️: <a href='https://t.me/GKBOTZ'>𝙂𝙆 𝘽𝙊𝙏𝙕™</a>"""

         
 

    HELP_TEXT = """   ㅤ ㅤ ㅤ 𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞 ❓\n
      - ғᴏʀᴡᴀʀᴅ ᴀɴʏ ᴠɪᴅᴇᴏ ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ.\n  - ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ.\n- ᴅᴏɴ'ᴛ ғᴏʀᴡᴀʀᴅ 𝟷𝟾+ ᴏʀ ᴘᴇʀsᴏɴᴀʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.

       
        <a href='https://t.me/gk_botz'>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐔𝐬 ✉️</a>"""
       

    
    ABOUT_TEXT = """<b>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟
 ‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/gk_file2link_bot>𝙁𝙞𝙡𝙚 𝙏𝙤 𝙇𝙞𝙣𝙠</a>
 ‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/GKBOTZ'>𝙂𝙆 𝘽𝙊𝙏𝙕™</a> 
 ‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢</a> 
 ‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>𝙋𝙮𝙩𝙝𝙤𝙣3</a> 
 ‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>𝙈𝙤𝙣𝙜𝙤𝘿𝘽</a> 
 ‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='tg://settingstg'>𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢</a> 
 ‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ1.3 [sᴛᴀʙʟᴇ]></b>"""

    STREAM_TEXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>🖥 Wᴀᴛᴄʜ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""
    
    

    BAN_TEXT = """𝙎𝙤𝙧𝙧𝙮 𝙏𝙤 𝙎𝙖𝙮, 𝘽𝙪𝙩 𝙔𝙤𝙪 𝘼𝙧𝙚 𝘽𝙖𝙣𝙣𝙚𝙙 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙮 𝙊𝙬𝙣𝙚𝙧 𝙐𝙨 𝙏𝙤 𝙍𝙚𝙨𝙤𝙡𝙫𝙚 𝙏𝙝𝙞𝙨 𝙄𝙨𝙨𝙪𝙚...!
    
    
                      [𝐎𝐖𝐍𝐄𝐑 🎇](https://t.me/talk2smile_bot)"""
          
       
    
       

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('𝙃𝙚𝙡𝙥 ❓', callback_data='help'),
            InlineKeyboardButton('𝘼𝙗𝙤𝙪𝙩 🤔', callback_data='about'),
            InlineKeyboardButton('𝘾𝙡𝙤𝙨𝙚 ❌', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('𝙃𝙤𝙢𝙚 🏠', callback_data='home'),
            InlineKeyboardButton('𝘼𝙗𝙤𝙪𝙩 🤔', callback_data='about'),
            InlineKeyboardButton('𝘾𝙡𝙤𝙨𝙚 ❌', callback_data='close'),
        ]]
       
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('𝙃𝙤𝙢𝙚 🏠', callback_data='home'),
            InlineKeyboardButton('𝙃𝙚𝙡𝙥 ❓', callback_data='help'),
            InlineKeyboardButton('𝘾𝙡𝙤𝙨𝙚 ❌', callback_data='close'),
        ]],
    )
    BAN_BUTTON = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐔𝐬 ✉️", url=f"https://t.me/gk_botz")
                ]],
    )
    
