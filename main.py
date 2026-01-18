import requests
import telebot

# ВРЕМЕННО ВСТАВЛЯЕШЬ КЛЮЧИ ПРЯМО В КОД (только для теста!)
TG_TOKEN = "8478495663:AAFyB2_HSQK0EwApJvCyxFMYWcBys0sXtKE"
API_KEY = "AQVN2mV0QKURgqpm-SAo0uP6wIap6VuKU3VMvE3g"  # ТОТ ЧТО ТЫ СОЗДАЛ
FOLDER_ID = "b1gsj5o72kg4m5rtd69f"

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
