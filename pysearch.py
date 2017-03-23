dslistbool = []
dslistssn = []
dirarray =[]
de =scandir.scadir(sys.argv[1])
while 1:
  	try:
      	d = de.next()
        dirarray.append = d.path
	except StopIterantion as _:
      	break
while i < len(dirarray)
	searchfile = open(dirarray[i])
		for line in searchfile:
        	if "HONORABLE" or "Honorable" in line: dslistbool.append = "eligible:true"
	searchfile.close()

