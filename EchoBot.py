import telebot

TOKEN = "1942025448:AAHGxLtxa1DP_G_y5Wo93vaYtECmIU64MFM"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands = ["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Hi, I am Discorama Bot")

@bot.message_handler(func = lambda message:True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
