from aiogram.types import Poll, PollType

pr_poll_1 = Poll(
    question="Широта ассортимента напитков. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

pr_poll_2 = Poll(
    question="Широта ассортимента десертов. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

pr_poll_3 = Poll(
    question="Внешний вид напитка. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

pr_poll_4 = Poll(
    question="Внешний вид десерта. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

pr_poll_5 = Poll(
    question="Соответствие температуры напитка. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

pr_poll_6 = Poll(
    question="Аромат напитка. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

pr_poll_7 = Poll(
    question="Вкус напитка. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

pr_poll_8 = Poll(
    question="Вкус десерта. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

pr_poll_9 = Poll(
    question="Возможность индивидуализации заказа",
    options=["да", "нет"],
    type=PollType.REGULAR
)

pr_poll_10 = Poll(
    question="Наличие постного меню",
    options=["да", "нет"],
    type=PollType.REGULAR
)

pr_poll = [pr_poll_1, pr_poll_2, pr_poll_3, pr_poll_4, pr_poll_5, pr_poll_6, pr_poll_7, pr_poll_8,
           pr_poll_9, pr_poll_10]
