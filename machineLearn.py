
def readTraining(filename):
	a_file = open(filename, "r")
	trainingSet = []
	for line in a_file:
		stripped_line = line.strip()
		line_list = stripped_line.split()
		trainingSet.append(line_list[0].split(','))
		#print(line_list[0].split(','))
	a_file.close()
	return trainingSet
	
def convert(lst):
	return (lst[0].split())


def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated



def buyingProb(separated, data, classifier):
	total = 0	# total occurances of classifer
	occ = 0	# occurances of data
	for label in separated:
		for row in separated[label]:
			if (label == classifier):
				total = total+1
				if(row[0] == data[0]):
					occ = occ+1
	prob = float(occ+1)/float(total)
	#print(occ+1, total, ' --- ', prob)
	return prob
		

def maintProb(separated, data, classifier):
	total = 0	# total occurances of classifer
	occ = 0	# occurances of data
	for label in separated:
		for row in separated[label]:
			if (label == classifier):
				total = total+1
				if(row[1] == data[1]):
					occ = occ+1
	prob = float(occ+1)/float(total)
	#print(occ+1, total, ' --- ', prob)
	return prob

def doorsProb(separated, data, classifier):
	total = 0	# total occurances of classifer
	occ = 0	# occurances of data
	for label in separated:
		for row in separated[label]:
			if (label == classifier):
				total = total+1
				if(row[2] == data[2]):
					occ = occ+1
	prob = float(occ+1)/float(total)
	#print(occ+1, total, ' --- ', prob)
	return prob

def personsProb(separated, data, classifier):
	total = 0	# total occurances of classifer
	occ = 0	# occurances of data
	for label in separated:
		for row in separated[label]:
			if (label == classifier):
				total = total+1
				if(row[3] == data[3]):
					occ = occ+1
	prob = float(occ+1)/float(total)
	#print(occ+1, total, ' --- ', prob)
	return prob

def lugBootProb(separated, data, classifier):
	total = 0	# total occurances of classifer
	occ = 0	# occurances of data
	for label in separated:
		for row in separated[label]:
			if (label == classifier):
				total = total+1
				if(row[4] == data[4]):
					occ = occ+1
	prob = float(occ+1)/float(total)
	#print(occ+1, total, ' --- ', prob)
	return prob

def safetyProb(separated, data, classifier):
	total = 0	# total occurances of classifer
	occ = 0	# occurances of data
	for label in separated:
		for row in separated[label]:
			if (label == classifier):
				total = total+1
				if(row[5] == data[5]):
					occ = occ+1
	prob = float(occ+1)/float(total)
	#print(occ+1, total, ' --- ', prob)
	return prob


def classProb(separated, classifier):
	total = 0	# total occurances of classifer
	occ = 0
	for label in separated:
		for row in separated[label]:
			if (label == classifier):
				occ = occ + 1
			total = total + 1	
	#print(occ, total, ' --- ', (occ/total))	
	return (occ/total)
	


def findGain(trainSet, testSet, classifier):
	buy = buyingProb(trainSet, testSet, classifier)
	maint = maintProb(trainSet, testSet, classifier)
	doors = doorsProb(trainSet, testSet, classifier)
	persons = personsProb(trainSet, testSet, classifier)
	lugBoot = lugBootProb(trainSet, testSet, classifier)
	safety = safetyProb(trainSet, testSet, classifier)
	classif = classProb(trainSet, classifier)

	# print(classifier)
	# print('buy:  ', buy)
	# print('maint:  ', maint)
	# print('doors:  ', doors)
	# print('persons:  ', persons)
	# print('lugBoot:  ', lugBoot)
	# print('safety:  ', safety)
	#print('class:  ', classif)
	gain = buy * maint * doors * persons * lugBoot * safety * classif
	#gain = gain / classif
	# print('Probability:  ', gain)
	# print()

	
	return gain


def findClass(line):
	return list[6]

def findBest(p1, p2, p3, p4):
	return (max(p1,p2,p3,p4))



trainSet = readTraining("carTrain.txt")	
trainSetSeparated = separate_by_class(trainSet)
	
testSet = readTraining("carTest.txt")
testSetSeparated = separate_by_class(testSet)

correct = 0
totalLearned = 0
unCount = 0
aCount = 0
gCount = 0
vCount = 0
for list in testSet:
	#print(list)
	unacc = findGain(trainSetSeparated, list, 'unacc')
	#print('unacc:  ', unacc)
	acc = findGain(trainSetSeparated, list, 'acc')
	#print('acc:  ', acc)
	good = findGain(trainSetSeparated, list, 'good')
	#print('good:  ', good)
	vgood = findGain(trainSetSeparated, list, 'vgood')
	#print('vgood:  ', vgood)
	highest = findBest(unacc, acc, good, vgood)
	if(highest == unacc):
		if(list[6] == 'unacc'):
			correct = correct +1
		unCount = unCount +1
		print(list, '  / unacc')
	elif(highest == acc):
		if(list[6] == 'acc'):
			correct = correct + 1
		aCount = aCount + 1
		print(list, '  / acc')
	elif(highest == good):
		if(list[6] == 'good'):
			correct = correct + 1
		gCount = gCount + 1
		print(list, '  / good')
	elif(highest == vgood):
		if(list[6] == 'vgood'):
			correct = correct + 1
		vCount = vCount +1
		print(list, '  / vgood')
	totalLearned = totalLearned + 1
	print()


print(totalLearned, ' instances in test data')
print(correct, ' correctly classified')
float = correct/totalLearned
format_float = "{:.2f}".format(float)
print('Accuracy = ', format_float)
print()



# unacc = findGain(trainSetSeparated, testSetSeparated, 'unacc')
# acc = findGain(trainSetSeparated, testSetSeparated, 'acc')
# good = findGain(trainSetSeparated, testSetSeparated, 'good')
# vgood = findGain(trainSetSeparated, testSetSeparated, 'vgood')

	# row 0 -> Buying
	# row 1 -> Maintenance
	# row 2 -> Doors
	# row 3 -> Persons
	# row 4 -> Lug Boot
	# row 5 -> Safety
	# row 6 -> Class