#classes encapsulates 2 thngs- variables / attributes and functions/methods
#recangle class-

#length -var
#width- var
#area- funct/ method / var
#perimeter - funct
#diagnol- var
#color- func

#constructor/ init method
#1. function
#2. this function gets automatically invoked when i make an instance
#3. to intialise variables in my class


class rectangle(): #create class
    def __init__(self,l,w): # jo bhi instance iss function ko call karega vo uski values lega  #self= rectangle1
        self.length=l #length is an attribute of the class
        self.width=w #width is an attribute
        self.area1=0;


    def area(self):
        self.area1= self.length * self.width
        return self.area1


l=int(input("enter length"))
w=int(input("enter width"))

rectangle1 = rectangle(l,w) # i have made an instance rectangle1 of class rectangle
#rectangle1.area()

print(rectangle1.length )
print(rectangle1.width)
print(rectangle1.area1)



#print(str(rectangle1.length)+" "+ str(rectangle1.width))



# whenever i call a varibale or a method from an object/instance i will have to use the dot operator
#print(rectangle1.length)













