#functions-
#print() is a function - it helps to perform a specific task

def greeting(name, number,tent,message="hi guys",num=20): #default parameter -optional paramter
    print("hello"+ name)
    print(message)

#calling a function will exceute it
name= input("pls enter you name")

greeting(name,10,"a","hi",20) #parameters or arguments

#default arguments --

#quiz-1

def func(message, num=1):
    print(message * num)

func('Welcome')
func('Viewers', 3)


#quiz-2

def func(x = 1, y = 2):
    x = x + y
    y += 1
    print(x, y)
func(y = 2, x = 1)

# question-
# take 2 inputs from the user - start number and end number
# define a function which prints all even numbers between start and end number including start and end number
# example : if the user inputs - 2 and 10 , the output should be 2 4 6 8 10

start=int(input("enter a start"))
end=int(input("enter end"))

for i in range(start, end+1,1):
    if start%2==0:
        print(start)

