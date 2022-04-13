# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, TARO2, TARO3, TARO4, TARO5):
    user_ids = list(SUDO_USERS) or []
    taro_id = await bot.get_me()
    user_ids.append(taro_id.id)

    try:
        if TARO2 is not None:
            id2 = await TARO2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if TARO3 is not None:
            id3 = await TARO3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if TARO4 is not None:
            id4 = await TARO4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if TARO5 is not None:
            id5 = await TARO5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MjA3Nzg0NjU1NQ==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        TARO_CLIENT = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        TARO_CLIENT = client.first_name
    taro_rpk = f"[{TARO_CLIENT}](tg://user?id={OWNER_ID})"
    return OWNER_ID, TARO_CLIENT, taro_rpk
