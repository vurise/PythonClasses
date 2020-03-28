 #list data structure

item1='pasta'
item2='sushi'
item3='noodles'

foods=['pasta', 'curry','sushi']
print(foods[0]) #pasta
print(foods[1]) #curry

#to iterate through the list we use loops
#for loop

# for loop
for food in foods:
    print('i' + 'like' + food)

#for loop and range
length= len(foods)

for i in range(length):
    print(foods[i])


#List comprehension method

list=[1,3,5,7]
[print(i) for i in list]

#properties-

foods.append('pizza')
print(foods)

foods[1]='noodles'
print(foods)

#dictionaries- (key, value pair)
fruits= { 'apple' : 'red' , 'banana' :'yellow', 'grapes':'black'}

print(fruits)

print(fruits['apple'])

#update
fruits['apple']='brown'
print(fruits)

#adding element
fruits['cherry']='red'
print(fruits)













