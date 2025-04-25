ID=input("Enter the id: ")
print("ID:",ID)
mark= input("enter the mark: ")
print("The obtained mark is: ",mark) #showingmark
if(mark>="90"):
    print("A+")
    print("Well Done") #feedback
elif(mark<"90" and mark>="80"):
    print("A")
    print("Keep it up") #feedback
elif(mark<"80" and mark>="70"):
    print("B+")
    print("Try to work more") #feedback
elif(mark<"70" and mark>="60"):
    print("B-")
    print("You should start hardworking") #feedback
elif(mark<"60" and mark>="50"):
    print("C")
    print("Not so well.\nHardwork needed") #feedback
else:
    print("FAIL!\nFeeling Bad For You Dear.\nBetter Luck Next Time") #feedback