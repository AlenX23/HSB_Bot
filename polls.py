from aiogram.types import Poll, PollType, PollOption

poll_1 = Poll(
    question="Выберите область:",
    options=["Ростовская область", "другая"],
    type=PollType.REGULAR,
)

poll_2 = Poll(
    question="Выберите город, предприятие которого Вы бы хотели оценить:",
    options=["Ростов-на-Дону", "другой"],
    type=PollType.REGULAR,
)

poll_3 = Poll(
    question="Выберите специализацию предприятия сферы сервиса:",
    options=["предприятие общественного питания", "другая"],
    type=PollType.REGULAR,
)

poll_4 = Poll(
    question="Выберите вид предприятия:",
    options=["кофейня", "другое"],
    type=PollType.REGULAR,
)

poll_5 = Poll(
    question="Выберите нужное предприятие:",
    options=["Пить кофе. Адрес: Ворошиловский пр., 91/1", "другое"],
    type=PollType.REGULAR,
)

poll_6 = Poll(
    question="Выберите, какой из блоков Вы бы хотели оценить:",
    options=["Интерьер", "Обслуживание", "Продукция"],
    type=PollType.REGULAR,
)

poll = [poll_1, poll_2, poll_3, poll_4, poll_5]
