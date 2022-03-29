import JsonHandle
path = "./demo.json"

def main():
	jsonHandle = JsonHandle.JsonHandle(path)
	jsonHandle.open()
	jsonHandle.context["gf"] = "beautiful"
	jsonHandle.save()
	print(jsonHandle)

if __name__ == "__main__":
	main()