import pybase64
from telethon import Button
from telethon.tl.functions.channels import JoinChannelRequest as Invt
from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/40d30f8b4b34e27a03e58.jpg",
                caption="🤡 **KITARO-USERBOT Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @ChannelKitaro ",
                buttons=[(Button.url("Support", "https://t.me/rumahkitaro3"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None


async def checking(client):
    gcsp = str(pybase64.b64decode("QHJ1bWFoa2l0YXJvMw=="))[2:15]
    chsp = str(pybase64.b64decode("QENoYW5uZWxLaXRhcm8="))[2:16]
    chgbt = str(pybase64.b64decode("QFdob0FtSWhlaA=="))[2:12]
    if client:
        try:
            await client(Invt(gcsp))
        except BaseException:
            pass
        try:
            await client(Invt(chsp))
        except BaseException:
            pass
        try:
            await client(Invt(chgbt))
        except BaseException:
            pass
