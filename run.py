from src.integrations.telegram_comunicator import bot

import src.main.routes.help_command
import src.main.routes.scraping_commands
import src.main.routes.ai_commands

if __name__ == '__main__':
    print('The bot is runnig now!!')
    bot.polling()