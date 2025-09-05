from src.integrations.telegram_comunicator import bot

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message:str) -> None:
    text = 'Olá, este é um bot puramente para testes com a finalidade de ' \
    'desenvolver meu conhecimento técnico sobre a integração com o Telegram. \n' \
    'Fique a vontade para explorar qualque um dos comandos existentes.\n\n' \
    'Para mais detalhes, digite " / " e verifique a listagem.'
    
    bot.reply_to(message, text)

