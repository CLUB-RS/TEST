import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
API_TOKEN = '6390602037:AAFLqx3zspTs_dT2v8gKXKl4_kCcSgHtzbg'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Enable logging
logging.basicConfig(level=logging.INFO)

# Handler for forwarding messages to the group and replying to the user
@dp.message_handler(func=lambda message: True)
async def forward_and_reply(message: types.Message):
    user_id = message.from_user.id
    text = f"Sender ID: {user_id}\nMessage: {message.text}"

    # Replace 'YOUR_GROUP_ID' with your actual group ID
    await bot.send_message(chat_id='-1002028560989', text=text, parse_mode=ParseMode.MARKDOWN)

    # Reply to the user
    await message.reply_text("Your message has been received and forwarded!")

# Start the bot
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
