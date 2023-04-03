import sqlite3


class BotDB:

    def __init__(self, db_file):
        """"ИНИЦИАЛИЗАЦИЯ СОЕДИНЕНИЯ С БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, user_id):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_questionnaire2(self, user_id, area, city, specialization, company_type, company_address, comfort_musical_accompaniment, comfort_lighting, comfort_air_temperature,
                           convenience_space_organization, comfort_smell, meeting_guest_entrance,
                           choose_table, quickly_waiter_came, quickly_menu_served, waiter_dessert_drink_,
                           waiter_specify_submission_items, waiter_give_advice_choice_dishes,
                           waiting_drink_served, waiting_dessert_served, how_quickly_bill_brought,
                           cash_receipt_brought, waiter_ask_drink_dessert,
                           say_goodbye_when_leaving, breadth_range_drinks, breadth_dessert_assortment, appearance_drink,
                           dessert_appearance, matching_temperature_drink,
                           aroma_drink, taste_drink, dessert_taste, possibility_individualization_order,
                           availability_lean_menu):
        """"СОЗДАЕМ ОПРОСНИК"""
        self.cursor.execute(
            "INSERT INTO 'questionnaire' ('user_id', 'area', 'city', 'specialization', 'company_type', 'company_address', 'comfort_musical_accompaniment', 'comfort_lighting', 'comfort_air_temperature', 'convenience_space_organization', 'comfort_smell', 'meeting_guest_entrance', "
            "'choose_table', 'quickly_waiter_came', 'quickly_menu_served', 'waiter_dessert_drink_', 'waiter_specify_submission_items', 'waiter_give_advice_choice_dishes', "
            "'waiting_drink_served', 'waiting_dessert_served', 'how_quickly_bill_brought', 'cash_receipt_brought', 'waiter_ask_drink_dessert',"
            "'say_goodbye_when_leaving', 'breadth_range_drinks', 'breadth_dessert_assortment', 'appearance_drink', 'dessert_appearance', 'matching_temperature_drink',"
            "'aroma_drink', 'taste_drink', 'dessert_taste', 'possibility_individualization_order', 'availability_lean_menu') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, area, city, specialization, company_type, company_address, comfort_musical_accompaniment, comfort_lighting, comfort_air_temperature, convenience_space_organization,
             comfort_smell, meeting_guest_entrance, choose_table, quickly_waiter_came, quickly_menu_served,
             waiter_dessert_drink_, waiter_specify_submission_items, waiter_give_advice_choice_dishes,
             waiting_drink_served, waiting_dessert_served, how_quickly_bill_brought, cash_receipt_brought,
             waiter_ask_drink_dessert, say_goodbye_when_leaving, breadth_range_drinks, breadth_dessert_assortment,
             appearance_drink, dessert_appearance, matching_temperature_drink, aroma_drink, taste_drink, dessert_taste,
             possibility_individualization_order, availability_lean_menu))
        return self.conn.commit()

    def close(self):
        """"ЗАКРЫТИЕ СОЕДИНЕНИЯ С БД"""
        self.conn.close()
