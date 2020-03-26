marks= input("enter your marks")  # takes input "45"

marks=int(marks)
grade=""

if marks< 25:
    grade="F"
elif marks>=25 and marks<45:
    grade="E"
elif marks>=45 and marks<65:
    grade="D"
elif marks>=65 and marks<85:
    grade="C"
elif marks>88:
    grade="C"



print(grade)


