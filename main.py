import telebot
from telebot import types

bot = telebot.TeleBot('6735142403:AAEck63-gTDZ7JDDD8i_yzKKEu0jjWdhs-s')

access_granted = False  # Изначально у пользователя нет доступа

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Crypto_step", url="https://t.me/my_crypto_step")
    button2 = types.InlineKeyboardButton(text="Проверить подписку", callback_data="check_subscription")
    keyboard.add(button1)
    keyboard.add(button2)
    
    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, "Здравствуйте, {}! Если вы ищите фильмы, сначала подпишитесь на канал".format(message.from_user.first_name), reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)   
def callback_query(call):
    global access_granted 
    access_granted = False
    if call.data == "check_subscription":
        user_id = call.from_user.id
        chat_id = "@my_crypto_step"
        status = ['creator', 'administrator', 'member']
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status in status:
            bot.send_message(call.message.chat.id, "Доступ открыт для пользователя")
            access_granted = True
            bot.send_message(call.message.chat.id, "Пожалуйста, введите код фильма:")
        else:
            bot.send_message(call.message.chat.id, "Для доступа к поиску фильмов подпишитесь на канал Crypto_step")
            

@bot.message_handler(func=lambda message: access_granted)
def handle_movie_code(message):
    if message.text == "333":
        bot.send_message(message.chat.id, "Иди на хуй!")
    else:
        movie_code = message.text
        bot.send_message(message.chat.id, f"Вы ввели несуществующий код: {movie_code}")

@bot.message_handler(func=lambda message: not access_granted)
def handle_invalid_access(message):
    bot.send_message(message.chat.id, "Для доступа к поиску фильмов подпишитесь на канал Crypto_step")

bot.polling(none_stop=True)
