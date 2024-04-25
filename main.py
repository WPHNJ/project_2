import logging
from telegram.ext import Application, MessageHandler, filters
from config import BOT_TOKEN
from telegram.ext import CommandHandler
from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup
from datetime import datetime
from data import db_session
from data.users import User


import requests


locality = []

locality_city_game = []

di = {}

dt1 = datetime.now()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['/address', '/phone'],
                  ['/site', '/work_time']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard1 = [['/reg', '/login']]

markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=False)


async def start(update, context):
    await update.message.reply_text(
        "Здравствуйте!\n"
        "Пожалуйста, выбирите, вы хотите войти или зарегестрироваться?",
        reply_markup=markup1
    )
    return 1


async def reg_name(update, context):
    await update.message.reply_text(
        "Введите имя"
    )
    return 1


async def reg_surname(update, context):
    global locality
    locality.append(update.message.text)
    await update.message.reply_text(
        "Введите фамилию"
    )
    return 2


async def reg_email(update, context):
    global locality
    if len(locality) < 2:
        locality.append(update.message.text)
    await update.message.reply_text(
        "Введите email"
    )
    return 'next'


async def reg_email_3(update, context):
    print(1)
    await update.message.reply_text(
        "Введите email"
    )
    return 'next'


async def reg_email_2(update, context):
    k = update.message.text
    print(str(k)[-10:], k, locality, len(str(k)), 898989)
    if len(str(k)) > 10:
        if "@gmail.com" == str(k)[-10:]:
            locality.append(k)
            print(locality)
            await update.message.reply_text(
                "Ведите что-нибудь для подтверждения"
            )
            return 3
    elif k == locality[-1]:
        pass
    else:
        await update.message.reply_text(
            "Неверный формат почты"
        )
        await update.message.reply_text(
            "Введите что-нибудь"
        )

        print(188)
        return 'next_next'
    locality.append(k)
    return 3


async def reg_password(update, context):
    global locality
    await update.message.reply_text(
        "Введите пароль"
    )
    locality.append(update.message.text)
    return 4


async def reg_end(update, context):
    global locality
    locality.append(update.message.text)
    print(locality)
    user = User()
    user.name = locality[0]
    user.surname = locality[1]
    user.email = locality[2]
    user.password = locality[3]
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    locality.append(update.message.text)
    await update.message.reply_text(
        "Регистрация окончена, подтвердите это"
    )
    return 5


async def login_name(update, context):
    await update.message.reply_text(
        "Введите имя"
    )
    return 1


async def login_surname(update, context):
    global locality
    locality.append(update.message.text)
    await update.message.reply_text(
        "Введите фамилию"
    )
    return 2


async def login_email(update, context):
    global locality
    locality.append(update.message.text)
    await update.message.reply_text(
        "Введите email"
    )
    return 'next'


async def login_email_3(update, context):
    print(1)
    await update.message.reply_text(
        "Введите email"
    )
    return 'next'


async def login_email_2(update, context):
    k = update.message.text
    print(str(k)[-10:], k, locality, len(str(k)), 898989)
    if len(str(k)) > 10:
        if "@gmail.com" == str(k)[-10:]:
            locality.append(k)
            print(locality)
            await update.message.reply_text(
                "Ведите что-нибудь для подтверждения"
            )
            return 3
    elif k == locality[-1]:
        pass
    else:
        await update.message.reply_text(
            "Неверный формат почты"
        )
        await update.message.reply_text(
            "Введите что-нибудь"
        )

        print(188)
        return 'next_next'
    locality.append(k)
    return 3


async def login_password(update, context):
    global locality
    locality.append(update.message.text)
    await update.message.reply_text(
        "Введите пароль"
    )
    return 4


async def login_end(update, context):
    global locality
    locality.append(update.message.text)
    db_sess = db_session.create_session()
    if len(list(db_sess.query(User).filter(User.name == locality[0], User.surname == locality[1],
                                           User.email == locality[2], User.password == locality[3],
                                           User.email.notilike("%1%")))) != 0:
        await update.message.reply_text(
            "Успешно, подтвердите это"
        )
    else:
        await update.message.reply_text(
            "Не успешно"
        )
        return
    return 5


async def entered(update, context):
    await update.message.reply_text(
        "Введите команду"
    )
    k = str(update.message.text)
    print(k)

    if k == 'ping':
        return 6
    if k == 'help':
        return 7
    if k == 'yandex':
        return 8
    if k == 'work_time':
        print(1)
        return 9
    if k == 'download_picture':
        return 10
    if k == 'city_game':
        global locality_city_game
        locality_city_game = []
        return 12
    if k == 'start':
        return 1
    if k == 'stop':
        return 13


async def stop(update, context):
    await update.message.reply_text(
        "Остановлено"
    )
    return ConversationHandler.END


