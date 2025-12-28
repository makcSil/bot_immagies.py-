mport random
import telebot
import os

API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет! Я бот помощник помогаю решить проблему с загрязнением"
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(
        message,
        "Команды бота:\n"
        "/create - одна поделка из бытового пластика"
    )

@bot.message_handler(commands=['horror'])
def send_horror(message):
    img_name = random.choice(os.listdir("images"))
    with open(f"images/{img_name}", "rb") as f:
        bot.send_photo(message.chat.id, f)

bot.polling()
