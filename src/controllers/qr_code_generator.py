from PIL.Image import Image
import qrcode

def qrcode_generator(text: str) -> Image:
    """
    Gera um QR Code a partir de um texto e salva como imagem PNG. 
    Posteriormnente, na própria rota, realiza a exclusão da imagem gerada.
    Pois justametne, após enviar ao usuário, não há mais necessidade de mantê-la no servidor.
    """
    img = qrcode.make(text) #gera um objeto com o hash payment
    img.save("qrcode.png")
    return img
