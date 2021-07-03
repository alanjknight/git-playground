#List
list_of_numbers = [1,2,3,4,5]
list_of_string = ["one", "two", "three", "four", "five"]
list_of_booleans = [False,True,True,False,True]
mixed_list = [1,'two','three',4,'five']
empty_list = []

print(list_of_numbers[0])
print(list_of_numbers[1])
print(list_of_numbers[-2])
print(list_of_numbers[1:3])
print(list_of_numbers[:3])
print(list_of_numbers[2:])

list_of_string[0] = "ONE"
print(list_of_string)

del list_of_string[0]
print(list_of_string)

list_of_string.remove("two")
print(list_of_string)

list_of_string.append("six")
print(list_of_string)

list_of_string.insert(0,"ONE")
print(list_of_string)

list_of_string.insert(1,"TWO")
print(list_of_string)

list_of_string2 = ["six","seven","eight","nine","ten"]
list_of_string3 = list_of_string + list_of_string2
print(list_of_string3)

list_of_string3.remove("six")
print(list_of_string3)

print(len(list_of_string3))