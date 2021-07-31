
import telebot

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip() 

bot = telebot.TeleBot(TOKEN)  

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "¿Me ha llamado maestro?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()

