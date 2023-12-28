import telebot
import time
from telebot import types
import parser

token = '6975511818:AAFPvo8Ku-UH71-oblVS2bWC5EzkyRFQLZk'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    while True:
        print(parser.parserpy())
        print('парсер завершен через мейн')
        new_info = parser.parserpy()
        for i in new_info:
            msg_msg = "\n".join(i)
            print(msg_msg,f'otprav v tg')
            bot.send_message(message.chat.id,'http://cab2.ru/sched.php',msg_msg)
bot.infinity_polling()