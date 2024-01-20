import telebot

api_key = "6591603757:AAFey7tU7H8uUapsxnY-bJvF2wpcmbVu-YE"

bot = telebot.TeleBot(api_key)

# Define an inline keyboard with two buttons
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.add(telebot.types.InlineKeyboardButton("Button 1", url="https://www.google.com"))
keyboard.add(telebot.types.InlineKeyboardButton("Button 2", callback_data="button2"))

# Function to verify message
def verify(msg):
    return True

# Function to handle messages with the inline keyboard
@bot.message_handler(func=verify)
def response(msg):
    print(msg)
    # Send a message with the inline keyboard
    message = bot.send_message(msg.chat.id, "Hello world!", reply_markup=keyboard)
    # Edit the message with the inline keyboard
    bot.edit_message_text("Hello world again!", msg.chat.id, message.message_id, reply_markup=keyboard)

# Function to handle callback queries from the inline keyboard
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    print(call)
    # Send a message to the user who clicked the button
    bot.send_message(call.from_user.id, f"You clicked {call.data}")

# Continue chat function
bot.polling()
