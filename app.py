import telebot
from utils import create_buttons, get_equipment, send_equipment
from constants import token

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "xd")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if('+' in message.text):

        equipmentVariants = get_equipment(message.text)
        response_keyboard = create_buttons(equipmentVariants)

        bot.reply_to(message, 'Оборудование би лайк: ' + str(message.text.split(" ")), reply_markup=response_keyboard)


@bot.callback_query_handler(func=lambda callback: True)
def handle_equipment(callback):

    # бот отправляет сообщение с выбранным оборудованием
    bot.send_message(callback.message.chat.id, callback.data)
    send_equipment(callback.data)
    return

bot.infinity_polling()

