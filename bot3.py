# import telebot

# from telebot import types

# TOKEN ="7141465764:AAEqWQdR6yJcFcmv73w24Jqr3MQYIbdo8GY"

# bot = telebot.TeleBot(TOKEN)
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Информация про OKURMEN KIDS")
#     btn2 = types.KeyboardButton("Информация про курсы")
#     btn3 = types.KeyboardButton("Контакты")
#     markup.add(btn1, btn2, btn3,)
#     bot.send_message(message.chat.id, "Привет! Меню:", reply_markup=markup)

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.text == "Информация про OKURMEN KIDS":
#         bot.send_message(message.chat_id, "OKURMEN KIDS — это образовательный центр для детей. Мы предлагаем курсы по направлениям: frontend, backend, UI/UX дизайн.")
        
#     elif message.text == "Информация про курсы":
#         bot.send_message(message.chat.id, "Наш основной курс называется «Программатика». Он состоит из двух направлений:\n\n"
#                                           "- 🌐 Frontend: HTML, CSS, JavaScript\n"
#                                           "- 🐍 Python: основы, ООП, Telebot, Pygame, Django")

#     elif message.text == "Контакты":
#         inline_markup = types.InlineKeyboardMarkup()
#         instagram_btn = types.InlineKeyboardButton("📷 Instagram", url="https://www.instagram.com/okurmen_kids?igsh=bjQ5cW9wcW55bm9o")
#         tiktok_btn = types.InlineKeyboardButton("🎵 TikTok", url="https://www.tiktok.com/@okurmen_kids_?_t=ZS-8wSidOKb4oE&_r=1")
#         inline_markup.add(instagram_btn, tiktok_btn)
#         bot.send_message(message.chat.id, "📞 Телефон: +996 700 000 000\n📧 Email: info@example.com", reply_markup=inline_markup)

#     else:
#         bot.send_message(message.chat.id, "Пожалуйста, выберите пункт из меню.")


# bot.polling()


import telebot
from telebot import types

TOKEN = "7141465764:AAEqWQdR6yJcFcmv73w24Jqr3MQYIbdo8GY"

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Афиша")
    btn2 = types.KeyboardButton("Расписание")
    btn3 = types.KeyboardButton("Адрес")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Основное Меню:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Афиша":
        bot.send_message(message.chat.id, "Список фильмов:/n"
        "Dune 2:/n"
        "Oppenheimer:/n"
        "Inside Out 2")
    
    elif message.text == "Расписание":
        bot.send_message(message.chat.id, "Сегодня показы:/n"
        " Dune 2:14:00,19:00:/n"
        "Inside Out 2:16:30,21:00")
    
    elif message.text == "Адрес":
        inline_markup = types.InlineKeyboardMarkup()
        map_btn = types.InlineKeyboardButton("Открыть на карте", url="https://2gis.kg/bishkek/firm/70000001019352753")
        website_btn = types.InlineKeyboardButton("Сайт кинотеатра", url="https://manascinema.com/schedule")
        inline_markup.add(map_btn, website_btn)
        bot.send_message(message.chat.id, "Адрес Проспект Чынгыз Айтматова 47а", reply_markup=inline_markup)
    
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите пункт из меню.")

bot.polling()