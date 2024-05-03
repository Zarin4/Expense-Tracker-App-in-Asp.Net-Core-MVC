import random
import telebot
from telebot import types

bot = telebot.TeleBot("7154834811:AAGT6-Isx4bwHvg_DOmoDFZL6KAm2Gu_48Y")

game = ["Камень", "Ножницы", "Бумага"]


#decorator - @bot.message_handler
@bot.message_handler(commands=['start'])
def handle_start(message):

  keyboard = types.ReplyKeyboardMarkup(True)
  button1 = types.KeyboardButton("Камень")
  button2 = types.KeyboardButton(text="Ножницы")
  button3 = types.KeyboardButton("Бумага")
  keyboard.add(button1, button2, button3)

  bot.send_message(message.chat.id,
                   "Привет, я бот - рандомайзер игры КНБ. Выбирай первым ход!",
                   reply_markup=keyboard)


#optimized handler for messages
def handle_message(message):
  random_object = random.choice(game)
  result = "Dead Heat!" if random_object == message.text else choose_result(
      random_object, message.text)
  bot.send_message(message.chat.id, random_object)
  bot.reply_to(message, result)


def choose_result(bot_choice, user_choice):
  if (bot_choice == "Камень" and user_choice == "Ножницы") or (
      bot_choice == "Ножницы"
      and user_choice == "Бумага") or (bot_choice == "Бумага"
                                       and user_choice == "Камень"):
    return "You lose!"
  elif (bot_choice == "Ножницы" and user_choice == "Камень") or (
      bot_choice == "Бумага"
      and user_choice == "Ножницы") or (bot_choice == "Камень"
                                        and user_choice == "Бумага"):
    return "You win!"
  else:
    return "Dead Heat!"


bot.message_handler(func=lambda message: True)(handle_message)
bot.polling(none_stop=True)

#обработчик сообщений @bot.message_handler(func=lambda message: True)
#def handle_message(message):

#random_object = random.choice(game)
#result = "Dead Heat!"

#if random_object == "Камень" and message.text == "Ножницы":
#result = "You lose!"
#elif random_object == "Камень" and message.text == "Бумага":
#result = "You win!"

#elif random_object == "Ножницы" and message.text == "Камень":
#result = "You win!"

#elif random_object == "Ножницы" and message.text == "Бумага":
#result = "You lose!"
#elif random_object == "Бумага" and message.text == "Камень":
#result = "You lose!"
#elif random_object == "Бумага" and message.text == "Ножницы":
#result = "You win!"

#else:
#result = "Dead Heat!"

#bot.send_message(message.chat.id, random_object)
#bot.reply_to(message, result)

#bot.polling(none_stop=True)

##Explanation of the code snippet:
# The provided code snippet defines a function called handle_message within the file.
# This function is responsible for processing incoming messages from users of a Telegram bot that plays the game "Rock, Paper, Scissors".
# Step-by-step breakdown:
# 1.Function definition:
# The function is defined using the def keyword followed by the function name handle_message and its parameter message.
# The parameter message represents the incoming message object from the Telegram bot API. This object contains information about the message, including its sender, text content, and other attributes.
# 2.Generating a random choice:
# Inside the function, the first line uses the
# method to randomly select an item from the game list. This list contains the three possible options in the Rock, Paper, Scissors game: "Камень" (Rock), "Ножницы" (Scissors), and "Бумага" (Paper). The selected item is stored in the variable random_object.
# 3. Determining the result:
# The next section of code checks the values of random_object and
# to determine the outcome of the game round. The logic is based on the standard rules of Rock, Paper, Scissors:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
# If both players choose the same option, it's a tie
# The if and elif statements compare the values of random_object and
# to determine the winner. If the player's choice beats the bot's choice, the result is set to "You win!". If the bot's choice beats the player's choice, the result is set to "You lose!". If both choices are the same, the result is set to "Dead Heat!".
# 4. Sending messages:
# After determining the result, the function uses the
# method to send two messages to the user:
# The first message reveals the bot's choice for the round, using the random_object value.
# The second message announces the result of the round, using the result value.
# 5.Function return:
# The handle_message function does not explicitly return a value. However, the
# calls within the function send the messages to the user, effectively completing the function's task.
# Additional notes:
# This code snippet relies on the telebot library for interacting with the Telegram bot API.
# The code uses Russian language for the game options and messages.
# The reply_to method in the handle_start function is not shown in the provided snippet but is likely used to reply to the user's initial "/start" command.
# Overall, this code demonstrates the implementation of a simple game bot using the telebot library. The bot interacts with users by sending messages and playing the Rock, Paper, Scissors game based on their choices.
