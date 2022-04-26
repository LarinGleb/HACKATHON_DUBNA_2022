
from fpdf import FPDF
from fpdf import XPos, YPos
from datetime import date


def AddToPDFText(pdf:FPDF, text:str, Font: int):
    pdf.set_font('DejaVu', '', Font)
    for t in text.split("\n"):
        pdf.cell(200, 5, text=t, ln=1, align="C")

def GenerateTZCH(Year:str, Ion:str, NumberIon: str, Session: str, NumberSesssionInYear: str = "1"):
    return f"ТЗЧ/{Year}-{Ion}-{NumberSesssionInYear}/{NumberIon}-{Session}" #Тзч/год-название иона- номер сессии в году/номер вывода иона - сеанс

def GenerateTextMain(pdf:FPDF, NumberProtocol: str, Ion: str, Isotope: int, Enegry: str, NumberIon: str, Session:str, Date: str = '.'.join(str(date.today()).split("-"))):
    text = f"""    Протокол №	1/{NumberIon}-{Session}	от {Date} \n					
		        Определения неоднородности флюенса ионов {Isotope}{Ion}	\n
            с энергией	{Enegry}МэВ/N на испытательном стенде	ИИК 10К-400"""
    AddToPDFText(pdf, text, 16)

def GeneratePlan(pdf:FPDF, StartDate: str, EndDate: str):
    text = f"""2. Время и место определения неоднородности флюенса ионов:	\n														
                проводилась в период с	{StartDate}	по {EndDate} в ЛЯР ОИЯИ.	"""
    AddToPDFText(pdf, text, 14)

def FluenceText(pdf:FPDF, Temp: str, Atmosphere: str, WaterInOx: str):
    main = "3. Условия определения неоднородности флюенса ионов:"
    AddToPDFText(pdf, main, 14)
    text = f"""   - температура окружающей среды: {Temp}°С; \n
                  - атмосферное давление: {Atmosphere} мм рт.ст.; \n		
                  - относительная влажность воздуха: {WaterInOx} \n"""

    AddToPDFText(pdf, text, 12)

def AddTable(pdf:FPDF, Values: set):
    data = [('ТД1','ТД2','ТД3','ТД4','ТД5','ТД6','ТД7','ТД8','ТД9'), Values]
    pdf.set_font('DejaVu', '', 14)
    line_height = 50
    col_width = pdf.epw / 9
    for row in data:
        for datum in row:
            pdf.multi_cell(col_width, line_height, datum, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size, align="C")
        pdf.ln(line_height)
    

def HeterogeneityIon(Intense: str, Heterogeneity: str, Koeff: str, DeltaKoef: str, TD: list):
    pass

pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '', 'Fonts/DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 14)

pdf.output('table_with_cells.pdf')