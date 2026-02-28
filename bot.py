
from telegram import Update
from telegram.ext import ApplicationBuilder , CommandHandler , MessageHandler , filters , ContextTypes
import requests

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke_data = r.json()
    await update.message.reply_text(joke_data['setup'] + '\n' + joke_data['punchline'])

TOKEN = '*******'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your Python bot')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    if 'hello' in user_text.lower():
        await update.message.reply_text('hello there!')
    else:
        await update.message.reply_text(f'You said: {user_text}')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Available commands: /start /help')

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start',start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(CommandHandler('joke', joke))
    print('Bot is running...')
    app.run_polling()
    
if __name__ == '__main__':
    main()
