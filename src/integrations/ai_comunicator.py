import google.generativeai as genai
from os import getenv

from config.gemini_infos import gemini_infos

api_key = gemini_infos['API_KEY']
google_model = gemini_infos['MODEL']

genai.configure(api_key=api_key)

# Escolha o modelo
model = genai.GenerativeModel(google_model)
