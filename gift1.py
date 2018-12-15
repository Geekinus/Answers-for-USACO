"""
	TASK: gift1
	LANG: PYTHON3 
"""

from collections import OrderedDict

f = open("gift1.in")
numOfGiftGiver = int(f.readline().strip("\n"))
collectionOfGiftGivers = OrderedDict()
for i in range(numOfGiftGiver):
	collectionOfGiftGivers[f.readline().strip("\n")] = 0

for i in range(numOfGiftGiver):
	theNameOfGiftGiver = f.readline().strip("\n")
	howToSplit = f.readline().strip("\n").split()
	howMuch = int(howToSplit[0])
	howMany = int(howToSplit[1])

	collectionOfGiftGivers[theNameOfGiftGiver] = collectionOfGiftGivers[theNameOfGiftGiver] - howMuch

	if howMany != 0:
		for j in range(howMany):
			theName = f.readline().strip("\n")
			collectionOfGiftGivers[theName] = howMuch // howMany + collectionOfGiftGivers[theName]
		collectionOfGiftGivers[theNameOfGiftGiver] = collectionOfGiftGivers[theNameOfGiftGiver] + howMuch % howMany
	else:
		collectionOfGiftGivers[theNameOfGiftGiver] = collectionOfGiftGivers[theNameOfGiftGiver] + howMuch

f.close()
f = open("gift1.out", "w")
for i in collectionOfGiftGivers.keys():
	f.write(i + " " + str(collectionOfGiftGivers[i]) + '\n')
f.close()
