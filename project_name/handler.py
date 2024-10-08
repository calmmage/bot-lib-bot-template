from aiogram.types import Message

from bot_lib import Handler, HandlerDisplayMode
from project_name.app import MyApp


class MyHandler(Handler):
    name = "main"
    display_mode = HandlerDisplayMode.FULL
    commands = {
        "dummy_command_handler": "dummy_command",
    }

    has_chat_handler = True

    async def chat_handler(self, message: Message, app: MyApp, **kwargs):
        input_str = await self.get_message_text(message)
        output_str = app.invoke(input_str)
        await self.reply_safe(message, output_str)

    async def dummy_command_handler(self, message, app: MyApp):
        output_str = app.dummy_command()
        await self.reply_safe(message, output_str)
