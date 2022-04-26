#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from telebot import *

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import keyboards 
from keyboards import *

import WorkWithInform
from WorkWithInform import *

bot = telebot.TeleBot('5175785145:AAGsNoU_rOlVd6zuMbFhD1W1D4nfxAd88Ag')
print('Bot started')


@bot.message_handler(commands=['start'])
def start_message(message):

    if str(message.from_user.id) in open('List.txt').read():
       open('SaveFiles/' + str(message.from_user.id) + '.txt', 'w').write('entered') 
       bot.send_message(message.from_user.id, "Привет! Что вы ходите сделать?", reply_markup = Keyboard_First)
    else:
        bot.send_message(message.chat.id, "Введите пароль")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if str(message.from_user.id) not in open('List.txt').read():
        if message.text == "123":
            bot.send_message(message.from_user.id, "Пароль верный")
            open('List.txt', 'a').write(str(message.from_user.id) + ' \n')
        else:
            bot.send_message(message.from_user.id, "Пароль неверный")

    if str(message.from_user.id) in open('List.txt').read():
        if message.text == "123" or message.text == "/help":
            bot.send_message(message.from_user.id, "Привет! Что вы ходите сделать?", reply_markup = Keyboard_First)

        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши привет")

        elif 'add' in open('SaveFiles/' + str(message.from_user.id) + '.txt').read():
            open('SaveFiles/' + str(message.from_user.id) + '.txt', 'a').write(message.text)
            bot.send_message(message.from_user.id, "Всё верно?\n" + message.text + '?', reply_markup = Keyboard_Sure)

        elif 'replaceInform' in open('SaveFiles/' + str(message.from_user.id) + '.txt').read():
            open('SaveFiles/' + str(message.from_user.id) + '.txt', 'a').write(message.text)
            ReplaceeInform(message)
            bot.send_message(message.from_user.id, "Спасибо, информация изменена", reply_markup = Keyboard_First)
            open('SaveFiles/' + str(message.from_user.id) + '.txt', 'w').write('entered')

        elif 'replace' in open('SaveFiles/' + str(message.from_user.id) + '.txt').read():
            open('SaveFiles/' + str(message.from_user.id) + '.txt', 'a').write(message.text + '\n')
            bot.send_message(message.from_user.id, "Что хотите изменить?", reply_markup = Keyboard_Column)
            
        elif 'extract' in open('SaveFiles/' + str(message.from_user.id) + '.txt').read():
            open('SaveFiles/' + str(message.from_user.id) + '.txt', 'a').write(message.text + '\n')
            bot.send_message(message.from_user.id, "Выберите протокол", reply_markup=Keyboard_Prot)

        
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "extract":
                bot.send_message(call.message.chat.id, "Выберите, как получить информацию", reply_markup = Keyboard_Extract)
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'w').write('extract\n')

            elif call.data == 'eon':
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'a').write('eon' + '\n')
                bot.send_message(call.message.chat.id, "Выберите ион", reply_markup=Keyboard_Eon)

            elif call.data == 'series' or call.data == 'object':
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'a').write(call.data + '\n')
                bot.send_message(call.message.chat.id, "Перечислите их через пробел")

            elif call.data == 'eon_1' or call.data == 'eon_2' or call.data == 'eon_3' or call.data == 'eon_4':
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'a').write(call.data + '\n')
                bot.send_message(call.message.chat.id, "Выберите протокол", reply_markup=Keyboard_Prot)


            elif call.data == "change":
                bot.send_message(call.message.chat.id, "Выберите лист", reply_markup = Keyboard_Lists)

            elif call.data == 'list_1' or call.data == 'list_2' or call.data == 'list_3':
                bot.send_message(call.message.chat.id, "Что сделать с информацией?", reply_markup = Keyboard_Action_with_list)
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'w').write(call.data + '\n')

            elif call.data == 'add':
                bot.send_message(call.message.chat.id, "Введите информацию через пробел(столбцы и прочее)")
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'a').write('add\n')

            elif call.data == 'yes':
                AddInform(call)
                bot.send_message(call.message.chat.id, "Спасибо, информация добавленна", reply_markup = Keyboard_First)
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'w').write('entered')

            elif call.data == 'no':
                f = open('SaveFiles/' + str(call.message.chat.id) + '.txt').readlines()[:-1]
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'w').writelines(f)
                bot.send_message(call.message.chat.id, "Введите информацию через пробел(столбцы и прочее)")

            elif call.data == 'replace':
                bot.send_message(call.message.chat.id, "Введите серию")
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'a').write('replace' + '\n')

            elif call.data == 'column_1' or call.data == 'column_2':
                bot.send_message(call.message.chat.id, "Текущая информация в ячейке: \n" + InformInColumn(call) + '\n Введите новую')
                open('SaveFiles/' + str(call.message.chat.id) + '.txt', 'a').write(call.data +'\nreplaceInform\n')
            


    except Exception as e:
       print(repr(e))

bot.polling(none_stop=True, interval=0)