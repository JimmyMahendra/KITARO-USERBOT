from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, jim_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@jim_cmd(pattern='d(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**DARAH GUA SAMA DARAH LU BEDA, KAN LU DARAH NYA CUPU GA ADA NYALI**")


@jim_cmd(pattern='e(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**EEELAAHH DEK DEK MENDING JANGAN DISINI CAPER NYA GAUSA BELAGU KONTOL**")


@jim_cmd(pattern='f(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**FUCK MEN ANJAYY KERENN BET YA INGGRIS GUA**")


@jim_cmd(pattern='i(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**INI LAH BOCAH GOBLOG GA PUNYA OTAK SAKSIKAN LAH!!**")


@jim_cmd(pattern='r(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**RANDOM SEKALI YA EPRIBADII DASAR PENJILAT!!**")


@jim_cmd(pattern='t(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**TERLENA SAYA LIAT TYPINGAN MU DEEK TERHARU SEKALI SEGITU NYA MENCERITAKAN DIRI SENDIRI**")


@jim_cmd(pattern='u(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**UNTUK MU YANG LAGI DUDUK SAMBIL DISKUSI, WKWKW DISKUSI DENGAN NGEBACOT GITU? GOBLOK**")


@jim_cmd(pattern='w(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**WAH ADA PETAROENK NGEERIIII **")


@jim_cmd(pattern='z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**MUKA LU ITU MIRIP KATAK ZUMA TAU GA LU? JELEK BET ANJG HAHAHA!!**")


@jim_cmd(pattern='k(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**KONTOL GAYA² DOANG TERNYATA..!!**")


@jim_cmd(pattern='n(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**NANTI GIMANA KALO KITA BAKAL JODOH? AWW SOSWIT**")


@jim_cmd(pattern='b(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**BHAKS KOCAK KALI KAU!!**")


@jim_cmd(pattern='m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**MELIHAT ORANG² YANG GA TAU DI UNTUNG!!**")


@jim_cmd(pattern='c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**CIH, HARAM KAMU PERGI SANA JANGAN DEKAT DEKAT!!**")


@jim_cmd(pattern='s(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**SAMA AKU AJA PACARANNYA MAU GA?**")


@jim_cmd(pattern='v(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**VARIASI INI SANGAT LAH TIDAK JELAS!!**")


@jim_cmd(pattern='j(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**JADI LAH ORANG SPESIAL DIHIDUP KU (TAPI BOONG)**")


@jim_cmd(pattern='a(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**AKU, RAJA MEKSIKO, ELMATADORE SALVADOR TEQUILA EL KONTOLLE **")


@jim_cmd(pattern='g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**GA MASUK DI AKAL BET ANJG**")


@jim_cmd(pattern='y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**YAA DAH SELALU BENAR...**")


@jim_cmd(pattern='h(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**HAHAHAH KENA MENTAL YA DEK? KASIAN YA**")


@jim_cmd(pattern='o(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**O AJA SI**")


@jim_cmd(pattern='1(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**NORAK LU KONTOL!!**")


CMD_HELP.update({
    "toxic":
    f"{cmd}d\
\nUsage: lihat sendiri.\
\n\n{cmd}e\
\nUsage: lihat sendiri.\
\n\n{cmd}f\
\nUsage: lihat sendiri.\
\n\n{cmd}i\
\nUsage: lihat sendiri.\
\n\n{cmd}r\
\nUsage: lihat sendiri.\
\n\n{cmd}t\
\nUsage: lihat sendiri.\
\n\n{cmd}u\
\nUsage: lihat sendiri.\
\n\n{cmd}w\
\nUsage: lihat sendiri.\
\n\n{cmd}z\
\nUsage: lihat sendiri.\
\n\n{cmd}k\
\nUsage: lihat sendiri.\
\n\n{cmd}n\
\nUsage: lihat sendiri.\
\n\n{cmd}b\
\nUsage: lihat sendiri.\
\n\n{cmd}m\
\nUsage: lihat sendiri.\
\n\\{cmd}c\
\nUsage: lihat sendiri.\
\n\n{cmd}s\
\nUsage: lihat sendiri.\
\n\n{cmd}v\
\nUsage: lihat sendiri.\
\n\n{cmd}a\
\nUsage: lihat sendiri.\
\n\n{cmd}j\
\nUsage: lihat sendiri.\
\n\n{cmd}g\
\nUsage: lihat sendiri.\
\n\n{cmd}y\
\nUsage: lihat sendiri.\
\n\n{cmd}h\
\nUsage: lihat sendiri.\
\n\n{cmd}o\
\nUsage: lihat sendiri.\
\n\n{cmd}1\
\nUsage: lihat sendiri."
})
