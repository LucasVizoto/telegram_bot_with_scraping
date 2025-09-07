from src.integrations.telegram_comunicator import bot
from src.controllers.scraping_news_g1 import scraping_five_recent_news_from_g1

@bot.message_handler(commands=['noticias', 'notícias', 'g1', 'G1'])
def send_scraping_with_five_news_from_g1_website(message):

    manchetes = scraping_five_recent_news_from_g1()
    try:
        for i, manchete in enumerate(manchetes[:5], 1):  # pega as 10 primeiras
            text = f"{i}. {manchete.get_text().strip()} \n  Link: {manchete['href']}"
            bot.reply_to(message, text)
    except Exception as e:
        print(str(e))