
from fpdf import FPDF
from fpdf import XPos, YPos
from datetime import date

NORMAL = "0123456789+-, "

def GetSuper(text):
    super = "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻, "
    res = text.maketrans("".join(NORMAL), "".join(super))
    return text.translate(res)

def AddToPDFText(pdf:FPDF, text:str, Font: int, Aling = "L"):
    pdf.set_font('DejaVu', '', Font)
    for t in text.split("\n"):
        pdf.cell(200, 5, txt=t, align=Aling)
        pdf.ln()

def GenerateTZCH(Year:str, Ion:str, NumberIon: str, Session: str, NumberSesssionInYear: str = "1"):
    return f"ТЗЧ/{Year}-{Ion}-{NumberSesssionInYear}/{NumberIon}-{Session}" #Тзч/год-название иона- номер сессии в году/номер вывода иона - сеанс

def GenerateTextMain(pdf:FPDF, NumberProtocol: str, Ion: str, Isotope: int, Enegry: str, NumberIon: str, Session:str, Date: str = '.'.join(str(date.today()).split("-"))):
    text = f"""Протокол №1/{NumberIon}-{Session} от {Date} \n Определения неоднородности флюенса ионов {GetSuper(Isotope)}{Ion}  \n с энергией  {Enegry}МэВ/N на испытательном стенде  ИИК 10К-400 \n"""

    AddToPDFText(pdf, text, 16, "C")

def GeneratePlan(pdf:FPDF, StartDate: str, EndDate: str):
    text = f"""1. Цель: Оценка соответствия неоднородности флюенса ионов \nтребованиям заказчика испытаний. \n\n2. Время и место определения неоднородности флюенса ионов:  \n     проводилась в период с  {StartDate}  по {EndDate} в ЛЯР ОИЯИ. \n """
    AddToPDFText(pdf, text, 14)

def FluenceText(pdf:FPDF, Temp: str, Atmosphere: str, WaterInOx: str):
    main = "3. Условия определения неоднородности флюенса ионов:"
    AddToPDFText(pdf, main, 14)
    text = f""" - температура окружающей среды: {Temp}°С; \n - атмосферное давление: {Atmosphere} мм рт.ст.; \n - относительная влажность воздуха: {WaterInOx}%\n"""

    AddToPDFText(pdf, text, 12)
    notFormating = f"""4. Средства определения неоднородности флюенса ионов:"""

    AddToPDFText(pdf, notFormating, 14) 

    notFormattingInfo = """ - испытательный стенд: ИИК 10К-400 \n - трековые мембраны (лавсановая плёнка); \n - установка для травления лавсановой плёнки; \n - растровы электронный микроскоп ТM-3000 (Hitachi, Япония); \n - система оцифровки видеосигнала «GALLERY-512». \n"""       
    
    AddToPDFText(pdf, notFormattingInfo, 12)

    nextInfo = """5. Методика определения неоднородности флюенса ионов. \n\n5.1. Проводилась в соответствии с «Методикой измерений флюенса \nтяжелых заряженных частиц с помощью трековых мембран\nна основе лавсановой пленки» ЦДКТ1.027.012-2015.\n"""

    AddToPDFText(pdf, nextInfo, 14) 

       
def AddTable(pdf:FPDF, Values):
    data = [['ТД1','ТД2','ТД3','ТД4','ТД5','ТД6','ТД7','ТД8','ТД9', "ТДсреднее"], Values]
    pdf.set_font('DejaVu', '', 14)
    line_height = 10
    col_width = pdf.epw / 7
    for row in data:
        
        for datum in row[:len(row) // 2]:
            pdf.multi_cell(col_width, line_height, datum, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size, align="C")
        pdf.ln(line_height)

    for row in data:
        for datum in row[len(row)//2:]:
            pdf.multi_cell(col_width, line_height, datum, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size, align="C")
        pdf.ln(line_height)
    pdf.ln(line_height)

def GenerateProtocolAccess(name, Year:str, Ion:str, NumberIon: str, AverageOnline: str,  Intense, Heterogeneity, Koeff, DeltaKoef, StartDate: str, EndDate: str, Session: str, NumberProtocol: str, TD:list, Isotope: int, Temp: str, Atmosphere: str, WaterInOx: str, Enegry: str, Date: str = '.'.join(str(date.today()).split("-")), NumberSesssionInYear: str = "1"):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'Fonts/DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    
    AddToPDFText(pdf, GenerateTZCH(Year, Ion, NumberIon, Session), 16, "R")
    GenerateTextMain(pdf, NumberProtocol, Ion, Isotope, Enegry, NumberIon, Session)
    GeneratePlan(pdf, StartDate, EndDate)
    FluenceText(pdf, Temp, Atmosphere, WaterInOx)
    HeterogeneityIon(pdf, Intense, Heterogeneity, Koeff, DeltaKoef, AverageOnline, TD, Ion, Isotope)

    finalText = """Ответственный за проведение испытаний \nв испытательную смену от \nООО"НПП"Детектор \n\n    _________________     (                     )\n\n\n"""

    finalText2 = """Ответственный за проверку от ЛЯР ОИЯИ\n\n _________________   (                     )\n"""

    AddToPDFText(pdf, finalText, 14, 'C')
    AddToPDFText(pdf, finalText2, 14, 'C')

    pdf.output(f'Mail/TempFiles/{name}.pdf')

def HeterogeneityIon(pdf, Intense: str, Heterogeneity: str, Koeff: str, DeltaKoef: str, AverageOnline:str, TD: list, Ion:str, Isotope: str):
    text = f"6. Результаты определения неоднородности флюенса \nионов {GetSuper(Isotope)}{Ion} представлены в таблице 1: "
    AddToPDFText(pdf, text, 14)

    formules= f"N = {Intense} c{GetSuper('-1')}\nФ = {AverageOnline} частиц*см{GetSuper('-2')}\n"
    AddToPDFText(pdf, formules, 12)
    AddTable(pdf, TD)

    koefs = f"Коэффициент : Красчетный = {Koeff} ± {DeltaKoef}\nНеоднородность флюенса ионов составила :{Heterogeneity}\n"
    AddToPDFText(pdf, koefs, 12)


