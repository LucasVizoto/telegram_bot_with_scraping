from src.integrations.ai_comunicator import model

def conversation_ai_repository(user_message: str) -> str:

    gemini_response = model.generate_content(user_message)

    return gemini_response.text