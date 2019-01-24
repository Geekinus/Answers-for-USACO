""" 
	TASK: friday
	LANG: PYTHON3 
"""

with open("friday.in") as f:
	N = int(f.readline().strip("\n"))

numOfDaysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
numOfDays = 0
numOfDaysInWeeks = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(N):
	if (1900 + i) % 4 == 0 and (1900 + i) % 100 != 0:
		numOfDaysInMonths[1] = 29
	elif (1900 + i) % 400 == 0:
		numOfDaysInMonths[1] = 29
	else:
		numOfDaysInMonths[1] = 28

	for j in range(12):
		numOfDaysInWeeks[(numOfDays + 13) % 7] = numOfDaysInWeeks[(numOfDays + 13) % 7] + 1
		numOfDays = numOfDays + numOfDaysInMonths[j]

with open("friday.out", "w") as f:
	f.write(str(numOfDaysInWeeks[6]) + ' ' + str(numOfDaysInWeeks[0]) + ' ' + str(numOfDaysInWeeks[1]) + ' ' + str(numOfDaysInWeeks[2]) + ' ' + str(numOfDaysInWeeks[3]) + ' ' + str(numOfDaysInWeeks[4]) + ' ' + str(numOfDaysInWeeks[5]) + '\n')
