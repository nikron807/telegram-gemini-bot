import telebot
import google.generativeai as genai
import os

os.environ['HTTPS_PROXY'] = os.getenv('HTTPS_PROXY', '')

TG_TOKEN = os.getenv("TG_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")

bot = telebot.TeleBot(TG_TOKEN)
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Gemini готов!")

@bot.message_handler(func=lambda m: True)
def reply(message):
    try:
        resp = model.generate_content(message.text)
        bot.reply_to(message, resp.text[:4096])
    except Exception as e:
        bot.reply_to(message, f"❌ {str(e)}")

bot.infinity_polling()
