"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
JARVIS_IS_ALIVE = ("**J.A.R.VI.S.** IS ALWAYS ONLINE ✔️\n\n"
                   "**I am Always Alive To Help You Boss**\n\n"
                   "**❌Currently Status❌** : `No Issue Found`\n\n"
                   "**❌Python Version❌** : `3.8`\n\n"
                   "**❌JARVIS OS❌** : `3.0 Snapdragon `\n\n"
                   "**❌Current Sat❌** : `SIDDARTHASat-2.0`\n\n"
                   "**❌My Boss❌** : {DEFAULTUSER} \n\n"
                   "**❌License❌** : [MIT Licence](https://github.com/sairam1103/JARVISUSERBOT//blob/master/LICENSE)\n\n"
                   "**❌Copyright❌** : By [SAIRAM1103@Github](GitHub.com/SAIRAM1103)\n\n"
                   "` 🔹 Bot created by:` [Siddartha](tg://user?id=1211918189)\n"
                   " [⌨︎Deploy JarvisUserbot⌨︎](https://telegra.ph/JARVIS-07-02)") 


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_message(chat, JARVIS_IS_ALIVE) 
