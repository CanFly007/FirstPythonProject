import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

class mailHandleIN(object):
	def __init__(self,testStr):
		self.myStr = testStr

	def myPrint(self):
		print(self.myStr)

	def mail(self,version,data):
		print("Alarm mail")
		print(version)
		print(data)
		return 2222
		mail_host = "smtp.163.com"
		mail_sender = "he_garena@163.com" #改为公共邮箱
		mail_license = "LSIVFTZVQYCTDTOF" #公共邮箱的license
		mail_receivers = ["563999075@qq.com"] #测试用，ff_all@garena.com

		mm = MIMEMultipart('related')

		subject_content = """Performance Alert"""
		mm["From"] = "upr_noreply"
		#mm["To"] = "receiver_1_name<******@qq.com>,receiver_2_name<******@outlook.com>"
		mm["To"] = "xueqiang.he@garena.com,fff_all@garena.com"
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