import os
import telebot
from telebot import *
from PDF import AddPDF
from GoogleTable import GetValues
import Mail




def AddInform(Info): #Добавуляет информацию в таблицу
    print(Info)

def InformInColumn(call): #возвращает информацию из ячейки
    return 'qqq'

def ReplaceInfo(Info): #изменяет информацию
    print(Info)

def Output_Information(Data):
    input = Data[9]
    for seria in input[1].split():
        information = GetValues.GetValuesByValue(seria)
        org = information[1]
        ion = information[2]
        
        
        start_date = information[9]
        end_date = information[10]
    
        long_aducation = information[11]
        logn_session = information[12]
        time_with_tp = information[13]
    
        start_tp = information[15]
        end_tp = information[16]
        time_tp = information[17]
        
        objects = information[20:24]
        code = information[24]
    
        average_TD = information[25]
        td = information[26:35]
    
        td.append(average_TD)
    
        average_online = information[36]
        online_decetors = information[37:41]
    
        intence = information[40]
        code_accsess = information[41]
        angle = information[42]
        pressure = information[43]
        water = information[44]
        temp = information[45]
        temp_seance = information[46]
        heneg = information[47]
        koef = information[48]
        delta = information[49]
    
        informationION = GetValues.GetValuesByValue(ion)
    
        isotop = informationION[1]
        number_session  = informationION[2]
        info_deg = informationION[2:5]
    
        sreda = informationION[5]
        energy = informationION[6]
        deltaEnegery = informationION[7]
        run = informationION[8]
        delta_run = informationION[9]
    
        lpe = informationION[10]
        delta_lpe = informationION[11]
    
        energy_ion = information[12]
    
        number_session_year = information[13]
        AddPDF.GenerateProtocolAccess(f"Protocol_{seria}_{ion}", "2022", ion, "1", average_online, intence, heneg, koef, delta, start_date, end_date, seria, number_session, td, isotop, temp, pressure, water, energy)
    mails_wet = input[4]
    if type(mails_wet) == str:
        mails = [mails_wet]

    else:
        mails = mails_wet
    mailsParced = []
    for i in mails:
        mailsParced.append(i.strip())

    Mail.SendMails.Mailing(mailsParced, os.listdir("Mail/TempFiles"))
    