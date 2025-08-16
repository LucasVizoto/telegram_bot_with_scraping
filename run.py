from src.drivers.telegram_comunicator import bot

import src.main.routes.help_command

print('The bot is runnig now!!')
bot.polling()