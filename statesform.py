from aiogram.dispatcher.filters.state import State, StatesGroup


class UserInfo(StatesGroup):
    user_id = State()
    area = State()
    city = State()
    specialization = State()
    company_type = State()
    company_address = State()
    blocks = State()
    result = State()
    user_info = [area, city, specialization, company_type, company_address]


class Interior_2(StatesGroup):
    q_1 = State()
    q_2 = State()
    q_3 = State()
    q_4 = State()
    q_5 = State()
    interior_2 = [q_1, q_2, q_3, q_4, q_5, q_5]


class Service_5(StatesGroup):
    q_1 = State()
    q_2 = State()
    q_3 = State()
    q_4 = State()
    q_5 = State()
    q_6 = State()
    q_7 = State()
    q_8 = State()
    q_9 = State()
    q_10 = State()
    q_11 = State()
    q_12 = State()
    q_13 = State()
    service_5 = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10, q_11, q_12, q_13, q_13]


class Products_6(StatesGroup):
    q_1 = State()
    q_2 = State()
    q_3 = State()
    q_4 = State()
    q_5 = State()
    q_6 = State()
    q_7 = State()
    q_8 = State()
    q_9 = State()
    q_10 = State()
    products_6 = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10, q_10]
