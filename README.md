# ocrpoc
psuedo code
#requirements
scan txt for Honorable & HONORABLE & set boolean
scan txt for 9 digit number
input both in array
pass array to Datastore write method
auth with GCP
write array contents to datastore
each text file becomes its own array
    format as follows:
        kind: discharge
        ssn:9#
        eligible:true/false
declare list array
declare datastore payload array
make list of files in dir and populate list array
scan file 1 
    find ssn
    set array element with int
    find honorable
    set datastore payload array boolean
close file
iterate for list array length

