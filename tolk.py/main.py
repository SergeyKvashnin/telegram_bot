from turtle import update
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from bots_commands import *

app = ApplicationBuilder().token("5332444779:AAGRXdMD3k6AL43JegIzTfyGfi1GWdzarzk").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("pr", pr_command))
app.run_polling()


