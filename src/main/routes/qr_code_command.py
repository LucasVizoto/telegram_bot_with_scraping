from src.integrations.telegram_comunicator import bot
from src.controllers.qr_code_generator import qrcode_generator

from os import remove

@bot.message_handler(commands=['qrcode', 'qr_code', 'qr'])
def send_qr_code_image(message: str) -> None:
    user_message = message.text.replace('/qrcode', '').replace('/qr_code', '').replace('/qr', '').strip()

    __validator_message(user_message)

    qrcode_generator(user_message)
    
    with open("qrcode.png", "rb") as qr_image:
        bot.send_photo(message.chat.id, qr_image)
    bot.reply_to(message, "Aqui está o seu QR Code!")
    remove("qrcode.png")



def __validator_message(message: str) -> bool:
    if not message:
        bot.send_message("Por favor, envie uma mensagem após o comando /qrcode.")
        return  #iterrompendo a execução do bot