import json
path = "./simple_report_dev.json"
Paradise_AlarmFrame = 25

def main():
	with open(path,mode='r',encoding='utf-8') as demoJSON:
		sessionData = json.load(demoJSON)
		newestReport = sessionData['ReportList'][0]
		score = int(newestReport['Score'])
		AverageFrameRate = newestReport['AverageFrameRate']
		print(AverageFrameRate)
		if AverageFrameRate < Paradise_AlarmFrame :
			print("warning")

if __name__ == "__main__":
	main()