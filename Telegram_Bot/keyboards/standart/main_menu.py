import random

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_help = ReplyKeyboardMarkup(resize_keyboard=True)

btn_start = KeyboardButton('/start')
btn_help = KeyboardButton('/help')
<<<<<<< HEAD
btn_info = KeyboardButton('/info')

kb_menu.add(btn_help).add(btn_info)
kb_help.add(btn_start)
=======
btn_contact = KeyboardButton('Кто я?', request_contact=True)
btn_location = KeyboardButton('Где я?', request_location=True)

kb_menu.add(btn_help)
kb_help.add(btn_start, btn_contact, btn_location)
>>>>>>> 783143bbdf188be5f4b4c51df1210c9278c8934b
