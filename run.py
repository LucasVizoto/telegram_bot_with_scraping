from src.drivers.telegram_comunicator import bot

import src.main.routes.help_command
import src.main.routes.scraping_commands

print('The bot is runnig now!!')
bot.polling()