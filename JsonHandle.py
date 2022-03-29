import json

class JsonHandle():
	file_path = ""
	context = None
	__file_handle = None
	def __init__(self,path):
		self.file_path = path

	def open(self):
		self.__file_handle = open(self.file_path,mode='r',encoding='utf-8')
		text = self.__file_handle.read()
		self.context = json.loads(text)
		self.__file_handle.close()
		self.__file_handle = None

	def save(self):
		if self.context:
			self.__file_handle=open(self.file_path,mode='w',encoding='utf-8')
			json.dump(self.context,self.__file_handle,ensure_ascii=False,indent=4)
			self.__file_handle.close()
			self.__file_handle = None

	def __del__(self):
		if self.__file_handle:
			self.__file_handle.close()

	def __repr__(self):
		if self.context:
			text = json.dumps(self.context,ensure_ascii=False,indent=4)
			return text
		return ""
