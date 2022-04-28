#! /usr/bin/env python
# -*- coding: utf-8 -*-

from aiohttp import JsonPayload
#import telebot
from telebot import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from Bot.keyboards import *
from WorkWithInform import *

from JSON import JSONFunc
from JSON import ConfigJSON
import JSON

bot = telebot.TeleBot("5175785145:AAGsNoU_rOlVd6zuMbFhD1W1D4nfxAd88Ag")
print("Bot started")
pas = "123"

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    global pas
    idUser = message.from_user.id
    if not JSONFunc.CheckUser(idUser):
        if message.text == pas:
            bot.send_message(idUser, "Пароль верный")
            JSONFunc.AddUser(idUser)
        else:
            bot.send_message(message.from_user.id, "Пароль неверный")

    
    if JSONFunc.CheckUser(idUser):
        stateUser = JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_STATE]
        if message.text == "123" or message.text == "/start":
            bot.send_message(message.from_user.id, "Привет! Что вы ходите сделать?", reply_markup = Keyboard_First)
            JSONFunc.SetDefaultInput(idUser)

        elif stateUser == "add":
            JSONFunc.SetInputProperty(idUser, "input", value=message.text)
            bot.send_message(message.from_user.id, "Всё верно?\n" + message.text + "?", reply_markup = Keyboard_Sure)
            JSONFunc.SetPropertyUser(idUser, "state", value="added")

        elif "replaceInform" == stateUser:
            list_input = JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_INPUT]
            list_input.append(message.text)
            ReplaceInfo(list_input)
            bot.send_message(message.from_user.id, "Спасибо, информация изменена", reply_markup = Keyboard_First)
            JSONFunc.SetDefaultInput(idUser)
            JSONFunc.SetPropertyUser(idUser, "state", value="entered")
    
        elif "replace" == stateUser:
            JSONFunc.SetInputProperty(idUser, "seria", message.text)
            JSONFunc.SetPropertyUser(idUser, "state", value="replaced")
            bot.send_message(message.from_user.id, "Что хотите изменить?", reply_markup = Keyboard_Column)
        
        elif "extract" == stateUser:
            JSONFunc.SetInputProperty(idUser, "input_indexed", value=message.text)

            bot.send_message(message.from_user.id, "Выберите протокол", reply_markup=Keyboard_Prot)
            
        elif "mail" == stateUser:
            JSONFunc.SetInputProperty(idUser, "mail", value=message.text)

            if message.text not in JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_LAST_MAIL]:
                list_last_mail = JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_LAST_MAIL]
                list_last_mail.append(message.text)
                JSONFunc.SetPropertyUser(idUser, "last_mail", value=list_last_mail)

            if JSONFunc.GetUserConfig(idUser) [5]:
                Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                JSONFunc.SetDefaultInput(idUser)

            elif JSONFunc.GetUserConfig(idUser) [6]:
                Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                JSONFunc.SetDefaultInput(idUser)

            elif JSONFunc.GetUserConfig(idUser) [7]:
                Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                JSONFunc.SetDefaultInput(idUser)
            
            else:
                bot.send_message(message.from_user.id, "Как отправить файлы?", reply_markup=Keyboard_Extension)

        elif "password" == stateUser:
            pas = message.text
            JSONFunc.SetPropertyUser(idUser, "state", value="settings")
            bot.send_message(message.from_user.id, "Новый пароль установлен", reply_markup = Keyboard_Settings)
        
        elif 'const_mail' == stateUser:
            JSONFunc.SetPropertyUser(idUser, "standart_mail", value=[*JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_STANDART_MAIL], message.text])
            bot.send_message(message.from_user.id, "Эта почта добавлена как постоянная", reply_markup = Keyboard_Settings)
            JSONFunc.SetPropertyUser(message.from_user.id, "state", value="entered")

        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        idUser = call.from_user.id
        if call.data == "extract":
            bot.send_message(idUser, "Выберите, как получить информацию", reply_markup = Keyboard_Extract)
            JSONFunc.SetPropertyUser(idUser, "state", value=call.data)

        elif call.data == "eon":
            JSONFunc.SetInputProperty(idUser, "indexed", call.data)
            bot.send_message(idUser, "Выберите ион", reply_markup=Keyboard_Eon)

        elif call.data == "series" or call.data == "object":
            JSONFunc.SetInputProperty(idUser, "indexed", call.data)
            bot.send_message(idUser, "Перечислите их через пробел")

        elif call.data in ['Xe', 'Kr', 'Ar' 'Ne']:
            JSONFunc.SetInputProperty(idUser, "ion", call.data)
            bot.send_message(idUser, "Выберите протокол", reply_markup=Keyboard_Prot)

        elif call.data == 'prot_1' or call.data == 'prot_2' or call.data == 'prot_3':
            JSONFunc.SetInputProperty(idUser, "protocol", call.data)

            if JSONFunc.GetUserConfig(idUser) [3]:

                if JSONFunc.GetUserConfig(idUser) [5]:
                    Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                    bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                    JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                    JSONFunc.SetDefaultInput(idUser)

                elif JSONFunc.GetUserConfig(idUser) [6]:
                    Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                    bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                    JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                    JSONFunc.SetDefaultInput(idUser)

                elif JSONFunc.GetUserConfig(idUser) [7]:
                    Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                    bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                    JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                    JSONFunc.SetDefaultInput(idUser)

                else:
                    bot.send_message(idUser, "Как отправить файлы?", reply_markup=Keyboard_Extension)

            elif JSONFunc.GetUserConfig(idUser) [4]:

                if len(JSONFunc.GetUserConfig(idUser) [1])>0:

                    if JSONFunc.GetUserConfig(idUser) [5]:
                        Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                        bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                        JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                        JSONFunc.SetDefaultInput(idUser)

                    elif JSONFunc.GetUserConfig(idUser) [6]:
                        Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                        bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                        JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                        JSONFunc.SetDefaultInput(idUser)

                    elif JSONFunc.GetUserConfig(idUser) [7]:
                        Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                        bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                        JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                        JSONFunc.SetDefaultInput(idUser)

                    else:
                        bot.send_message(idUser, "Как отправить файлы?", reply_markup=Keyboard_Extension)

                else:
                    JSONFunc.SetPropertyUser(idUser, "state", value='mail')

                    Keyboard_Mail = types.ReplyKeyboardMarkup(row_width=2)  
                    if len(JSONFunc.GetUserConfig(idUser) [0]) > 0:
                        btn_m1 = types.KeyboardButton(JSONFunc.GetUserConfig(idUser) [0][0])
                        Keyboard_Mail.add(btn_m1)
                        if len(JSONFunc.GetUserConfig(idUser) [0]) > 1:
                            btn_m2 = types.KeyboardButton(JSONFunc.GetUserConfig(idUser) [0][1])
                            Keyboard_Mail.add(btn_m2)
                    bot.send_message(idUser, "Введите почту", reply_markup=Keyboard_Mail)
                        
            else:
                bot.send_message(idUser, "Выберите способ отправки", reply_markup=Keyboard_Send)
            
        elif call.data == "ins_chat": 
            JSONFunc.SetInputProperty(idUser, "send", call.data)
            Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
            bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
            JSONFunc.SetPropertyUser(idUser, "state", value="entered")
            JSONFunc.SetDefaultInput(idUser)

        elif call.data == "ins_mail":
            if JSONFunc.GetUserConfig(idUser) [1]:
                if JSONFunc.GetUserConfig(idUser) [5]:
                    Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                    bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                    JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                    JSONFunc.SetDefaultInput(idUser)

                elif JSONFunc.GetUserConfig(idUser) [6]:
                    Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                    bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                    JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                    JSONFunc.SetDefaultInput(idUser)

                elif JSONFunc.GetUserConfig(idUser) [7]:
                    Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
                    bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
                    JSONFunc.SetPropertyUser(idUser, "state", value="entered")
                    JSONFunc.SetDefaultInput(idUser)
                
                else:
                    bot.send_message(idUser, "Как отправить файлы?", reply_markup=Keyboard_Extension)

            else:
                JSONFunc.SetPropertyUser(idUser, "state", value="mail")
                JSONFunc.SetInputProperty(idUser, "send", call.data)

                Keyboard_Mail = types.ReplyKeyboardMarkup(row_width=2)  
                if len(JSONFunc.GetUserConfig(idUser) [0]) > 0:
                    btn_m1 = types.KeyboardButton(JSONFunc.GetUserConfig(idUser) [0][0])
                    Keyboard_Mail.add(btn_m1)
                    if len(JSONFunc.GetUserConfig(idUser) [0]) > 1:
                        btn_m2 = types.KeyboardButton(JSONFunc.GetUserConfig(idUser) [0][1])
                        Keyboard_Mail.add(btn_m2)
                bot.send_message(idUser, "Введите почту", reply_markup=Keyboard_Mail)

        elif call.data == 'to_zip' or call.data == 'to_tar' or call.data == 'to_file':
            JSONFunc.SetInputProperty(idUser, "type_file", value=call.data)
            Output_Information(JSONFunc.GetUserConfig(idUser), bot, idUser)
            bot.send_message(idUser, "Спасибо, протокол отправлен", reply_markup = Keyboard_First)
            JSONFunc.SetPropertyUser(idUser, "state", value="entered")
            JSONFunc.SetDefaultInput(idUser)

        elif call.data == "change":
            bot.send_message(idUser, "Выберите лист", reply_markup = Keyboard_Lists)

        elif call.data in ["list_1", "list_2", "list_3"]:
            bot.send_message(idUser, "Что сделать с информацией?", reply_markup = Keyboard_Action_with_list)
            JSONFunc.SetPropertyUser(idUser, "state", value="choosed list")
            JSONFunc.SetInputProperty(idUser, "list", value=call.data)

        elif call.data == "add":
            bot.send_message(idUser, "Введите информацию через пробел(столбцы и прочее)")
            JSONFunc.SetPropertyUser(idUser, "state", value=call.data)

        elif call.data == "yes":
            AddInform(JSONFunc.GetUserConfig(idUser)[ConfigJSON.I_INPUT])
            bot.send_message(idUser, "Спасибо, информация добавленна", reply_markup = Keyboard_First)
            JSONFunc.SetPropertyUser(idUser, "state", value="entered")
            JSONFunc.SetDefaultInput(idUser)

        elif call.data == "replace":
            bot.send_message(idUser, "Введите серию")
            JSONFunc.SetPropertyUser(idUser, "state", value="replace")

        elif call.data == "column_1" or call.data == "column_2":
            JSONFunc.SetInputProperty(idUser, "input", "choosen_column")
            bot.send_message(idUser, "Текущая информация в ячейке: \n" + InformInColumn(call) + "\n Введите новую")
            JSONFunc.SetPropertyUser(idUser, "state", value="replaceInform")

        elif call.data == "settings":
            JSONFunc.SetPropertyUser(idUser, "state", value="settings")
            bot.send_message(idUser, "Меню настроек бота", reply_markup = Keyboard_Settings)
        
        elif call.data == 'sending_files':
            bot.send_message(idUser, "Выберите действие", reply_markup = Keyboard_Sending_Files)
        
        elif call.data == "password":
            JSONFunc.SetPropertyUser(idUser, "state", value="password")
            bot.send_message(idUser, "Введите новый код доступа")

        elif call.data == 'link_to_table':
            print('dodelat')
            #изменение ссылки на таблицу

        elif call.data == 'menu':
            JSONFunc.SetPropertyUser(idUser, "state", value="entered")
            bot.send_message(idUser, "Выберите действие", reply_markup=Keyboard_First)
        
        elif call.data == 'always_chat':
            JSONFunc.SetPropertyUser(idUser, "ins_chat", value=True)
            JSONFunc.SetPropertyUser(idUser, "ins_mail", value=False)
            bot.send_message(idUser, "Теперь протоколы будут всегда отправляться в чат", reply_markup = Keyboard_Settings)

        elif call.data == 'always_mail':
            JSONFunc.SetPropertyUser(idUser, "ins_mail", value=True)
            JSONFunc.SetPropertyUser(idUser, "ins_chat", value=False)
            bot.send_message(idUser, "Теперь протоколы будут всегда отправляться на почту", reply_markup = Keyboard_Settings)

        elif call.data == 'const_mail':
            JSONFunc.SetPropertyUser(idUser, "state", value='const_mail')
            bot.send_message(idUser, "Введите почту для постоянной отправки на неё")

        elif call.data == 'always_tar':
            JSONFunc.SetPropertyUser(idUser, "to_tar", value=True)
            JSONFunc.SetPropertyUser(idUser, "to_file", value=False)
            JSONFunc.SetPropertyUser(idUser, "to_zip", value=False)
            bot.send_message(idUser, "Теперь протоколы всегда будут отправляться в расширении tar", reply_markup = Keyboard_Settings)

        elif call.data == 'always_zip':
            JSONFunc.SetPropertyUser(idUser, "to_zip", value=True)
            JSONFunc.SetPropertyUser(idUser, "to_file", value=False)
            JSONFunc.SetPropertyUser(idUser, "to_tar", value=False)
            bot.send_message(idUser, "Теперь протоколы всегда будут отправляться в расширении zip", reply_markup = Keyboard_Settings)

        elif call.data == 'always_fi.le':
            JSONFunc.SetPropertyUser(idUser, "to_file", value=True)
            JSONFunc.SetPropertyUser(idUser, "to_zip", value=False)
            JSONFunc.SetPropertyUser(idUser, "to_tar", value=False)
            bot.send_message(idUser, "Теперь протоколы всегда будут отправляться обычными файлами", reply_markup = Keyboard_Settings)

        elif call.data == 'menu':
            JSONFunc.SetPropertyUser(idUser, "state", value="entered")
            bot.send_message(idUser, "Выберите действие", reply_markup=Keyboard_First)
        
        elif call.data == 'always_chat':
            JSONFunc.SetPropertyUser(idUser, "ins_chat", value=True)
            JSONFunc.SetPropertyUser(idUser, "ins_mail", value=False)
            bot.send_message(idUser, "Теперь протоколы будут всегда отправляться в чат", reply_markup = Keyboard_Settings)
        elif call.data == 'always_mail':
            JSONFunc.SetPropertyUser(idUser, "ins_mail", value=True)
            JSONFunc.SetPropertyUser(idUser, "ins_chat", value=False)
            bot.send_message(idUser, "Теперь протоколы будут всегда отправляться на почту", reply_markup = Keyboard_Settings)
        elif call.data == 'const_mail':
            JSONFunc.SetPropertyUser(idUser, "state", value='const_mail')
            bot.send_message(idUser, "Введите почту для постоянной отправки на неё")
        elif call.data == 'always_tar':
            JSONFunc.SetPropertyUser(idUser, "to_tar", value=True)
            JSONFunc.SetPropertyUser(idUser, "to_file", value=False)
            JSONFunc.SetPropertyUser(idUser, "to_zip", value=False)
            bot.send_message(idUser, "Теперь протоколы всегда будут отправляться в расширении tar")
        elif call.data == 'always_zip':
            JSONFunc.SetPropertyUser(idUser, "to_zip", value=True)
            JSONFunc.SetPropertyUser(idUser, "to_file", value=False)
            JSONFunc.SetPropertyUser(idUser, "to_tar", value=False)
            bot.send_message(idUser, "Теперь протоколы всегда будут отправляться в расширении zip")
        elif call.data == 'always_fi.le':
            JSONFunc.SetPropertyUser(idUser, "to_file", value=True)
            JSONFunc.SetPropertyUser(idUser, "to_zip", value=False)
            JSONFunc.SetPropertyUser(idUser, "to_tar", value=False)
            bot.send_message(idUser, "Теперь протоколы всегда будут отправляться обычными файлами")

if __name__=='__main__':
    bot.polling(none_stop=True, interval=0)
