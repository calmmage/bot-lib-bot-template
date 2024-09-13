from aiogram import Dispatcher
from bot_lib import BotManager
from bot_lib.utils import create_bot
from dotenv import load_dotenv

from project_name.app import MyApp
from project_name.handler import MyHandler

load_dotenv()

app = MyApp()
bot_manager = BotManager(app=app)

dp = Dispatcher()

my_handler = MyHandler()
handlers = [my_handler]
bot_manager.setup_dispatcher(dp, extra_handlers=handlers)

bot = create_bot()

if __name__ == "__main__":
    app.run(dp, bot)
