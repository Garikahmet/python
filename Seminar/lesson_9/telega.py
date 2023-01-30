import os
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6167842182:AAGzTueC1J9bW7rJ2gScOTwCpIPqPbJfC9o").build()

app.add_handler(CommandHandler("hello", hello))
print('server start')
app.run_polling()

os.path.join(os.path.dirname(sys.argv[0]), 'telega.py')