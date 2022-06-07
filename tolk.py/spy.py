import telebot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import date, datetime

def log(update: Update, context: ContextTypes):
    file = open('db.csv', 'a')
    file.write(f'{datetime.now()}, {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text} \n \n')
    file.close
    
