import telebot
import google.generativeai as genai

TG_TOKEN = "8478495663:AAFNrD16EMR4j6lcVUZwRChmFQ7kzdDOYKo"
GEMINI_KEY = "AIzaSyCAz9ucF5TXFks8y6ZS6H_LvFh6gNERL2I"

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
