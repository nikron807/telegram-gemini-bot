import requests
import telebot

TG_TOKEN = "8478495663:AAFNrD16EMR4j6lcVUZwRChmFQ7kzdDOYKo"
YANDEX_API_KEY = "AQVN2mV0QKURgqpm-SAo0uP6wIap6VuKU3VMvE3g"  # Из Yandex Console
YOUR_AGENT_MODEL_URI = "gpt://b1gsj5o72kg4m5rtd69f/gpt-oss-120b/latest"  # ← ТВОЙ АГЕНТ!

bot = telebot.TeleBot(TG_TOKEN)

def ask_my_agent(text):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Authorization": f"Api-Key {YANDEX_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "modelUri": YOUR_AGENT_MODEL_URI,  # ← ТВОЙ АГЕНТ
        "messages": [{"role": "user", "text": text}],
        "completionOptions": {"temperature": 0.7, "maxTokens": 1000}
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        return response.json()['result']['alternatives'][0]['message']['text']
    except Exception as e:
        return f"Ошибка: {str(e)}"

@bot.message_handler(func=lambda m: True)
def reply(message):
    answer = ask_my_agent(message.text)
    bot.reply_to(message, answer)

bot.infinity_polling()
