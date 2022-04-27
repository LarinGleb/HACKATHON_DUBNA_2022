import os
import mimetypes   
from email import encoders  
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart 

def AttachFile(Message: MIMEMultipart, FilePath: str):
    filename = os.path.basename(FilePath)

    ctype, encoding = mimetypes.guess_type(FilePath)
    maintype, subtype = ctype.split('/', 1)  

    with open("Mail/TempFiles/" + FilePath, 'rb') as fp:
        file = MIMEBase(maintype, subtype)         
        file.set_payload(fp.read())                    
        fp.close()
        encoders.encode_base64(file)

    file.add_header('Content-Disposition', 'attachment', filename=filename) 
    Message.attach(file) 

def ProcessAttachment(Message: MIMEMultipart, FilePaths: list):
    for file in FilePaths:                         
        AttachFile(Message, file)               
