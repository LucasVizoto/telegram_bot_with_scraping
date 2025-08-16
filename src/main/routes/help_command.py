from src.drivers.telegram_comunicator import bot
from src.repositories.soma import somatoria
import requests

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message:str) -> None:
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    bot.reply_to(message, text)

@bot.message_handler(commands=['soma'])
def send_soma(message):
    text = somatoria()
    bot.reply_to(message,text) 
