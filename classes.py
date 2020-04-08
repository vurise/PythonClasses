class Menu:#mostly we write functions in class
    #pass
    def hello(self,name):#self mei object(MI-1) ki copy bana lega
        return self.name
menu_item1=Menu()#empty object,1 st time we went to class
menu_item1.name='sandwich'
menu_item1.price="$5"
print(menu_item1.hello())
#print(menu_item1.name+"->"+menu_item1.price)
menu_item2=Menu()#2nd time
#menu_item2.hello()
#menu_item2.name='choco cake'
#menu_item2.price="$2"
#menu_item3=Menu()#3rd time
#menu_item3.name='orange juice'
#menu_item3.price="$3"
#print(menu_item2.name+"->"+menu_item2.price)
#print(menu_item3.name+"->"+menu_item3.price)

