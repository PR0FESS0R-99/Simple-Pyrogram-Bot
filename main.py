from pyrogram import Client, filters


api_id = 13503794
api_hash = "7c5edb66000bcb12d914019f87bffed4"
bot_token = "5500972328:AAF8KG3bTj3ycmjEjpOg5Yo8oKivcrxnltI"

bot = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@bot.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)

print("bot started")
bot.run()
