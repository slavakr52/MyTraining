import random

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_help = ReplyKeyboardMarkup(resize_keyboard=True)

btn_start = KeyboardButton('/start')
btn_help = KeyboardButton('/help')
btn_info = KeyboardButton('/info')

kb_menu.add(btn_help).add(btn_info)
kb_help.add(btn_start)
