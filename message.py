import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize the bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Handler for forwarding messages to the group and replying to the user
def forward_and_reply(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    text = f"Sender ID: {user_id}\nMessage: {update.message.text}"

    # Replace 'YOUR_GROUP_ID' with your actual group ID
    context.bot.send_message(chat_id='YOUR_GROUP_ID', text=text, parse_mode='Markdown')

    # Reply to the user
    update.message.reply_text("Your message has been received and forwarded!")

# Register the handler
message_handler = MessageHandler(Filters.text & ~Filters.command, forward_and_reply)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()
