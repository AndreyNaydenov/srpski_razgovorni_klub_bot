import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from questions import QUESTIONS
from config import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Here are the available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/get - Get a random question for a discussion\n"
        "/source - Get a link to the source code"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ćao! Kako si?")

async def get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    random_question = random.choice(QUESTIONS)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=random_question)

async def source(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Source code: https://github.com/AndreyNaydenov/srpski_razgovorni_klub_bot"
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    help_handler = CommandHandler('help', help_command)
    start_handler = CommandHandler('start', start)
    get_handler = CommandHandler('get', get)
    source_handler = CommandHandler('source', source)
    application.add_handler(help_handler)
    application.add_handler(start_handler)
    application.add_handler(get_handler)
    application.add_handler(source_handler)
    
    application.run_polling()
