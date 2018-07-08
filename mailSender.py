import smtplib
import config
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
def sendMail(toSendMail,msgOfTheMail,subject,filePath):
	fromaddr = config.EMAIL_ADDRESS
	toaddr = toSendMail
	 
	msg = MIMEMultipart()
	 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject
	 
	body = msgOfTheMail
	 
	msg.attach(MIMEText(body, 'plain'))
	 
	filename = filePath
	attachment = open(filename,"rb")
	
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(part)
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, config.PASSWORD)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
	except e:
		print (e)

sendMail("vardaru@mef.edu.tr","deneme Maili","test","/Users/uluc/Desktop/firstSparkCode.py")
