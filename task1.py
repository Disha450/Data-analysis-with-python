#creating a list
car=["bmw","audi","porche","maruti"]  #list name car

#adding an element to the list 
car.append("tata punch")

#removing an element from list 
car.remove("audi")

#modifying an element in the list 
car[2]="mercedes"

print("updated list=",car)

########################################################

#dictionary in python 
info={

    "name":"Ishika choudhary",
    "age":20,
    "city":"moradabad"

}
#adding
info['gender']='female'

#removing
del info["age"]

#modifying
info['city']='rampur'
print("updated dictionary=",info)

##########################################################

#set operation
set={9,5,25,14,8}

#add element
set.add(45)

#remove
set.remove(25)

#modifying
set.add(18)
set.discard(8)

print("updated set=",set)
set.clear()
