import smtplib                
from email.mime.text import MIMEText                      
from email.mime.multipart import MIMEMultipart

from yaml import add_representer 
from . import FileInMail
from pathlib import Path

PORT = 587
SERVER = "smtp.gmail.com"
USER = "hackathonbotdubna@gmail.com"
PASSWORD = "table_bot_ones"

def SendMail(Addr: str, FilePaths: str):

    msg = MIMEMultipart()                                  
    msg['From']    = USER                     
    msg['To']      = Addr        
    msg['Subject'] = "Protocol"   

    body = "there is your files!"
    msg.attach(MIMEText(body, 'plain'))         
    FileInMail.ProcessAttachment(msg, FilePaths)   
    server = smtplib.SMTP(SERVER, PORT)       
    server.starttls()                          
    server.login(USER, PASSWORD)    
    server.send_message(msg)
    server.quit()  

    

def Mailing(Addresses: list, PDFS: list):
    try:
        for address in Addresses:
            print(address)
            SendMail(address, PDFS)
    except Exception as e:
        print(e)