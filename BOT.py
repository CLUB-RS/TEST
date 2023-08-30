import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6644443558:AAH9i1vvLli1YXE0cocYdhhCeI0tTRujX50'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("IP info"))
    keyboard.add(types.KeyboardButton("Button 2"))
    keyboard.add(types.KeyboardButton("Button 3"))
    keyboard.add(types.KeyboardButton("Button 4"))
    return keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    await message.reply(f"Hello, {user.first_name}! I'm your bot. How can I help you?",
                        reply_markup=main_keyboard())

@dp.message_handler(lambda message: message.text == "IP info")
async def ask_for_ip(message: types.Message):
    await message.reply("Please input your IP address:")

@dp.message_handler(lambda message: is_valid_ip(message.text))
async def handle_ip_info(message: types.Message):
    ip = message.text
    ip_info = get_ip_info(ip)
    await message.reply(ip_info,
                        reply_markup=main_keyboard())

def is_valid_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    ip_info = (
        f"IP: {data['ip']}\n"
        f"Hostname: {data.get('hostname', 'N/A')}\n"
        f"City: {data.get('city', 'N/A')}\n"
        f"Region: {data.get('region', 'N/A')}\n"
        f"Country: {data.get('country', 'N/A')}\n"
        f"Location: {data.get('loc', 'N/A')}\n"
        f"Postal Code: {data.get('postal', 'N/A')}\n"
        f"Organization: {data.get('org', 'N/A')}"
    )
    return ip_info

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
