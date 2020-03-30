#string iteration
str= "vanshika"
for i in str:
  print(i)
for i in range(len(str)): # 8 ... 0 to 8
    print(str[i])

list=[1,2,3,4,5]
for i in list:
    print(i)
for i in range(len(list)):
    print(list[i])
for i in range(0,10,2): #initialize... end point...increment  ..end point is exclusive
    print(i)
for i in range(3): # initialise default- 0 and increment default is 1 ..end point should atleast be mentioned
    print(i)

for i in range(2,6): #initialise...end .. 2 3 4 5
    print(i)
#inner loops ..multiple loops

adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]

for i in adj:
    for j in fruits:
        print(i,j)

for i in adj:
    print(i)
for j in fruits:
    print(j)
#while loop:

x=1
while(x<=100): #jabtak condition false na ho jaye
    print(x)
    x=x+1

y=2
while(y<=40):
    print(y)
    y=y+2


#continue
#break
#they are used to exit the loop in between according to a condition

for i in fruits:
    if i=="banana":
        break;
    print(i) #apple

#they are used to skip the loop for that specific iteration

numbers=[1,2,3,4,5] # 1 3 5
for number in numbers:
    if number%2==0:
        continue; #jitni bhi neeche ki statements hai skip them
        print(number)









