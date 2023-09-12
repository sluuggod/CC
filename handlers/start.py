from aiogram import types, Dispatcher
from config import bot
from const import START_TEXT

async def start_button(message: types.Message):
    print(message)
    await bot.send_message(
        chat_id=message.chat.id,
        text=START_TEXT.format(
            username=message.from_user.username
        ),
        parse_mode=types.ParseMode.MARKDOWN
    )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])
