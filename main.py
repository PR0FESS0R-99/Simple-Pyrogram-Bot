from pyrogram import Client,filters,enums
from pyrogram.handlers import MessageHandler
import asyncio


api_id = 13503794
api_hash = "7c5edb66000bcb12d914019f87bffed4"
bot_token = "5600997688:AAG_8tBfLx4XOXorGSaXBNt521NKMI2l_nI"

admin = [5329205911,5559099357]

bot = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


@bot.on_message(filters.command('start'))
def start(bot,msg):
    bot.send_message(msg.chat.id,"Hey ! ")




@bot.on_message(filters.video  | filters.document )
async def start(bot,msg):
     await asyncio.sleep(120)
     await bot.copy_message(-1001733967564,msg.chat.id,msg.id)
     await bot.copy_message(-1001755298903,msg.chat.id,msg.id)
     await bot.delete_messages(msg.chat.id,msg.id)

@bot.on_message(filters.photo )
async def start(bot,msg):
     #await bot.copy_message(-1001733967564,msg.chat.id,msg.id)
     await bot.copy_message(-1001755298903,msg.chat.id,msg.id)
     await asyncio.sleep(10800)
     await bot.delete_messages(msg.chat.id,msg.id)
  

@bot.on_message(filters.animation)
async def del_filt(bot,msg):
     await asyncio.sleep(120)
     await bot.delete_messages(msg.chat.id,msg.id)



@bot.on_message( filters.web_page)
async def service_msg(bot,msg):
     await asyncio.sleep(1)
     await bot.delete_messages(msg.chat.id,msg.id) 
    


print("bot started")
bot.run()
