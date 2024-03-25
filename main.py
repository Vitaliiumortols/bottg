import telebot
from telebot import types

bot = telebot.TeleBot('6735142403:AAEck63-gTDZ7JDDD8i_yzKKEu0jjWdhs-s')


@bot.message_handler(commands=['start'])

def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Crypto_step", url = "https://t.me/my_crypto_step" )
    button2 = types.InlineKeyboardButton(text="проверить подписку", callback_data="button_pressed")
    keyboard.add(button1)
    keyboard.add(button2)
    
    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, "Здравствуйте " + message.from_user.first_name + ", Если вы ищите фильмы, то сначала подпишитесь на канал", reply_markup=keyboard)



bot.polling(none_stop=True)
