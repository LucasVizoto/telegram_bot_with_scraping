from os import getenv
from dotenv import load_dotenv
load_dotenv()
from telebot import TeleBot

API_TOKEN = getenv('BOT_TOKEN')
bot = TeleBot(API_TOKEN)