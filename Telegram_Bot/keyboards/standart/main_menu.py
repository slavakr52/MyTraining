import random

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_help = ReplyKeyboardMarkup(resize_keyboard=True)

btn_start = KeyboardButton('/start')
btn_help = KeyboardButton('/help')
btn_digit = KeyboardButton('Нажми меня')

kb_menu.add(btn_help).add(btn_digit)
kb_help.add(btn_start, btn_digit)
