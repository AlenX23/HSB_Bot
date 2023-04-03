from aiogram import executor
from dispatcher import dp
from db import BotDB
import handlers
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "reviews.db")
BotDB = BotDB(db_path)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
