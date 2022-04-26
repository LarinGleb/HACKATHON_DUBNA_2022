#! /usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import JsonPayload
import telebot
from telebot import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from Bot.keyboards import *
from Bot.WorkWithInform import *

from JSON import JSONFunc
from JSON import ConfigJSON

bot = telebot.TeleBot('5362077781:AAFQzCUuV8KKX7q_wShDxYY9t_yFP4yoA7g')
print('Bot started')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    idUser = message.from_user.id
    if not JSONFunc.CheckUser(idUser):
        if message.text == "123":
            bot.send_message(idUser, "Пароль верный")
            JSONFunc.AddUser(idUser)
        else:
            bot.send_message(message.from_user.id, "Пароль неверный")

    if JSONFunc.CheckUser(idUser):
        stateUser = JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_STATE]
        if message.text == "123" or message.text == "/start":
            bot.send_message(message.from_user.id, "Привет! Что вы ходите сделать?", reply_markup = Keyboard_First)
            JSONFunc.SetPropertyUser(idUser, "input", value=[])

        elif stateUser == "add":
            list_input = JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_INPUT]
            list_input.append(message.text)
            JSONFunc.SetPropertyUser(idUser, "input", value=list_input)
            bot.send_message(message.from_user.id, "Всё верно?\n" + message.text + '?', reply_markup = Keyboard_Sure)
            JSONFunc.SetPropertyUser(idUser, "state", value="added")

        elif 'replaceInform' == stateUser:
            list_input = JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_INPUT]
            list_input.append(message.text)
            ReplaceInfo(list_input)
            bot.send_message(message.from_user.id, "Спасибо, информация изменена", reply_markup = Keyboard_First)
            JSONFunc.SetPropertyUser(idUser, "input", value=[])
            JSONFunc.SetPropertyUser(idUser, "state", value="entered")
    
        elif 'replace' == stateUser:
            list_input = JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_INPUT]
            list_input.append(message.text)
            JSONFunc.SetPropertyUser(idUser, "input", value=list_input)
            JSONFunc.SetPropertyUser(idUser, "state", value="replaced")
            bot.send_message(message.from_user.id, "Что хотите изменить?", reply_markup = Keyboard_Column)
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            idUser = call.from_user.id
            if call.data == "extract":
                bot.send_message(call.message.chat.id, "Выберите, как получить информацию", reply_markup = Keyboard_Extract)

            elif call.data == "change":
                bot.send_message(call.message.chat.id, "Выберите лист", reply_markup = Keyboard_Lists)

            elif call.data in ['list_1', 'list_2', 'list_3']:
                bot.send_message(call.message.chat.id, "Что сделать с информацией?", reply_markup = Keyboard_Action_with_list)
                JSONFunc.SetPropertyUser(idUser, "state", value=call.data)

            elif call.data == 'add':
                bot.send_message(call.message.chat.id, "Введите информацию через пробел(столбцы и прочее)")
                JSONFunc.SetPropertyUser(idUser, "state", value=call.data)

            elif call.data == 'yes':
                AddInform(JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_INPUT])
                bot.send_message(call.message.chat.id, "Спасибо, информация добавленна", reply_markup = Keyboard_First)
                JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                JSONFunc.SetPropertyUser(idUser, "input", value=[])

            elif call.data == 'replace':
                bot.send_message(call.message.chat.id, "Введите серию")
                JSONFunc.SetPropertyUser(idUser, "state", value="replace")

            elif call.data == 'column_1' or call.data == 'column_2':
                list_input = JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_INPUT]
                list_input.append(call.data)
                JSONFunc.SetPropertyUser(idUser, "input", value=list_input)
                bot.send_message(call.message.chat.id, "Текущая информация в ячейке: \n" + InformInColumn(call) + '\n Введите новую')
                JSONFunc.SetPropertyUser(idUser, "state", value="replaceInform")


    except Exception as e:
       print(repr(e))

bot.polling(none_stop=True, interval=0)