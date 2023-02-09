from loader import dp 
from aiogram.types import Message
from keyboards import kb_menu

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    await message.answer(f'И тебе привет, {message.from_user.first_name}', reply_markup=kb_menu)
