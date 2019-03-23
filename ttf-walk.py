#move all .ttf file from subdirectories to one directory for easier installation

import os

cwd = os.getcwd()
toMove = os.path.join(os.getcwd(), "all")

print (cwd)
print (toMove)

for root, dirs, files in os.walk(cwd):
	for file in files:
		if file.endswith((".ttf")):
			temp = toMove+"\\"+file
			if not os.path.isfile(temp):
				os.rename(root+"\\"+file, temp)