#Vars
i = 0
a = 0
dslistbool = []
dslistssn = []
dirarray =[]
import os
#Loops
#populate dirarray
for root,dirs, files in os.walk(r'.'):
    for file in files:
        if file.endswith('.txt'):
            dirarray.append(file)

while a < len(dirarray):
        print dirarray[a]
	print dslistbool[a]
        a=a+1
#populate bool array
while i < len(dirarray):

        searchfile = open(dirarray[i])
        for line in searchfile:
                if "HONORABLE" or "Honorable" in line: dslistbool.append("eligible:true")
        searchfile.close()
        i=i+1
