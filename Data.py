# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
𝗣𝗥𝗜𝗖𝗘 𝗟𝗜𝗦𝗧 𝗩𝗩𝗜𝗣 💰

— VVIP INDO : Rp. 30.000,-
— VVIP HIJAB : Rp. 35.000,-
— VVIP ONLYFANS : Rp. 35.000,-
— VVIP CAMPURAN : Rp. 30.000,-
— VVIP JAV HD : Rp. 35.000,-
— VVIP LIVE RECORD : Rp. 30.000,-

— VVIP PREMIUM : Rp. 100.000,-

PROMO HEMAT 🪙
— Rp. 165.000 TAKE ALL CHANNNEL VVIP NO PREMIUM
— Rp. 225.000 TAKE ALL CHANNEL VVIP WITH PREMIUM

PC @HeadSchool Kalau limit bisa pc bot @SchoolServiceBOT
"""

    close = [
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("VVIP", callback_data="help"),
            InlineKeyboardButton("CLOSE", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("JOIN VVIP", callback_data="about"),
            InlineKeyboardButton("CLOSE", callback_data="close")
        ],
    ]

    ABOUT = """
JOIN VVIP BISA LANGSUNG CHAT KE @HeadSchool / @SchoolServiceBOT, TIDAK MENERIMA PERTANYAAN BASA BASI, HANYA MENERIMA CHAT JOIN VVIP
"""
