# Description - To Calculate Total Classes in a semester

import datetime

# Starting date of semester
start_date = datetime.date(2019, 1, 10)
# Last date of semester
end_date = datetime.date(2019, 4, 19)

# Internal values
delta = datetime.timedelta(days=1)

# Date of holidays
holidays = [datetime.date(2019, 1, 15),
		 	datetime.date(2019, 1, 26),
		 	datetime.date(2019, 2, 10),
		 	datetime.date(2019, 3, 4),
		 	datetime.date(2019, 3, 24),
		 	datetime.date(2019, 4, 8), 
		 	datetime.date(2019, 4, 13),
		 	datetime.date(2019, 4, 14),
		 	datetime.date(2019, 4, 17),
		 	datetime.date(2019, 4, 19)]

# Lectures of the day
# 0 - Monday , 1 - Tuesday, 2 - Wednesday, 3 - Thursday, 4 - Friday, 5 - Saturday, 6 - Sunday
time_table = {0:'IPC-SPM-CD-DCCN', 1:'CFA-CFA-DCCN-CD-SPM', 2:'IPC-LCD-CFA', 3:'CD-CD-SPM', 4:'IPC-LCN-DCCN'}
# Include days where days are off eg weekends (Saturday and Sunday)
weekend = set([5, 6])

# Initializing lectures values
ipc = spm = cd = dccn = cfa = lcn = lcd = 0

while start_date <= end_date:
	if start_date.weekday() not in weekend and start_date not in holidays:
		print('{}\n'.format(start_date))
		subjects = time_table[start_date.weekday()].split("-")
		for subject in subjects:
			if subject == 'IPC':
				ipc += 1
			if subject == 'SPM':
				spm += 1
			if subject == 'CFA':
				cfa += 1
			if subject == 'CD':
				cd += 1
			if subject == 'DCCN':
				dccn += 1
			if subject == 'LCD':
				lcd += 3
			if subject == 'LCN':
				lcn += 3
	start_date += delta 

print("Total no of classes\nIPC = {}\nSPM = {}\nCD = {}\nDCCN = {}\nCFA = {}\nLCD = {}\nLCN = {}".format(ipc,spm,cd,dccn,cfa,lcd,lcn))
