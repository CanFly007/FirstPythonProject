import json

from MailHandle import mailHandleIN

path = "./simple_report_dev.json"
Paradise_AlarmFrame = 25

def main():
	with open(path,mode='r',encoding='utf-8') as demoJSON:
		sessionData = json.load(demoJSON)
		newestReport = sessionData['ReportList'][0]
		score = int(newestReport['Score'])
		AverageFrameRate = newestReport['AverageFrameRate']
		if AverageFrameRate < Paradise_AlarmFrame :
			mailHandleINt = mailHandleIN()
			subjectContent = "Performance Alert " + newestReport['SessionName'] + newestReport['Version']
			bodyContent = "Version: " + newestReport['Version'] + "\nData:" + \
			newestReport['Date'] + "\nParadise map runs low frames"
			mailHandleINt.mail(subjectContent, bodyContent)

if __name__ == "__main__":
	main()