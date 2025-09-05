from src.integrations.telegram_comunicator import bot
from src.controllers.ai_conversation import conversation_ai_repository

@bot.message_handler(commands=['ai', 'AI', 'Ai'])
def ai_command(message: str):
    user_message = message.text.replace('/ai', '').replace('/AI', '').replace('/Ai', '').strip()

    if not user_message:
        bot.reply_to(message, "Por favor, envie uma mensagem após o comando /ai.")
    
    text_response = conversation_ai_repository(user_message)
    bot.reply_to(text_response)