import smtplib                
from email.mime.text import MIMEText                      
from email.mime.multipart import MIMEMultipart

import os
from . import FileInMail
PORT = 587
SERVER = "smtp.gmail.com"
USER = "hackathonbotdubna8@gmail.com"
PASSWORD = "tryToHack8!"

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
            SendMail(address, PDFS)
        
        for file in PDFS:
            os.remove("Mail/TempFiles/"+file)
    except Exception as e:
        print(e)