import json
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

path = "./simple_report_dev.json"
Paradise_AlarmFrame = 25

def mail():
	print("Alarm mail")
	mail_host = "smtp.163.com"
	mail_sender = "he_garena@163.com"
	mail_license = "LSIVFTZVQYCTDTOF"
	mail_receivers = ["563999075@qq.com"]

	mm = MIMEMultipart('related')

	subject_content = """Python邮件测试"""
	mm["From"] = "ffUPRWarning<******@garena.com>"
	#mm["To"] = "receiver_1_name<******@qq.com>,receiver_2_name<******@outlook.com>"
	mm["To"] = "ff<******@garena.com>,receiver_2_name<******@outlook.com>"
	mm["Subject"] = Header(subject_content,'utf-8')

	body_content = """你好，这是一个测试邮件！"""
	message_text = MIMEText(body_content,"plain","utf-8")
	mm.attach(message_text)

	stp = smtplib.SMTP()
	stp.connect(mail_host, 25)  
	stp.set_debuglevel(1)
	stp.login(mail_sender,mail_license)
	stp.sendmail(mail_sender, mail_receivers, mm.as_string())
	print("邮件发送成功")
	stp.quit()
	return 1234

def main():
	with open(path,mode='r',encoding='utf-8') as demoJSON:
		sessionData = json.load(demoJSON)
		newestReport = sessionData['ReportList'][0]
		score = int(newestReport['Score'])
		AverageFrameRate = newestReport['AverageFrameRate']
		print(AverageFrameRate)
		if AverageFrameRate < Paradise_AlarmFrame :
			print("warning")
			index = mail()
			print(index)

		print("缩进对if有影响")

if __name__ == "__main__":
	main()