marks={}
x=int(input("Bangla: "))
marks.update({"Bangla":x})
y=int(input("English: "))
marks.update({"English":y})
z=int(input("ICT: "))
marks.update({"ICT":z})
a=int(input("Physics: "))
marks.update({"Physics":a})
b=int(input("Chemistry: "))
marks.update({"Chemistry":b})
c=int(input("Math: "))
marks.update({"Math":c})
d=int(input("Biology: "))
marks.update({"Biology":d})
total_marks=sum(marks.values()) #total marks
num_of_sub=len(marks) #num of sub
avg_marks=total_marks / num_of_sub #avg marks
print("Num of subjects:",num_of_sub)
print("Total marks:",total_marks)
print("Avg Marks:",avg_marks )
if (avg_marks>=80):
    print("Grade: A+")
    print("GPA: 5.00")
elif(avg_marks<80 and avg_marks>=70):
    print("Grade: A")
    print("GPA: 4.50")
elif(avg_marks<70 and avg_marks>=60):
    print("Grade: A-")
    print("GPA: 4.00")
elif(avg_marks<60 and avg_marks>=50):
    print("Grade: B")
    print("GPA: 3.50")
elif(avg_marks<50 and avg_marks>=40):
    print("Grade: C")
    print("GPA: 3.00")
else:
    print("Grade: F")
    print("GPA: 0.00")
#if average_marks > 80: grade = "A+" else: grade = "Below A+"
print(marks)