#author Eric Zhang ecz5032@psu.edu

gradeOneInput = input("Enter your course 1 letter grade: ") 
credit1 = input("Enter your course 1 credit: ")
credit1 = float(credit1)

if gradeOneInput == "A":
  gradeOne = 4
elif gradeOneInput == "A-":
  gradeOne = 3.67
elif gradeOneInput == "B+":
  gradeOne = 3.33
elif gradeOneInput == "B":
  gradeOne = 3
elif gradeOneInput == "B-":
  gradeOne = 2.67
elif gradeOneInput == "C+":
  gradeOne = 2.33
elif gradeOneInput == "C":
  gradeOne = 2
elif gradeOneInput == "D":
  gradeOne = 1
else:
  gradeOne = 0

print("Grade point for course 1 is: " +str(gradeOne))

gradeTwoInput = input("Enter your course 2 letter grade: ") 
credit2 = input("Enter your course 2 credit: ")
credit2 = float(credit2)

if gradeTwoInput == "A":
  gradeTwo = 4
elif gradeTwoInput == "A-":
  gradeTwo = 3.67
elif gradeTwoInput == "B+":
  gradeTwo = 3.33
elif gradeTwoInput == "B":
  gradeTwo = 3
elif gradeTwoInput == "B-":
  gradeTwo = 2.67
elif gradeTwoInput == "C+":
  gradeTwo = 2.33
elif gradeTwoInput == "C":
  gradeTwo = 2
elif gradeTwoInput == "D":
  gradeTwo = 1
else:
  gradeTwo = 0

print("Grade point for course 2 is: " +str(gradeTwo))

gradeThreeInput = input("Enter your course 3 letter grade: ") 
credit3 = input("Enter your course 3 credit: ")
credit3 = float(credit3)

if gradeThreeInput == "A":
  gradeThree = 4
elif gradeThreeInput == "A-":
  gradeThree = 3.67
elif gradeThreeInput == "B+":
  gradeThree = 3.33
elif gradeThreeInput == "B":
  gradeThree = 3
elif gradeThreeInput == "B-":
  gradeThree = 2.67
elif gradeThreeInput == "C+":
  gradeThree = 2.33
elif gradeThreeInput == "C":
  gradeThree = 2
elif gradeThreeInput == "D":
  gradeThree = 1
else:
  gradeThree = 0

print("Grade point for course 3 is: " +str(gradeThree))

GPA = (gradeOne * credit1 + gradeTwo * credit2+gradeThree * credit3) / (credit1+credit2+credit3)
print("Your GPA is: "+str(GPA))
