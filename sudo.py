from random import randint
import json
from glob import glob

command = input(" >> ")

InTerm = True
while InTerm:
	if command == "clear":
		#try:
		with open("DebugMeta.json", "r") as meta:
			File2Clear = json.load(meta)["clear"]
			print(glob(f"**/SnS-AI/*/{File2Clear}"))
			with open(glob(f"**/SnS-AI/*/{File2Clear}")[0], "w") as file:
				file.write("")
		'''except:
			print(" > no file or invalid file")
			file = input(" enter file >> ")
			with open("DebugMeta.json", "w") as meta:
				json.dump({"clear" : file}, meta)'''
				
		command = input(" >> ")
	elif command == "quit":
		InTerm = False
	else:
		print(" >> invalid command")