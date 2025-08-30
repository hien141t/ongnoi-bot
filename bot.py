import os 
from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler 
TOKEN = "8319744629:AAEj75089dfC7SiwCYPtZoNAhe5TMjOFPR0" 
async def start(update: Update, context): 
    await update.message.reply_text("Bot is running!") 
app = ApplicationBuilder().token(TOKEN).build() 
app.add_handler(CommandHandler("start", start)) 
app.run_polling() 
