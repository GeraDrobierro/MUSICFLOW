# MusicBot "MUSICFLOW"

## ВСТУПЛЕНИЕ
Телеграмм бот "MUSICFLOW". Мы создали этого бота, чтобы прослушивание музыки для пользователя стало более удобным и уменьшило количество платных подписок. 

Как работает наш бот? Всё просто, вам необходимо найти желанный аудиофйал и отправить его боту. Далее он сохранит его в вашем плейлисте с тем название, каким вы захотите. 
Как только вы пожелаете послушать музыку, то вам надо будет просто написать название своего трека, и бот отправит вам аудиофайл.

## БИБЛИОТЕКИ
Чтобы в полном объёме реализовать функционал бота, нам необходима библиотека, которая позволит работать с мессенджером "Telegram". Для этого мы будем использовать библиотеку [telebot](https://pypi.org/project/pyTelegramBotAPI/0.3.0/). 
Чтобы реализовать возможность сохранять, изменять и удалять музыкальные файлы, будем использовать библиотеку [sqlite3](https://docs.python.org/3/library/sqlite3.html), которая предоставит нам доступ к возможности создать базу данных о музыке пользователя. 
Для работы с аудиофайлами непосредственно на сервере мы используем библиотеку [os](https://docs.python.org/3/library/os.html).
Для подробного ознакомления с каждой из библиотек, предлагаем перейти по ссылке, нажав на название интересующей вас библиотеки выше.

## УСТАНОВКА НЕОБХОДИМЫХ БИБЛИОТЕК

Чтобы скачать библиотеки, необходимо открыть терминал компьютера и в нём написать

```
pip install telebot
```
os, sqlite3 - являются установленными по умолчанию библиотеками.

## ПОДГОТОВИТЕЛЬНЫЕ ДЕЙСТВИЯ
Перед тем как использовать бота, вам необходимо получить токен и создать своего Telegram бота. Как это сделать рассказано [здесь](https://docs.radist.online/radist.online-docs/nashi-produkty/radist-web/podklyucheniya/telegram-bot/instrukciya-po-sozdaniyu-i-nastroiki-bota-v-botfather).

Создайте новый проект в выбранной вами среде разработки. Затем создайте папку **MUSIC** в папке, в которой будет храниться проект. В эту папку будут сохраняться все ваши аудиозаписи.

Также добавьте в ваш проект следующие текстовые файлы:

1. `validation.txt` - текст, который будет выводиться в чате при вводе пользователем данных неизвестного типа.
2. `help.txt` - текст, который будет выводиться при вызове команды `/help`.

## ФУНКЦИОНАЛ БОТА
Чтобы начать работу с ботом достаточно в диалоге с ним прописать команду `/start`, тогда вам будет предоставлен ознакомительный текст. Если вы новый пользователь и не знаете, как работает бот, то вы можете прописать команду `/help`, и вам будет доступен весь функционал бота. 

Разберемся, за что отвечает каждая из команд:

1. `/add` - эта команда позволяет добавить вам новый трек в ваш плейлист. После применения этой команды, вам будет предложено ввести название трека и отправить сам аудиофайл для дальнейшего сохранения в вашем плейлисте.

2. `/listen` - эта команда позволяет вам слушать музыку из вашего плейлиста. После применения этой команды, бот попросит вас выбрать один из треков в вашем плейлисте, и как только вы напишите название, которое указали при загрузке, бот отправит вам требуемый аудиофайл.

3. `/view_all` - эта команда позволяет вам ознакомиться со всем вашим плейлистом, то есть посмотреть все загруженные ранее треки.

4. `/options` - эта команда напрвлена на взаимодейтсвие с вашим плейлистом. Если вы хотите изменить название трека или удалить его, то при применении команды `/options`, вам будет предложено две новые команды `/delete` и `/edit`. Команда `/edit` позволит вам исправить название трека, а команда `/delete` - удалить трек из вашего плейлиста по названию.

## КОД
Сначала импортируем необходимые нам библиотеки, чтобы мы могли с ними работать
```python
import telebot
import sqlite3
from telebot import types
import os
```

## ПОЛНЫЙ КОД
В файле `main.py` прописан весь код, необходимый для корректной работы бота. Если вы выполнили все предыдущие шаги, запустите код и наслаждайтесь вашей любимой музыкой, а если вы захотите расширить функционал вашего музыкального бота, то можете править код и дополнить его нужными вам функциями. Приятного прослушивания!