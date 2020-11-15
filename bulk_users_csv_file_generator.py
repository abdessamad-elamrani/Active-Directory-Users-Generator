import sys
f = open("bulk_users1.csv", "a")

print("-----------Welcome------------")
print()
print ("How many Users you want to generate?  ")
print()

n = int(sys.stdin.readline())

print()

print("The CSV file will be written to current folder, name of the file : bulk_users1.csv")

print()

f.write ("firstname,middleInitial,lastname,username,email,streetaddress,city,zipcode,state,country,department,password,telephone,jobtitle,company,ou\n")
for i in range (1,n+1):
	f.write ('client'+str(i)+',,,client'+str(i)+',client'+str(i)+'@lab.local,1800 Street Amster,Amsterdam,72002,FL,Netherlands,Engineering,1fortinet!,+3142300239,EnginneeringSpecialists,AD Pro,"CN=Users,DC=lab,DC=local"\n')

print("finished")

f.close()
