#Vars
i = 0
a = 0
dslistbool = []
dslistssn = []
dirarray =[]
posresult = "true"
import os
#Loops
#populate dirarray
for root,dirs, files in os.walk(r'ocrpoc/data/'):
    for file in files:
        if file.endswith('.txt'):
            dirarray.append(file)

while a < len(dirarray):
        print dirarray[a]
#	print dslistbool[a]
	a=a+1
#populate bool array
while i < len(dirarray):
	searchfile = open(dirarray[i])
        for line in searchfile:
		print i
               	if "HONORABLE" or "Honorable" in line: 
			dslistbool.append(posresult)
		i=i+1
        searchfile.close()
        #i=i+1
#regex for finding ssn
#def ssnfinder():


#dsinterleave method
#def interleavearray():
#while true:
