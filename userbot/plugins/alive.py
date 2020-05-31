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
    await alive.edit("   **Welcome To Dead Bot ** \n\n"
        "**` ABE! ZINDA HUN🧐. Sab Sahi Chal Raha Hai   ... ψ(~_~)ψ`**\n\n"
                      "` 🔸 Database Status:` **All OK 👌!**\n"
                     f"` 🔹 My proest owner`: {DEFAULTUSER}\n\n"

         


