from pyrogram import Client, filters
import asyncio


api_id = 13503794
api_hash = "7c5edb66000bcb12d914019f87bffed4"
bot_token = "5500972328:AAF8KG3bTj3ycmjEjpOg5Yo8oKivcrxnltI"

admin = [5329205911,5559099357]

bot = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


@bot.on_message(filters.command('start'))
def start(bot,msg):
    bot.send_message(msg.chat.id,"Hey ! ")




@bot.on_message(filters.video | filters.photo | filters.document )
async def start(bot,msg):
     await bot.copy_message(-1001751906984,msg.chat.id,msg.id)
     await bot.copy_message(-1001607224684,msg.chat.id,msg.id)
     await asyncio.sleep(1)
     await bot.delete_messages(msg.chat.id,msg.id) 
    



print("bot started")
bot.run()
