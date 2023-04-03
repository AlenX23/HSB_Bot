from aiogram.types import PollAnswer
from aiogram import types
from aiogram.dispatcher import FSMContext
from dispatcher import dp, bot
from imex import export
from main import BotDB
from polls import poll, poll_6
from questions.interior_2 import in_poll
from questions.products_6 import pr_poll
from questions.service_5 import se_poll
from reply import st, nexT, lq
from statesform import UserInfo, Interior_2, Products_6, Service_5

x, g, inter, serv, prod = 0, 0, 0, 0, 0
y: str = '0'


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(message.from_user.id)
        export()

    await bot.send_message(message.chat.id,
                           f"{message.from_user.first_name}, готовы начать? Анкетирование займёт 15 минут.",
                           reply_markup=st)


@dp.message_handler(commands=["support"])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Агенты поддержки бота:\n"
                           f"При возникновении вопросов по технической части функционирования можете связаться со специалистом akha@sfedu.ru\n"
                           f"При возникновении вопросов по руководству пользования можете связаться с менеджером бота franchuk@sfedu.ru\n")


@dp.message_handler(commands=["commands"])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Приветствуем Вас, {message.from_user.first_name}, в правилах пользования чат-ботом:\n"
                           f"1. С самого начала во вкладке «меню» нажмите /start.\n"
                           f"2. После появления на экране области, выберите ту, которая соответсвует местоположению предприятия, которое Вы посетили и хотели бы оценить.\n"
                           f"3. Выберите специализацию предприятия сферы сервиса.\n"
                           f"4. Выберите вид предприятия сферы сервиса, исходя из его специализации.\n"
                           f"5. Из отображаемых предприятий выберете то, которое Вы посетили (обращайте внимание на адрес организации/заведения).\n"
                           f"6. Введите ФИО или пройдите анкету анонимно.\n"
                           f"7. Приступайте к анкетированию (для перехода к следующему вопросу нажмите «далее»; при совершении ошибки в предыдущем вопросе нажмите «назад»).\n"
                           f"8. По завершении прохождения анкеты убедитесь в корректности ответов и нажмите «готово».)\n")


