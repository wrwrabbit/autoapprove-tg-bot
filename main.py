from os import environ
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

bot=Client("Automatic approve bot", bot_token = environ["BOT_TOKEN"], api_id = int(environ["API_ID"]), api_hash = environ["API_HASH"])

@bot.on_chat_join_request()
async def autoapprove(client: bot, message: ChatJoinRequest):
    chat=message.chat
    user=message.from_user
    print(f"A user joined {chat.id}")
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
   
print("Bot is up")
bot.run()
