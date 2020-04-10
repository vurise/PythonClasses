#quiz-1

#radius
#perimeter- method
#area - method
class circle():
    def __init__(self, rad):
        self.radius=rad
    def perimeter(self):
        return  2*3.14* self.radius
    def area(self):
        return 3.14* self.radius**2
    def print_all(self):
        print(str(self.radius) + " "+ str(self.perimeter()) + str(self.area()))

radius= int(input("enter radius"))

circle1=circle(radius)
circle1.print_all()


#quiz-2
class String_functions:
    def get_string(self):
        self.str= input("enter string")
    def print_string(self):
        self.str= self.str.upper()
        print(self.str)

str1= String_functions()

str1.get_string()

str2=String_functions()

str2.get_string()

str1.print_string()
str2.print_string()



#quiz-3


#construct a class parrot
#3 parrots jismei mei unke name and age pass karu from the user
# parrot 1 and parrot2 ko bologe sing a song xyz---- console- parrot_name is singing xyz
#dance(song)- parrot_name is dancing on song- parrot3

class parrot:

    def __init__(self, name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        print(self.name + ' is singing on ' + song)

    def dance(self,song):
        print(self.name + ' is dancing on ' + song)

parrot1=parrot(input("enter name"), int(input("enter age")))

parrot2=parrot(input("enter name"), int(input("enter age")))

parrot3=parrot(input("enter name"), int(input("enter age")))

parrot1.sing(input("enter song for parrot-1"))
parrot2.sing(input("enter song for parrot-2"))
parrot3.dance(input("enter song for parrot-3"))