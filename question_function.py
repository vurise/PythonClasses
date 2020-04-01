# question-
# take 2 inputs from the user - start number and end number
# define a function which prints all even numbers between start and end number including start and end number
# example : if the user inputs - 2 and 10 , the output should be 2 4 6 8 10

start = int(input("enter a start"))
end = int(input("enter end"))

def func(start,end):
    for i in range(start, end+1, 1):
        if i % 2 == 0:
            print(i)

func(start,end)


