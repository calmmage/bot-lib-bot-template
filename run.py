import asyncio
from dotenv import load_dotenv

load_dotenv()
from project_name.bot import bot, dp, app


if __name__ == "__main__":
    app.run(dp=dp, bot=bot)
