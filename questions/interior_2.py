from aiogram.types import Poll, PollType

in_poll_1 = Poll(
    question="Комфортность музыкального сопровождения. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

in_poll_2 = Poll(
    question="Комфортность освещения. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

in_poll_3 = Poll(
    question="Комфортность температуры воздуха. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

in_poll_4 = Poll(
    question="Удобство организации пространства. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

in_poll_5 = Poll(
    question="Комфортность запаха. Оцените по 5-ти балльной шкале (где 1 – низший балл, а 5 – высший балл)",
    options=["1", "2", "3", "4", "5"],
    type=PollType.REGULAR
)

in_poll = [in_poll_1, in_poll_2, in_poll_3, in_poll_4, in_poll_5]
