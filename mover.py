#move files matched with the string in move.txt

import os
from shutil import copyfile

# getting the current path
cwd = os.getcwd()
# path to move
toMove = os.path.join(os.getcwd(), "moved")
# get all the files in the cwd
dirFiles = os.listdir(cwd)

# create a new folder if it doesn't exist
if not os.path.exists(toMove):
	os.mkdir(toMove)

# create a list to store the names of files
list = []

# open the move.txt
with open('move.txt', 'r') as files:
	# read string line by line
	for file in files:
		# append the file name to list
		list.append(str(file).strip())
		# get a list of files in the cwd
		for df in dirFiles:
			# if string name matches file name or a part of it matches
			if str(file).strip() in str(df):
				temp = toMove+"\\"+df
				# move the file
				copyfile(cwd+'\\'+df, temp)
				# remove the string from list
				list.remove(str(file).strip())
# if list is empty all files moved successfully, otherwise shows a list of strings whose corresponding files were not found
print(list)
