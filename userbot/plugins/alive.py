"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet, check pinned in @TeleBotHelp"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("   **𝚂𝚑𝚛𝚎𝚢𝚊 𝙾𝚏𝚏𝚒𝚌𝚒𝚊𝚕 𝙱𝚘𝚝** \n\n"
        "**`𝙻𝚘𝚕! 𝚉𝚒𝚗𝚍𝚊 𝙷𝚞𝚗 𝚈𝚊𝚛𝚛. 𝙰𝚕𝚕 𝚜𝚢𝚜𝚝𝚎𝚖𝚜 𝚘𝚗𝚕𝚒𝚗𝚎 𝚊𝚗𝚍 𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗𝚒𝚗𝚐 𝚗𝚘𝚛𝚖𝚊𝚕𝚕𝚢... ψ(^_^)ψ`**\n\n"
                     "`  😘 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 𝚟𝚎𝚛𝚜𝚒𝚘𝚗:` **6.9.0**\n" 
                     "`  ❤️ 𝙿𝚢𝚝𝚑𝚘𝚗:` **3.7.3** \n"
                     "`  😘 𝙱𝚘𝚝 𝚌𝚛𝚎𝚊𝚝𝚎𝚍 𝚋𝚢:` [DEAD BOY](tg://user?id=1247419158)\n"
                     "`  ❤️ 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 𝚂𝚝𝚊𝚝𝚞𝚜:` **All OK 👌!**\n"
                     "`  😘 𝙼𝚢 𝙱𝚎𝚊𝚞𝚝𝚒𝚏𝚞𝚕 𝚘𝚠𝚗𝚎𝚛:`♡Shreya♡")
