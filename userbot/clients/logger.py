# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import TARO2, TARO3, TARO4, TARO5, bot, branch, tgbot
from userbot.utils import taroscrt

MSG_ON = """
✨**𝙺ιтαяσ-υѕєявσ𝚃 Berhasil Diaktifkan**!!
━━━━━━━━━━━━━━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}ping` **untuk Mengecheck Bot**
━━━━━━━━━━━━━━━
➠ **Powered By :** @ChannelKitaro
"""


async def taro_ubot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            TaroUBOT = await tgbot.get_me()
            BOT_USERNAME = TaroUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            TaroUBOT = await tgbot.get_me()
            BOT_USERNAME = TaroUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await taroscrt(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if TARO2:
            await taroscrt(TARO2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await TARO2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if TARO3:
            await taroscrt(TARO3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await TARO3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if TARO4:
            await taroscrt(TARO4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await TARO4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if TARO5:
            await taroscrt(TARO5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await TARO5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
