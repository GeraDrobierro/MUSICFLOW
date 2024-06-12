import telebot
from telebot import types
import sqlite3  # Импортирую библиотеку для работы с БД


bot = telebot.TeleBot(token='7175694691:AAGbBUhvNaKbC93_BSQynmzSeu5GCV_NAGo')
name = None  # переменная, в которой будут храниться значения с названием аудиофайла
artist = None  # переменная, в которой будут храниться значения с названием артиста


def main():
    @bot.message_handler(commands=['help'])  # Создал декоратор, который принимает в себя команду /help
    def help_info(message):
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('/listen')  # Это основные кнопки бота
        btn2 = types.KeyboardButton('/add')
        btn3 = types.KeyboardButton('/view_all')
        btn4 = types.KeyboardButton('/options')
        markup.row(btn1, btn2, btn3, btn4)
        file = open('help.txt', 'r') 
        # Создаю переменную file и присваиваю ей файловый объект с режимом доступа только для чтения
        k = file.read()  # переменной k передаем метод считывания данных из файла
        bot.send_message(message.chat.id, f'{k}', reply_markup=markup)  
        # бот отправляет сообщение с текстом и выводит кнопки на экран 
        file.close()  # закрываю файл
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

    @bot.message_handler(['add'])
    def song_name(message):
        conn = sqlite3.connect('music.sql')  # создаю обьект на основе класса sqlite3, т.е. создаю БД
        cur = conn.cursor()  # Создаю курсор для работы с БД

        cur.execute('CREATE TABLE IF NOT EXISTS loadings '
                    '(id int auto_increment primary key, name varchar(50), artist varchar(50))')
        # создаю таблицу с атрибутами name, artist и первичным ключом id
        conn.commit()  # обращаюсь к БД с нашим запросом
        cur.close()  # закрываю курсор
        conn.close()  # закрываю БД

        bot.send_message(message.chat.id, 'Введи название песни')
        bot.register_next_step_handler(message, naming)  # перенаправляю бота выполнить следующую функцию

    def naming(message):  # функция для 'регистрации' имени трека
        global name  # обьявляю переменную name как глобальную

        bot.send_message(message.chat.id, 'отправь аудио')
        name = message.text  # бот регистрирует название с сообщения пользователя

        bot.register_next_step_handler(message, save_audio)

    @bot.message_handler(content_types=['audio'])  # декоратор, который приниимает как значение аудиофайл
    def save_audio(message):  # функция сохранения аудиофайла в БД
        try:
            global name  # обьявляю переменную name, artist как глобальную
            global artist

            artist = message.audio.performer
            # обращаюсь к методу обьекта message, в котором хранится инф. о исполнителе

            audio_file_id = message.audio.file_id  # переменная, в которой храниться id сообщения
            audio_file = bot.get_file(audio_file_id)  # переменная, которая представляет собой полученный файл
            audio_file_path = audio_file.file_path

            audio_name = f"/ВАШ_ПУТЬ_К_ПАПКЕ_/MUSIC/{name}.mp3"

            audio_data = bot.download_file(audio_file_path)

            with open(audio_name, 'wb') as file:  # Открытие файла для записи в двоичном режиме
                file.write(audio_data)  # Запись данных аудиофайла в файл

            conn = sqlite3.connect('music.sql')
            cur = conn.cursor()

            cur.execute('INSERT INTO loadings (name, artist) VALUES ("%s", "%s")' % (name, artist))
            # Выполнение SQL-запроса для добавления информации об аудиофайле в БД
            conn.commit()
            cur.close()
            conn.close()

            markup = types.InlineKeyboardMarkup()
            bot.delete_message(message.chat.id, message.message_id)  # Удаление сообщения с аудиофайлом
            markup.add(types.InlineKeyboardButton('Весь плейлист', callback_data='loadings'))
            # Добавление кнопки к клавиатуре и вызываю функцию loadings
            bot.send_message(message.chat.id, 'Трек добавлен', reply_markup=markup)
        except AttributeError:  # обработка исключения, если сообщение не является аудиофайлом
            bot.send_message(message.chat.id, 'Друг, похоже ты отправил мне не аудиофайл. Отправь мне аудио, пожалуйста')

    @bot.callback_query_handler(func=lambda callback: True)  # Декоратор для обработки callback-запросов
    def callback_message(callback):  # Функция, которая будет вызываться при callback-запросах

        conn = sqlite3.connect('music.sql')
        cur = conn.cursor()

        cur.execute('SELECT * FROM loadings')
        loadings = cur.fetchall()

        info = ''   # Переменная для хранения информации о треках
        for i in loadings:
            info += f'Название трека:{i[1]}, Исполнитель: {i[2]}\n'  # Формирование строки информации о треке
        cur.close()
        conn.close()
        bot.send_message(callback.message.chat.id, info)  # Отправка сообщения с информацией о треках в чат

        
if __name__ == '__main__':
    main()
    bot.polling()  # обращаюсь к методу обьекта bot, чтобы бот мог принимать сообщения и отправлять их