from pyrogram import Client,filters,enums
from pyrogram.handlers import MessageHandler
import asyncio




#bot=Client('Bot')

#@bot.on_message(filters.command('start'))
#def start(bot,msg):
 #   bot.send_message(msg.chat.id,"hello there !")


from pyrogram import Client

api_id = 13503794
api_hash = "7c5edb66000bcb12d914019f87bffed4"

admin = [5329205911,5559099357]


bot = Client("my_account", api_id=api_id, api_hash=api_hash)

@bot.on_message(filters.command('start'))
def start(bot,msg):
    bot.send_message(msg.chat.id,"Hey ! ")
    


#@bot.on_message(filters.text | filters.sticker | filters.voice |filters.contact | filters.web_page | filters.animation | filters.mentioned)
#def delete_text(bot,msg):
    #if msg.from_user.id != 5329205911:
        #bot.delete_messages(msg.chat.id,msg.id)
        #bot.send_message(msg.chat.id,"Chats are not allowed ! Only Media")
             

       




@bot.on_message(filters.video | filters.photo | filters.document )
async def start(bot,msg):
     await bot.copy_message(-1001126475746,msg.chat.id,msg.id)
     await asyncio.sleep(1)
     #await bot.delete_messages(msg.chat.id,msg.id) 
     



    
      
@bot.on_message(filters.text | filters.sticker | filters.voice |filters.contact | filters.web_page | filters.animation | filters.mentioned)
def delete_text(bot,msg):
    if msg.from_user.id in admin:
        None
    else:
        #bot.send_message(msg.chat.id,"Chats are not allowed ! Only Media")
        bot.delete_messages(msg.chat.id,msg.id)
    
        
        








bot.run()