async def help_command(update, context):
    await update.message.reply_text(
        "ping - выводит pong\n"
        "help - выводит это\n"
        "yandex - выводит ссылку на сайт яндекса\n"
        "work_time - показывает время работы программы\n"
        "download_picture - скачивает и выводит картинку с карт\n"
        "city_game - игра в города"
    )
    return 5


async def site(update, context):
    await update.message.reply_text(
        "Сайт: https://ya.ru/"
    )
    return 5


async def ping(update, context):
    await update.message.reply_text(
        "pong"
    )
    return 5


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def work_time(update, context):
    dt2 = datetime.now()
    timedelta = dt2 - dt1
    await update.message.reply_text(
        f"Время работы: {str(timedelta)[:-7]}"
    )
    return 5


async def picture_download(update, context):
    await update.message.reply_text(
        "Введите координаты места, которое хотите увидеть через пробел"
    )
    return 11


async def picture_download_2(update, context):
    global locality
    locality.append(update.message.text)
    get_image(locality[-1])
    await update.message.reply_text(
        "Ищу картинку"
    )
    print(11)
    await context.bot.send_photo(
        update.message.chat_id,


        'picture.png',
        caption="Нашёл:"
    )
    return 5


def get_image(text):
    print(text.split())
    response = requests.get(f'http://static-maps.yandex.ru/1.x/?ll={str(text).split()[0]},{str(text).split()[1]}&spn=0'
                            f'.002,0.002&l=map')

    if not response:
        return 'error'

    map_file = "picture.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


def file_read(file_name):
    f = open(f"{file_name}", 'r')
    data = f.read().split('\n')
    f.close()
    return data


def first_letter(li):
    global di
    for i in li:
        if i[0] not in di:
            di[i[0]] = [i]
        else:
            temp = di[i[0]]
            temp.append(i)
            di[i[0]] = temp


async def city_game(update, context):
    if len(locality_city_game) < 1:
        await update.message.reply_text(
            "Введите город"
        )

    first_letter(file_read('cities.txt'))
    locality_city_game.append(update.message.text)
    if locality_city_game[-1] == 'сдаюсь':
        return 5
    if len(locality_city_game) > 1:
        if locality_city_game[-1][0].upper() not in di:
            print(locality_city_game[-1][0].upper())
            await update.message.reply_text(
                "Я не знаю такого города"
            )

        elif locality_city_game[-1] not in di[locality_city_game[-1][0].upper()]:
            await update.message.reply_text(
                "Я не знаю такого города"
            )

        else:
            if locality_city_game[-1][-1].upper() in di and len(locality_city_game) > 1:
                for i in di[locality_city_game[-1][-1].upper()]:
                    if i not in locality_city_game:
                        await update.message.reply_text(
                            i
                        )
                        break

                    else:
                        await update.message.reply_text(
                            "Сдаюсь"
                        )

                        return 5
            else:
                await update.message.reply_text(
                    "Сдаюсь"
                )

                return 5


def main():

    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('reg', reg_name)],

        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, reg_surname)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, reg_email)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, reg_password)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, reg_end)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, entered)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, ping)],
            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, help_command)],
            8: [MessageHandler(filters.TEXT & ~filters.COMMAND, site)],
            9: [MessageHandler(filters.TEXT & ~filters.COMMAND, work_time)],
            'next': [MessageHandler(filters.TEXT & ~filters.COMMAND, reg_email_2)],
            'next_next': [MessageHandler(filters.TEXT & ~filters.COMMAND, reg_email_3)],
            10: [MessageHandler(filters.TEXT & ~filters.COMMAND, picture_download)],
            11: [MessageHandler(filters.TEXT & ~filters.COMMAND, picture_download_2)],
            12: [MessageHandler(filters.TEXT & ~filters.COMMAND, city_game)],
            13: [MessageHandler(filters.TEXT & ~filters.COMMAND, stop)]
        },

        fallbacks=[CommandHandler('stop', stop), CommandHandler('entered', entered)]
    )
    application.add_handler(conv_handler)

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('login', login_name)],

        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, login_surname)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, login_password)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, login_email)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, login_end)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, entered)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, ping)],
            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, help_command)],
            8: [MessageHandler(filters.TEXT & ~filters.COMMAND, site)],
            9: [MessageHandler(filters.TEXT & ~filters.COMMAND, work_time)],
            'next': [MessageHandler(filters.TEXT & ~filters.COMMAND, login_email_2)],
            'next_next': [MessageHandler(filters.TEXT & ~filters.COMMAND, login_email_3)],
            10: [MessageHandler(filters.TEXT & ~filters.COMMAND, picture_download)],
            11: [MessageHandler(filters.TEXT & ~filters.COMMAND, picture_download_2)],
            12: [MessageHandler(filters.TEXT & ~filters.COMMAND, city_game)],
            13: [MessageHandler(filters.TEXT & ~filters.COMMAND, stop)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler)

    application.add_handler(CommandHandler("start", start))

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

    db_session.global_init("db/users.db")

    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
