# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import sys

from telethon.utils import get_peer_id

from userbot import BOT_TOKEN
from userbot import BOT_VER as version
from userbot import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    TARO2,
    TARO3,
    TARO4,
    TARO5,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_SESSION,
    taroblacklist,
    bot,
    call_py,
    tgbot,
)
from userbot.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nKITARO-USERBOT v{}, Copyright © 2021-2022 KITARO <https://github.com/Kitaroo/KITARO-USERBOT>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU."


async def taro_clients(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multiclienttaro():
    if 2077846555 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001489233533 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 2077846555 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(taro_clients(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in taroblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_2:
        try:
            TARO2.start()
            LOOP.run_until_complete(taro_clients(TARO2))
            user = TARO2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in taroblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            TARO3.start()
            LOOP.run_until_complete(taro_clients(TARO3))
            user = TARO3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in taroblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            TARO4.start()
            LOOP.run_until_complete(taro_clients(TARO4))
            user = TARO4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in taroblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            TARO5.start()
            LOOP.run_until_complete(taro_clients(TARO5))
            user = TARO5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in taroblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    return failed
