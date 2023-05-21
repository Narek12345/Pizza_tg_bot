from aiogram import types, Dispatcher


async def no_command(message: types.Message):
    await message.answer("Простите, но я не смог распознать вашу команду.")


def register_handlers_other(dp):
    dp.register_message_handler(no_command)