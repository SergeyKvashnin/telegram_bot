import telebot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import date, datetime
from spy import *


async def hi_command(update: Update, context: ContextTypes):
    log(update, context)
    if update.effective_user.first_name == 'Vasiliy' or update.effective_user.first_name == 'Василий':
        await update.message.reply_text(f'Дароу {update.effective_user.first_name}! \nВася, по братски, смени аватар в дискорде')
    else:
        await update.message.reply_text(f'Дароу {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')

async def time_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'{datetime.now()}')

async def sum_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def pr_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

