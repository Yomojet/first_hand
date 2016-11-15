#Tejomoy_Das
#Roll_number:2016274
from StudentRecord import *
def FileToStringList(filename):
	L=[]
	with open(filename) as F:
		for s in F:
			s1=s.rstrip("\n")
			s2=s1.rstrip("\r")
			L.append(s2)
		return L

def readrecords(filename):
	list=[]
	Records=FileToStringList(filename)
	for record in Records:
		space=record.split(' ')
		new=Student(space[0],space[1],space[2],space[3],space[4])
		list.append(new)
	return list


def order_records(studentlist):
	i=0
	while(i<len(studentlist)-1):
		j=1
		while(j<len(studentlist)-i):
			if(studentlist[j].comes_before(studentlist[j-1])==True):
				temp=studentlist[j]
				studentlist[j]=studentlist[j-1]
				studentlist[j-1]=temp
			j=j+1
		i=i+1
	return studentlist

def display_ordered_data(orderedlist):
	for i in range(len(orderedlist)):
		print(orderedlist[i].Rollnumber,orderedlist[i].FirstName,orderedlist[i].LastName,orderedlist[i].Program,orderedlist[i].CGPA)

a=readrecords("studentdata.txt")
b=order_records(a)
display_ordered_data(b)
