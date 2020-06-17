"""Available Commands:

.leg
.pro
.upro
.mepro

@arnab431"""

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

    if input_str == "leg":

        await event.edit(input_str)

        animation_chars = [
            "DEAD",
            "BOY",
            "IS",
            "THE" ,
            "DAD",
            "OF",
            "LEGENDS",
            "😈",
            "DEAD BOY IS THE DAD OF LEGENDS 😈"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)
            
@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "pro":

        await event.edit(input_str)

        animation_chars = [
            "DEAD",
            "BOY",
            "SE",
            "LIYA" ,
            "PANGA",
            "TO",
            "HO",
            "JAYEGA",
            "DANGA😈",
            "DEAD BOY SE LIYA PANGA TO HO JAYEGA DANGA😈"
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

    if input_str == "upro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "PeRu" ,
            "uNtiL",
            "YoU",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ PeRu uNtiL YoU aRriVe 😈"
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

    if input_str == "mepro":

        await event.edit(input_str)

        animation_chars = [
            "Everybody",
            "Was",
            "Pro" ,
            "Untill",
            "I",
            "Arrived",
            "😈",
            "Everybody Was Pro Untill I Arrived 😈"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)                                
