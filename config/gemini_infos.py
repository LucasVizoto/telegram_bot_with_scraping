from dotenv import load_dotenv
from os import getenv

load_dotenv()

gemini_infos = {
    'API_KEY': getenv('GOOGLE_API_KEY'),
    'MODEL': getenv('GOOGLE_MODEL')
}