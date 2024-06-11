import telebot
from telebot import types


bot = telebot.TeleBot(token='7175694691:AAGbBUhvNaKbC93_BSQynmzSeu5GCV_NAGo')


def main():
    @bot.message_handler(commands=['start'])  # декоратор, который получает значение ввиде команды \start
    def start(message):
        markup = types.ReplyKeyboardMarkup()  # создаю обьект на основе класса
        btn1 = types.KeyboardButton('/listen')  # основные кнопки бота
        btn2 = types.KeyboardButton('/add')
        btn3 = types.KeyboardButton('/view_all')
        btn4 = types.KeyboardButton('/options')
        markup.row(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, напиши /help', reply_markup=markup)
        # приветсвенное сообщение

if __name__ == '__main__':
    main()
    bot.polling()  # обращаюсь к методу обьекта bot, чтобы бот мог принимать сообщения и отправлять их