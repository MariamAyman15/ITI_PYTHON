import csv

f1= ['Name','Branch','Data of birth','Gpa'] 
a=[['Mina','ASSUIT',1998,2.85],['Moussa','ASSUIT',1999,3],['Asem','ASSUIT',199,2.77]]

f2=open("min.csv","w",newline='') #to prevent printing empety line

writer=csv.writer(f2)
writer.writerow(f1)
writer.writerows(a)
f2.close()

f3=open("min.csv")
reader=csv.reader(f3)
h=next(reader)
rows=[]

for row in reader:
	rows.append(row)
print(h)
print(rows)



