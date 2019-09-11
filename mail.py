import smtplib #simple mail transfer protocol used for email server i.e to create client session obj
from io import StringIO
from io import BytesIO
from email.mime.base import MIMEBase #This is the base class for all the MIME-specific subclasses of Message
from email.mime.text import MIMEText #The MIMEText class is used to create MIME objects of major type text
from email import encoders
from email.mime.multipart import MIMEMultipart #This is an intermediate base class for MIME messages that are multipart

print('Sending email...')

sender_id = '' #email of sender
email_password = ''
receiver_id = '' #email of receiver
subject = 'ICT'



message = MIMEMultipart()
message['From'] = sender_id #USING MULTIPART() WE CAN DIVIDE MESSAGE INTO DIFFERENT PARTS
message['To'] = receiver_id
message['Subject'] = subject

message_body = 'DEMO MAIL FROM PYTHON PROGRAM'
message.attach(MIMEText(message_body,'plain')) #USING ATTACH WE CAN ATTACH MAIL MULTIPARTS AS ONE SINGLE MESSAGE

file_name='C:\\Users\\Hetvi\\Desktop\\ICT.txt'
attachment=open(file_name,'rb')

part = MIMEBase('application','octet-stream') #TO POST DATA
part.set_payload((attachment).read())
encoders.encode_base64(part) #Encodes the payload into base64(TO ENCODE DATA)
part.add_header('Content-Disposition',"attachment; filename= "+file_name)

message.attach(part)
text = message.as_string() #CONVERTS MESSAGE INTO STRING TYPE
server = smtplib.SMTP('smtp.gmail.com',587) #PORT NUMBER FOR GMAIL
server.starttls() #STARTS THE EMAIL SERVER
server.login(sender_id,email_password)


server.sendmail(sender_id,receiver_id,text)
server.quit() #QUIT CONNECTION TO THE EMAIL SERVER

print('\nEmail sent...')