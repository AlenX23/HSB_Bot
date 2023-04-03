from aiogram.types import Poll, PollType

se_poll_1 = Poll(
    question="Как происходила встреча гостя на входе? ",
    options=["персонал поздоровался с улыбкой", "персонал поздоровался без улыбки", "персонал не поздоровался"],
    type=PollType.REGULAR
)

se_poll_2 = Poll(
    question="Предложили выбрать столик?",
    options=["да", "нет"],
    type=PollType.REGULAR,
)

se_poll_3 = Poll(
    question="Как быстро подошёл официант?",
    options=["до 3 минут", "от 3 до 5 минут", "дольше 5 минут"],
    type=PollType.REGULAR
)

se_poll_4 = Poll(
    question="Как быстро подали меню?",
    options=["до 3 минут", "от 3 до 5 минут", "дольше 5 минут"],
    type=PollType.REGULAR
)

se_poll_5 = Poll(
    question="Предложил ли официант десерт к напитку?",
    options=["да", "нет"],
    type=PollType.REGULAR
)

se_poll_6 = Poll(
    question="Уточнил ли официант очередность подачи позиций заказа?",
    options=["да", "нет"],
    type=PollType.REGULAR
)

se_poll_7 = Poll(
    question="Дал ли официант совет по выбору блюд? (по запросу тайного покупателя)",
    options=["дал очень подробный совет", "дал скорее подробный совет", "дал скорее неподробный", "не дал совета в выборе блюд"],
    type=PollType.REGULAR
)

se_poll_8 = Poll(
    question="Ожидание подачи напитка",
    options=["до 5 минут", "от 5 до 10 минут", "более 10 минут"],
    type=PollType.REGULAR
)

se_poll_9 = Poll(
    question="Ожидание подачи десерта",
    options=["до 5 минут", "от 5 до 10 минут", "более 10 минут"],
    type=PollType.REGULAR
)

se_poll_10 = Poll(
    question="Как быстро был принесен счет?",
    options=["до 5 минут", "от 5 до 10 минут", "более 10 минут"],
    type=PollType.REGULAR
)

se_poll_11 = Poll(
    question="Был ли принесен кассовый чек?",
    options=["да", "нет"],
    type=PollType.REGULAR
)

se_poll_12 = Poll(
    question="Спросил ли официант, понравился ли напиток/десерт?",
    options=["да", "нет"],
    type=PollType.REGULAR
)

se_poll_13 = Poll(
    question="Попрощался ли с вами персонал при выходе из кафе?",
    options=["да", "нет"],
    type=PollType.REGULAR
)

se_poll = [se_poll_1, se_poll_2, se_poll_3, se_poll_4, se_poll_5, se_poll_6, se_poll_7, se_poll_8, se_poll_9,
           se_poll_10, se_poll_11, se_poll_12, se_poll_13]
