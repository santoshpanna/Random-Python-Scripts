# Description - To Calculate Total Classes in a semester

import datetime

# Starting date of semester
start_date = datetime.date(2019, 7, 16)
# Last date of semester
end_date = datetime.date(2019, 11, 20)

# Internal values
delta = datetime.timedelta(days=1)

#subjects
subjects = {
	'CG' : 0,
	'SSM' : 0,
	'OT' : 0,
	'FOO' : 0,
	'BAR' : 0,
	'LCG' : 0,
	'LSSM' : 0
}

# Date of holidays
holidays = [datetime.date(2019, 8, 12),
		 	datetime.date(2019, 8, 15),
		 	datetime.date(2019, 8, 23),
		 	datetime.date(2019, 9, 9),
		 	datetime.date(2019, 9, 10),
		 	datetime.date(2019, 9, 17), 
		 	datetime.date(2019, 10, 2),
		 	datetime.date(2019, 10, 5),
		 	datetime.date(2019, 10, 6),
		 	datetime.date(2019, 10, 7),
		 	datetime.date(2019, 10, 8),
		 	datetime.date(2019, 10, 27),
		 	datetime.date(2019, 11, 2),
		 	datetime.date(2019, 11, 10),
		 	datetime.date(2019, 11, 12),
		 	datetime.date(2019, 11, 15)]

# Lectures of the day
# 0 - Monday , 1 - Tuesday, 2 - Wednesday, 3 - Thursday, 4 - Friday, 5 - Saturday, 6 - Sunday
time_table = {0:'CG-SSM', 1:'FOO-BAR', 2:'FOO-BAR-CG', 3:'SSM-LCG', 4:'LSSM-BAR-OT'}
# Include days where days are off eg weekends (Saturday and Sunday)
weekend = set([5, 6])

while start_date <= end_date:
	if start_date.weekday() not in weekend and start_date not in holidays:
		#print('{}\n'.format(start_date))
		subs = time_table[start_date.weekday()].split("-")
		for sub in subs:
			subjects[sub] = subjects[sub] + 1
	start_date += delta

#updating weights
subjects['LCG'] = subjects['LCG'] * 3
subjects['LSSM'] = subjects['LSSM'] * 3

for key, value in subjects.items():
	print(str(key)+"\t"+str(value)+"\t"+"["+str(round((value/100)*75))+"|"+str(round((value/100)*25))+"]"+"\t"+"["+str(round((value/100)*65))+"|"+str(round((value/100)*35))+"]")
