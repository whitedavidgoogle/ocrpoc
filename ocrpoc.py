from google.cloud import datastore

def create_client(project_id):
    return datastore.Client(project_id)

def add(discharge, HONORABLE):
    key = discharge.key(

String result = false

print "What is the file name?"
filename = raw_input()



def transfer_funds(client, from_key, to_key, amount):
    with client.transaction():
        from_account = client.get(from_key)
        to_account = client.get(to_key)

        from_account['balance'] -= amount
        to_account['balance'] += amount

        client.put_multi([from_account, to_account])

searchfile = open(filename)
for line in searchfile:
        if "HONORABLE" or "Honorable" in line: print "yes" and result = true
searchfile.close()

#populate an array to write filename and result

#def dbwrite()
        #insert datastore write here	
