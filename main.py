import json
from mailHandle import MailHandle

path = "./simple_report_dev.json"
Paradise_AlarmFrame = 25
ReservedTotal_Alarm = 400 #测试数值
TrianglesPeak_Alarm = 160000

def main():
	with open(path,mode='r',encoding='utf-8') as simpleReportDevJSON:
		sessionData = json.load(simpleReportDevJSON)
		newestReport = sessionData['ReportList'][0]
		needWarningMail = False
		warningMessage = ""
		subjectContent = "Performance Alert " + newestReport['SessionName'] + newestReport['Version']

		AverageFrameRate = newestReport['AverageFrameRate'] #帧率
		if AverageFrameRate < Paradise_AlarmFrame :
			warningMessage += newestReport['SessionName'] + " map runs low frames\n"
			needWarningMail = True

		ReservedTotalPeak = newestReport['ReservedTotalPeak'] #内存
		if ReservedTotalPeak > ReservedTotal_Alarm :
			warningMessage += newestReport['SessionName'] + "'s total reserved exceeds " + str(ReservedTotal_Alarm) + "\n"
			needWarningMail = True

		TrianglesPeak = newestReport['TrianglesPeak'] #资源
		if TrianglesPeak > TrianglesPeak_Alarm :
			warningMessage += newestReport['SessionName'] + "'s triangle peak exceeds " + str(TrianglesPeak_Alarm) + "\n"
			needWarningMail = True

		if needWarningMail :
			_mailHandle = MailHandle()
			subjectContent = "Performance Alert " + newestReport['SessionName'] + newestReport['Version']
			bodyContent = "Version: " + newestReport['Version'] + "\nData:" + \
			newestReport['Date'] + "\n" + warningMessage
			_mailHandle.mail(subjectContent, bodyContent)


if __name__ == "__main__":
	main()