@dp.message_handler(content_types=["text"], state=None)
async def main_menu(message: types.Message):
    global x, y, g, inter, serv, prod

    if message.text == "Начать анкетирование!":
        x, g, inter, serv, prod = 0, 0, 0, 0, 0
        await send_poll_main(message, poll[x], nexT)

    if message.text == "Далее" and x < len(poll) and y == '23':
        x += 1
        await send_poll_main(message, poll[x], nexT)
        y = ''
    elif message.text == "Назад" and x < len(poll):
        y = ''
        await send_poll_main(message, poll[x], nexT)

    if x == 5:
        UserInfo.user_info[0] = 'Ростовская область' if UserInfo.user_info[0] == '0' else 'другая'
        UserInfo.user_info[1] = 'Ростов-на-Дону' if UserInfo.user_info[1] == '0' else 'другой'
        UserInfo.user_info[2] = 'предприятие общественного питания' if UserInfo.user_info[2] == '0' else 'другая'
        UserInfo.user_info[3] = 'кофейня' if UserInfo.user_info[3] == '0' else 'другое'
        UserInfo.user_info[4] = 'Пить кофе. Адрес: Ворошиловский пр., 91/1' if UserInfo.user_info[4] == '0' else 'другое'

        await send_poll_dop(message, poll_6, nexT)
        x = 6

    # НАЧАЛО ОПРОСА ПО РАЗДЕЛАМ
    if x == 7:
        UserInfo.blocks = str(UserInfo.blocks).replace('0', '')
        if inter < len(in_poll):
            g = 1
            if message.text == "Далее":
                await send_poll_main(message, in_poll[inter], nexT)
            elif message.text == "Назад":
                if inter == 0:
                    await send_poll_main(message, in_poll[inter], nexT)
                else:
                    inter -= 1
                    await send_poll_main(message, in_poll[inter], nexT)

    if x == 8:
        UserInfo.blocks = str(UserInfo.blocks).replace('1', '')
        if serv < len(se_poll):
            g = 2
            if message.text == "Далее":
                await send_poll_main(message, se_poll[serv], nexT)
            elif message.text == "Назад":
                if serv == 0:
                    await send_poll_main(message, se_poll[serv], nexT)
                else:
                    serv -= 1
                    await send_poll_main(message, se_poll[serv], nexT)

    if x == 9:
        UserInfo.blocks = str(UserInfo.blocks).replace('2', '')
        if prod < len(pr_poll):
            g = 3
            if message.text == "Далее":
                await send_poll_main(message, pr_poll[prod], nexT)
            elif message.text == "Назад":
                if prod == 0:
                    await send_poll_main(message, pr_poll[prod], nexT)
                else:
                    prod -= 1
                    await send_poll_main(message, pr_poll[prod], nexT)

    if g == 10:
        await bot.send_message(message.chat.id,
                               "Вы успешно справились с анкетой! Ваше мнение очень важно для нас. До следующих встреч!",
                               reply_markup=lq)

        if UserInfo.result == '0':
            BotDB.add_questionnaire2(UserInfo.user_id, UserInfo.user_info[0], UserInfo.user_info[1],
                                     UserInfo.user_info[2],
                                     UserInfo.user_info[3], UserInfo.user_info[4], Interior_2.interior_2[0],
                                     Interior_2.interior_2[1], Interior_2.interior_2[2],
                                     Interior_2.interior_2[3], Interior_2.interior_2[4],
                                     '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                                     '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-')

        if UserInfo.result == '01':
            BotDB.add_questionnaire2(UserInfo.user_id, UserInfo.user_info[0], UserInfo.user_info[1],
                                     UserInfo.user_info[2],
                                     UserInfo.user_info[3], UserInfo.user_info[4], Interior_2.interior_2[0],
                                     Interior_2.interior_2[1], Interior_2.interior_2[2],
                                     Interior_2.interior_2[3], Interior_2.interior_2[4],
                                     Service_5.service_5[0], Service_5.service_5[1], Service_5.service_5[2],
                                     Service_5.service_5[3], Service_5.service_5[4], Service_5.service_5[5],
                                     Service_5.service_5[6], Service_5.service_5[7], Service_5.service_5[8],
                                     Service_5.service_5[9], Service_5.service_5[10], Service_5.service_5[11],
                                     Service_5.service_5[12],
                                     '-', '-', '-', '-', '-', '-', '-', '-', '-', '-')

        if UserInfo.result == '02':
            BotDB.add_questionnaire2(UserInfo.user_id, UserInfo.user_info[0], UserInfo.user_info[1],
                                     UserInfo.user_info[2],
                                     UserInfo.user_info[3], UserInfo.user_info[4], Interior_2.interior_2[0],
                                     Interior_2.interior_2[1], Interior_2.interior_2[2],
                                     Interior_2.interior_2[3], Interior_2.interior_2[4],
                                     '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                                     Products_6.products_6[0], Products_6.products_6[1], Products_6.products_6[2],
                                     Products_6.products_6[3], Products_6.products_6[4], Products_6.products_6[5],
                                     Products_6.products_6[6], Products_6.products_6[7], Products_6.products_6[8],
                                     Products_6.products_6[9])

        if UserInfo.result == '012':
            BotDB.add_questionnaire2(UserInfo.user_id, UserInfo.user_info[0], UserInfo.user_info[1],
                                     UserInfo.user_info[2], UserInfo.user_info[3], UserInfo.user_info[4],
                                     Interior_2.interior_2[0],
                                     Interior_2.interior_2[1], Interior_2.interior_2[2],
                                     Interior_2.interior_2[3], Interior_2.interior_2[4],
                                     Service_5.service_5[0], Service_5.service_5[1], Service_5.service_5[2],
                                     Service_5.service_5[3], Service_5.service_5[4], Service_5.service_5[5],
                                     Service_5.service_5[6], Service_5.service_5[7], Service_5.service_5[8],
                                     Service_5.service_5[9], Service_5.service_5[10], Service_5.service_5[11],
                                     Service_5.service_5[12],
                                     Products_6.products_6[0], Products_6.products_6[1], Products_6.products_6[2],
                                     Products_6.products_6[3], Products_6.products_6[4], Products_6.products_6[5],
                                     Products_6.products_6[6], Products_6.products_6[7], Products_6.products_6[8],
                                     Products_6.products_6[9])

        if UserInfo.result == '1':
            BotDB.add_questionnaire2(UserInfo.user_id, UserInfo.user_info[0], UserInfo.user_info[1],
                                     UserInfo.user_info[2],
                                     UserInfo.user_info[3], UserInfo.user_info[4], '-', '-', '-', '-', '-',
                                     Service_5.service_5[0], Service_5.service_5[1], Service_5.service_5[2],
                                     Service_5.service_5[3], Service_5.service_5[4], Service_5.service_5[5],
                                     Service_5.service_5[6], Service_5.service_5[7], Service_5.service_5[8],
                                     Service_5.service_5[9], Service_5.service_5[10], Service_5.service_5[11],
                                     Service_5.service_5[12], '-', '-', '-', '-', '-', '-', '-', '-', '-', '-')

        if UserInfo.result == '12':
            BotDB.add_questionnaire2(UserInfo.user_id, UserInfo.user_info[0], UserInfo.user_info[1],
                                     UserInfo.user_info[2],
                                     UserInfo.user_info[3], UserInfo.user_info[4], '-', '-', '-', '-', '-',
                                     Service_5.service_5[0], Service_5.service_5[1], Service_5.service_5[2],
                                     Service_5.service_5[3], Service_5.service_5[4], Service_5.service_5[5],
                                     Service_5.service_5[6], Service_5.service_5[7], Service_5.service_5[8],
                                     Service_5.service_5[9], Service_5.service_5[10], Service_5.service_5[11],
                                     Service_5.service_5[12],
                                     Products_6.products_6[0], Products_6.products_6[1], Products_6.products_6[2],
                                     Products_6.products_6[3], Products_6.products_6[4], Products_6.products_6[5],
                                     Products_6.products_6[6], Products_6.products_6[7], Products_6.products_6[8],
                                     Products_6.products_6[9])

        if UserInfo.result == '2':
            BotDB.add_questionnaire2(UserInfo.user_id, UserInfo.user_info[0], UserInfo.user_info[1],
                                     UserInfo.user_info[2],
                                     UserInfo.user_info[3], UserInfo.user_info[4], '-', '-', '-', '-', '-', '-', '-',
                                     '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                                     Products_6.products_6[0], Products_6.products_6[1], Products_6.products_6[2],
                                     Products_6.products_6[3], Products_6.products_6[4], Products_6.products_6[5],
                                     Products_6.products_6[6], Products_6.products_6[7], Products_6.products_6[8],
                                     Products_6.products_6[9])
        g = 11

    if message.text == "Скачать файл с отзывами":
        await send_welcome(message)


@dp.poll_answer_handler()
async def handler_poll_answer(p: PollAnswer):
    global x, y, g, serv, inter, prod
    UserInfo.user_id = p['user']['id']

    if x < len(poll):
        y = '23'
        UserInfo.user_info[x] = str(p.option_ids).strip('[]')
        if x == 4:
            x = 5

    if x == 6:
        UserInfo.blocks = str(p.option_ids).strip('[]').replace(',', '').replace(' ', '')
        UserInfo.result = UserInfo.blocks
        if UserInfo.blocks == '0' or UserInfo.blocks == '01' or UserInfo.blocks == '02' or UserInfo.blocks == '012':
            x = 7
        elif UserInfo.blocks == '1' or UserInfo.blocks in '12':
            x = 8
        elif UserInfo.blocks == '2':
            x = 9

    if g == 1:
        Interior_2.interior_2[inter] = str(p.option_ids).strip('[]')
        inter += 1
        if inter == 5 and (UserInfo.blocks == '1' or UserInfo.blocks == '12'):
            x = 8
        elif inter == 5 and UserInfo.blocks == '2':
            x = 9
        elif inter == 5 and UserInfo.blocks == '':
            g = 10

    if g == 2:
        Service_5.service_5[serv] = str(p.option_ids).strip('[]')
        serv += 1
        if serv == 13 and UserInfo.blocks == '2':
            x = 9
        elif serv == 13 and UserInfo.blocks in '':
            g = 10

    if g == 3:
        Products_6.products_6[prod] = str(p.option_ids).strip('[]')
        prod += 1
        if prod == 10:
            g = 10
dp.register_poll_answer_handler(handler_poll_answer)


# ВЫВОД ОПРОСА
@dp.message_handler()
async def send_poll_main(message: types.Message, poll, button):
    await bot.send_poll(chat_id=message.chat.id, question=poll.question, options=poll.options, type=poll.type,
                        is_anonymous=False, reply_markup=button)
async def send_poll_dop(message: types.Message, poll, button):
    await bot.send_poll(chat_id=message.chat.id, question=poll.question, options=poll.options, type=poll.type,
                        is_anonymous=False, allows_multiple_answers=True, reply_markup=button)


# ОТПРАВКА ФАЙЛА
@dp.message_handler(commands=["file"])
async def send_welcome(message: types.Message):
    export()
    f = open("result.xlsx", "rb")
    await bot.send_document(message.chat.id, f)
