from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("gg ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Shreya")
        await asyncio.sleep(0.3)
        await event.edit("Ki")
        await asyncio.sleep(0.2)
        await event.edit("Support")
        await asyncio.sleep(0.5)
        await event.edit("Me")
        await asyncio.sleep(0.2)
        await event.edit("Dead")
        await asyncio.sleep(0.3)
        await event.edit("Boy")
        await asyncio.sleep(0.3)
        await event.edit("Hai😈😈")
        await asyncio.sleep(0.3)
        await event.edit("Shreya Ki Support Me Dead Boy Hai😈😈")
