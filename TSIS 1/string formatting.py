price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))


price = 49
count = 3
itemno = 567
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(count, itemno, price))

price = 49
quantity = 3
itemno = 567
myorder= "I want {0} pieces of item number {1} for {2: .2f} dollars"
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "his name is {1}. {1} is {0} years old."
print(txt.format(age, name))


myorder = "I have {carname}, it is a {model}"
print(myorder.format(carname = 'toyota', model = 'camry' ))