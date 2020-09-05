#author Eric Zhang ecz5032@psu.edu

gradeOneInput = input("Enter your course 1 letter grade: ") 
credit1 = input("Enter your course 1 credit: ")
credit1 = float(credit1)

if gradeOneInput == "A":
  gradeOne = float(4)
elif gradeOneInput == "A-":
  gradeOne = float(3.67)
elif gradeOneInput == "B+":
  gradeOne = float(3.33)
elif gradeOneInput == "B":
  gradeOne = float(3)
elif gradeOneInput == "B-":
  gradeOne = float(2.67)
elif gradeOneInput == "C+":
  gradeOne = float(2.33)
elif gradeOneInput == "C":
  gradeOne = float(2)
elif gradeOneInput == "D":
  gradeOne = float(1)
else:
  gradeOne = 0

print("Grade point for course 1 is: " +str(gradeOne))

gradeTwoInput = input("Enter your course 2 letter grade: ") 
credit2 = input("Enter your course 2 credit: ")
credit2 = float(credit2)

if gradeTwoInput == "A":
  gradeTwo = float(4)
elif gradeTwoInput == "A-":
  gradeTwo = float(3.67)
elif gradeTwoInput == "B+":
  gradeTwo = float(3.33)
elif gradeTwoInput == "B":
  gradeTwo = float(3)
elif gradeTwoInput == "B-":
  gradeTwo = float(2.67)
elif gradeTwoInput == "C+":
  gradeTwo = float(2.33)
elif gradeTwoInput == "C":
  gradeTwo = float(2)
elif gradeTwoInput == "D":
  gradeTwo = float(1)
else:
  gradeTwo = float(0)

print("Grade point for course 2 is: " +str(gradeTwo))

gradeThreeInput = input("Enter your course 3 letter grade: ") 
credit3 = input("Enter your course 3 credit: ")
credit3 = float(credit3)

if gradeThreeInput == "A":
  gradeThree = float(4)
elif gradeThreeInput == "A-":
  gradeThree = float(3.67)
elif gradeThreeInput == "B+":
  gradeThree = float(3.33)
elif gradeThreeInput == "B":
  gradeThree = float(3)
elif gradeThreeInput == "B-":
  gradeThree = float(2.67)
elif gradeThreeInput == "C+":
  gradeThree = float(2.33)
elif gradeThreeInput == "C":
  gradeThree = float(2)
elif gradeThreeInput == "D":
  gradeThree = float(1)
else:
  gradeThree = float(0)

print("Grade point for course 3 is: " +str(gradeThree))

GPA = (gradeOne * credit1 + gradeTwo * credit2+gradeThree * credit3) / (credit1+credit2+credit3)
print("Your GPA is: "+str(GPA))
