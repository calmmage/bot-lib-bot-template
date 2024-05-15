from bot_lib import Handler, HandlerDisplayMode
from calmapp import App


class MyApp(App):
    pass


class MyHandler(Handler):
    name = "main"
    display_mode = HandlerDisplayMode.FULL
    pass
