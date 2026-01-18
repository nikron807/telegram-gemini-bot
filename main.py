import os
import requests
import telebot

# Используй переменные окружения
TG_TOKEN = os.getenv("TG_TOKEN")
API_KEY = os.getenv("YANDEX_API_KEY")
FOLDER_ID = os.getenv("FOLDER_ID")

bot = telebot.TeleBot(TG_TOKEN)

def ask_yandex_gpt(text):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt-lite",
        "messages": [{"role": "user", "text": text}],
        "completionOptions": {"temperature": 0.7}
    }
    response = requests.post(url, json=payload, headers=headers)
    try:
        return response.json()['result']['alternatives'][0]['message']['text']
    except:
        return "Ошибка запроса"

@bot.message_handler(func=lambda m: True)
def reply(message):
    answer = ask_yandex_gpt(message.text)
    bot.reply_to(message, answer)

bot.infinity_polling()
