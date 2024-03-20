import telebot

bot = telebot.TeleBot('6735142403:AAEck63-gTDZ7JDDD8i_yzKKEu0jjWdhs-s')

@bot.message_handler(commands=[ 'main'])
def main(message): 
    bot.send_message(message.chat.id, 'привет, ' + message.from_user.first_name)

bot.polling(none_stop=True)
