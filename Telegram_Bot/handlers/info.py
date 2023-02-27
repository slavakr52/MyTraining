from loader import dp 
from aiogram.types import Message

@dp.message_handler(commands=['info'])
async def mes_help(message: Message):
    await message.answer(f'Посмотрим, что зашито в твоём сообщении: {message}')
