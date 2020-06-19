#Join @TeleBotHelp for custom plugins

from telethon import events
import subprocess
import asyncio
import time


@command(pattern="^.cmds", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**ʟɪsᴛ ᴏғ ᴘʟᴜɢɪɴs ɪɴ ᴅᴇᴀᴅʙᴏᴛ\nᴄᴜsᴛᴏᴍɪᴢᴇᴅ ғᴏʀ ᴏғғɪᴄɪᴀʟʟʏ ғᴏʀ sʜʀᴇʏᴀ\n\n**\n{o}\n\n**ᴛɪᴘ:** __ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋɴᴏᴡ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴀ ᴘʟᴜɢɪɴ, ᴅᴏ:-__ \n `. <plugin name>` **ᴡɪᴛʜᴏᴜᴛ ᴛʜᴇsᴇ < > ʙʀᴀᴄᴋᴇᴛs.**\n__ᴀʟʟ ᴘʟᴜɢɪɴs ᴍɪɢʜᴛ ɴᴏᴛ ᴡᴏʀᴋ ᴅɪʀᴇᴄᴛʟʏ..."
    await event.edit(OUTPUT)
