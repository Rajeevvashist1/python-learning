#   Numbers in Python 

#   number = 1234  , 3.14 (Float) , 3+5j (imaginary) , octal (0o) , binary(0b) , hexa (0x) 

import math
#print(math.floor(3.99))       #last or previous or smallest value 
#print(math.ceil(3.222))       #upper or next greatest value 
#print(math.trunc(-2.4))       #go towards 0 

#print(2 ** 1000)   #Python can handle large numbers this is it's beauty

import random
#print(random.random())
#print(random.randint(1,99))

my_list = ["Python" , "Anaconda " , "From" , "Strangers" , "things"]
#print(random.choice(my_list))

name = " Rajeev "

#print(random.choice(name))


#  Diffrent types of numberss

# print(oct(64))
# print(hex(64))
# print(bin(64))

# direct converstion to int (base 10)  taking the'64 ' as the next input like 16 , 8 , 2 

#print(int('64' , 16))

#Relatinoal operator :->>

#and , or

name = 1234
name2 = 1234

#print(name == name2)  #True

#print(name is name2)  #True

#print(True == 1)  #True
#print(True is 1)  #False


my_list = [ 1,2,3,4]
my_list2 = my_list
#print(my_list)
#print(my_list2)

#print(my_list == my_list2)  #True
#print(my_list is my_list2)  #True

#my_list[0] = 99
# print(my_list)
# print(my_list2)

my_list = [1,2,3,4]

#print(my_list == my_list2)   #True
#print(my_list is my_list2)   #False     BECAUSE THIS TIME WE HAVE CHANGED THE REFRENCE OF THE MY_LIST SO THEY ARE DIFFRENT NOW

my_list[0] = 9999

#print(my_list)
#print(my_list2)


#LEFT SHIFT   2<<1 , 2<<2

#RIGHT SHIFT   2>>1 , 2>>2 

print(True + 3)
print(True + True)

print(True << 2)
print(True >> 1)