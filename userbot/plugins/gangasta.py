from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("gangasta ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Dead")
        await asyncio.sleep(0.3)
        await event.edit("Boy")
        await asyncio.sleep(0.2)
        await event.edit("Is")
        await asyncio.sleep(0.5)
        await event.edit("Biggest")
        await asyncio.sleep(0.2)
        await event.edit("Gangster")
        await asyncio.sleep(0.3)
        await event.edit("😈😈😈")
        await asyncio.sleep(0.3)
        await event.edit("🔥🔥🔥")
        await asyncio.sleep(0.3)
        await event.edit("Dead Boy Is Biggest Gangster 😈😈😈 🔥🔥🔥")
