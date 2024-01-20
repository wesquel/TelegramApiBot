import telebot

api_key = "6591603757:AAFey7tU7H8uUapsxnY-bJvF2wpcmbVu-YE"

bot = telebot.TeleBot(api_key)

# Function to verify message
def verifify(msg):
    return True

# Function to handler with message in group of the bot.
@bot.message_handler(func=verifify)
def response(msg):
    bot.reply_to(msg, "Hello wolrd!")


# Continue chat function
bot.polling()
