from telebot import TeleBot, types
from settings import TOKEN, ID_TECH

bot = TeleBot(token=TOKEN)

with open('ras.txt', 'w') as file:
    file = file.write('')

@bot.message_handler(['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("Обратиться за помощью к тех. поддержке")
    btn1 = types.KeyboardButton("Посмотреть уроки")
    btn3 = types.KeyboardButton("Изменить расписание")
    btn4 = types.KeyboardButton("Посмотреть документацию")
    markup.add(btn2, btn1, btn3, btn4)
    bot.send_message(message.chat.id, text='Привет, это бот помошник!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Обратиться за помощью к тех. поддержке':
        bot.send_message(message.chat.id, 'Введите вопрос!')
        bot.register_next_step_handler(message, question)

    elif message.text == 'Посмотреть уроки':
        with open('ras.txt', 'r') as file:
            file = file.read()

        if file == '':
            bot.send_message(message.chat.id, 'Расписания нет!')

        else:
            bot.send_message(message.chat.id, file)

    elif message.text == 'Изменить расписание':
        bot.send_message(message.chat.id, 'Введите новое расписание!')
        bot.register_next_step_handler(message, write_ras)

    elif message.text == 'Посмотреть документацию':
        bot.send_message(message.chat.id, 'Нажимайте нужные кнопки!')

def question(message):
    try:
        bot.send_message(ID_TECH, message.text)
        bot.send_message(message.chat.id, 'Сообщение успешно отправлено!')

    except:
        bot.send_message(message.chat.id, 'Произошла ошибка!')

def write_ras(message):
    with open('ras.txt', 'w') as file:
        file = file.write(message.text)

    bot.send_message(message.chat.id, 'Расписание изменено!')

bot.infinity_polling()