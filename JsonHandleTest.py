#import JsonHandle
import json

path = "./demo.json"

def main():
	#jsonHandle = JsonHandle.JsonHandle(path)
	#jsonHandle.open()
	#print(jsonHandle.context["ReportList"])
	#jsonHandle.context["gf"] = "beautiful"
	#jsonHandle.save()
	#print(jsonHandle)

	with open(path,mode='r',encoding='utf-8') as demoJSON:
		sessionData = json.load(demoJSON)
		print(sessionData['ReportList'][0]['SessionId'])

if __name__ == "__main__":
	main()