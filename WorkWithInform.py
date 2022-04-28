import os
import telebot
from telebot import *
import GoogleTable
from PDF import AddPDF
from GoogleTable import GetValues
import Mail
import zipfile
import tarfile

workingLib = os.getcwd()

def AddInform(Info): #Добавуляет информацию в таблицу
    print(123)

def InformInColumn(call): #возвращает информацию из ячейки
    return 'qqq'

def ReplaceInfo(Info): #изменяет информацию
    print(345)

def AddToZip(nameZip, files):
    archive = zipfile.ZipFile(f'Mail/TempFiles/{nameZip}.zip', 'w')
    os.chdir("Mail/TempFiles/")
    for file in files:
        if file.endswith(".pdf"):
            archive.write(file, compress_type=zipfile.ZIP_DEFLATED)
    archive.close()
    os.chdir(workingLib)

def AddTotar(nametar, files):
    os.chdir("Mail/TempFiles/")
    for file in files:
        with tarfile.TarFile.open(f'Mail/TempFiles/{nametar}.tar.bz2', 'w:bz2') as tar:
            tar.add("Mail/TempFiles/" + file, 'Mail/TempFiles/{nametar}.tar.bz2')
    tar.close()
    os.chdir(workingLib)
    
def GenerateAccessProtoclBySeria(seria):
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

def GetAllTempFiles():
    return os.listdir("Mail/TempFiles")

def Output_Information(Data, Bot, Id):
    standart_mail = Data[1]
    ins_chat = Data[3]
    ins_mail = Data[4]
    to_file = Data[5]
    to_zip = Data[6]
    to_tar = Data[7]
    input = Data[9]
    format_file = ""


    if to_zip or input["type_file"] == "to_zip":
        format_file = "zip"
    elif to_tar or input["type_file"] == "to_tar":
        format_file = "tar"
    elif to_file or input["type_file"] == "to_zip":
        format_file = "file"


    mails = []
    if ins_mail:
        mails = standart_mail
    elif input["send"] == "ins_mail":
        mails = input["mail"]
    
    series = []


    if input["indexed"] == "eon":
        series = GoogleTable.GetValues.GetAllSeriesByIon(input["ion"])
    
    elif input["indexed"] == "object":
        for i in input["input_indexed"].split(" "):
            series.extend(GoogleTable.GetValues.GetAllSeriesByObject(i))

    elif input["indexed"] == "series":
        for i in input["input_indexed"].split(" "):

            series.append(i)

    if input["protocol"] == "prot_2":
        for seria in series:
            GenerateAccessProtoclBySeria(seria)


    if format_file == "zip":
        AddToZip("Protocols", GetAllTempFiles())
        for file in GetAllTempFiles():
            if not file.endswith(".zip"):
                os.remove("Mail/TempFiles/" + file)
    
    elif format_file == "tar":
        AddTotar("protocols", GetAllTempFiles())
        for file in GetAllTempFiles():
            if not file.endswith(".tar.bz2"):
                os.remove("Mail/TempFiles/" + file)


    if mails:
        if type(mails) == str:
            mails = [mails]
        Mail.SendMails.Mailing(mails, GetAllTempFiles())

    elif input["send"] == "ins_chat":
        SendFilesToBot(Bot, Id, format_file)


def SendFilesToBot(Bot, Id, format):
    for file in GetAllTempFiles():
        Bot.send_document(chat_id=Id, data=open("Mail/TempFiles/" + file, "rb"))
        os.remove("Mail/TempFiles/" + file)