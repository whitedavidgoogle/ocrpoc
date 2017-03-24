#Vars
i = 0
a = 0
b = 0
dslistbool = []
dslistssn = []
dirarray =[]
posresult = "true"
import os
#Loops

#populate dirarray
for root,dirs, files in os.walk(r'.'):
    for file in files:
        if file.endswith('.txt'):
            dirarray.append(file)


#populate bool array
while i < len(dirarray):
	searchfile = open(dirarray[i])
        for line in searchfile:
#		print dirarray[i]
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
