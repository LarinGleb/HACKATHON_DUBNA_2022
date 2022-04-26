import telebot
from telebot import *
Keyboard_First = types.InlineKeyboardMarkup(row_width = 1)
btn_f1 = types.InlineKeyboardButton('Извлечь информацию', callback_data='extract')
btn_f2 = types.InlineKeyboardButton('Изменить информацию', callback_data='change')
btn_f3 = types.InlineKeyboardButton('Настройки бота', callback_data='settings')
Keyboard_First.add(btn_f1, btn_f2, btn_f3)

Keyboard_Extract = types.InlineKeyboardMarkup(row_width = 1)
btn_e1 = types.InlineKeyboardButton('По иону', callback_data='eon')
btn_e2 = types.InlineKeyboardButton('По серии', callback_data='series')
btn_e3 = types.InlineKeyboardButton('По объекту', callback_data='object')
Keyboard_Extract.add(btn_e1, btn_e2, btn_e3)

Keyboard_Lists = types.InlineKeyboardMarkup(row_width = 1)
btn_l1 = types.InlineKeyboardButton('1', callback_data='list_1')
btn_l2 = types.InlineKeyboardButton('2', callback_data='list_2')
btn_l3 = types.InlineKeyboardButton('3', callback_data='list_3')
Keyboard_Lists.add(btn_l1, btn_l2, btn_l3)

Keyboard_Action_with_list = types.InlineKeyboardMarkup(row_width = 1)
btn_a1 = types.InlineKeyboardButton('Добавить', callback_data='add')
btn_a2 = types.InlineKeyboardButton('Изменить', callback_data='replace')
Keyboard_Action_with_list.add(btn_a1, btn_a2)

Keyboard_Sure = types.InlineKeyboardMarkup(row_width = 1)
btn_s1 = types.InlineKeyboardButton('Да', callback_data='yes')
btn_s2 = types.InlineKeyboardButton('Нет', callback_data='no')
Keyboard_Sure.add(btn_s1, btn_s2)

Keyboard_Column = types.InlineKeyboardMarkup(row_width = 1)
btn_c1 = types.InlineKeyboardButton('Столбец 1', callback_data='column_1')
btn_c2 = types.InlineKeyboardButton('Столбец 2', callback_data='column_2')
Keyboard_Column.add(btn_c1, btn_c2)