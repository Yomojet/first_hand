#TEJOMOY_DAS
#roll_number:2016274
class Student():
	def __init__(self,rollnum,fname,lname,prog,cgpa):     #constructor
		self.Rollnumber=rollnum
		self.FirstName=fname
		self.LastName=lname
		self.Program=prog
		self.CGPA=float(cgpa)
	
	def comes_before(self,other):
		if(self.Rollnumber[ :4] < other.Rollnumber[ :4]):
			return True
		elif(self.Rollnumber[ :4] == other.Rollnumber[ :4]):
			if(self.Program < other.Program):
				return True
			elif(self.Program == other.Program):
				if(self.CGPA > other.CGPA):
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	
