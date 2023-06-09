import logging
from aiogram import Bot, Dispatcher
from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not config.BOT_TOKEN:
    exit("No token provided")


#proxy_url = 'http://proxy.server:3128'
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")#, proxy=proxy_url)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# activate filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)
