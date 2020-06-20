"""Available Commands:

.shreya
.panga
.pro
.atti

@dead_boy_here"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd





@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "shreya":

        await event.edit(input_str)

        animation_chars = [
            "THE",
            "MOST",
            "BEAUTIFUL",
            "😍GIRL" ,
            "SHREYA",
            "IS",
            "MY",
            "OWNER❤️",
            "THE MOST BEAUTIFUL 😍GIRL SHREYA IS MY OWNER❤️"
         ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)
            
@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 10)

    input_str = event.pattern_match.group(1)

    if input_str == "panga":

        await event.edit(input_str)

        animation_chars = [
            "SHREYA",
            "SE",
            "AGAR",
            "LIYA" ,
            "PANGA",
            "TO",
            "HO",
            "JAYEGA",
            "DANGA😈",
            "SHREYA SE AGAR LIYA PANGA TO HO JAYEGA DANGA😈"
         ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval) 
            
@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "pro":

        await event.edit(input_str)

        animation_chars = [
            "YOU",
            "WERE",
            "PRO",
            "UNTILL",
            "I (SHREYA)",
            "ARRIVED",
            "😈",
            "YOU WERE PRO UNTILL I (SHREYA) ARRIVED 😈"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)  
            
@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "atti":

        await event.edit(input_str)

        animation_chars = [
            "APNA",
            "ATTITUDE",
            "APNI",
            "JEB",
            "ME",
            "RAKH",
            "😒",
            "APNA ATTITUDE APNI JEB ME RAKH 😒"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)                                
