
# print("hello")

# a=10;
# b=20;

# print(a+b)

# a=input();
# print("you entered the number is ",a)

# a=100;
# 100=literals

#constant is a vairable whos value can't be changed

#pi=3.14,pi is a constant and pi is a variable

# print(type(100))

# b=1.5
# b=int(b);
# print(type(b))

# a=tuple([10,1,3,4,5,6])
# b=list(a)
# b[0]=87
# print(b)

#print(ord("a"))=prints ascii value

# a=67
# print(chr(a))=prints alphabets


# a=10
# if a<20:
#     print("Welcome")

# age=9

# if age>18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")


# print(chr(65))

# print(ord('a'))


# b="male"

# print("a" in "bang")
# print("a" not in "bang")

# print("b" is  "male")
# print("b" is not "male")


# num=int(input("enter the number"))

# if num%2==0:
#     print("it is a even")

# else:
#     print("it is a odd")


# item=input("enter the phone : ")
# if item=="mi":
#     print("your is mi")
# elif item=="sumsung":
#     print("your phone is sumsung")
# else:
#     print("nin janmuke phone bere kedu")


# a=10

# if a>5:
#     if a>3:
#         print(a,"is greater")


# i=0
# while i<=10:
#     print("hello")
#     i=i+1


# for i in "welcome":
#     print(i)


# w="sunny"

# if w=="sunny" or w=="rainy":
#     print("correct")
# else:
#     print("wrong")


#Caculator

# num1=int(input("enter the num1 : "))
# num2=int(input("enter the num2 : "))

# oper=input("enter the operator : ")

# if oper=="+":
#     print(num1+num2)
# elif oper=="-":
#     print(num1-num2)
# elif oper=="*":
#     print(num1*num2)
# elif oper=="/":
#     print(num1/num2)
# else:
#     print("invalid operator")


# str="akash"

# print(str[0])

#Slicing

# name="abcdefghijklnmopqrstuvwxyz"

# print(len(name))

# print(name[0:4:2])

# print(name[::-1])

# print(name.upper())
# print(name.lower())
# print(len(name))
# print(name.replace('b','a'))
# print(name.count('a'))

# print("hello\"s world")


# name="Hello, World!"

# smaller=name.lower()

# a=smaller.count('a')
# e=smaller.count('e')
# i=smaller.count('i')
# o=smaller.count('o')
# u=smaller.count('u')

# print(f"number of vowels are :{a+e+i+o+u}")


# math=int(input("enter the math marks : "))
# Science=int(input("enter the Science marks : "))
# English=int(input("enter the English marks : "))

# total=math+Science+English
# print(f"Total Marks : {total}")
# Average=total/3
# print(f"Average Marks : {Average}")

# if(Average>=65) and (Average<=75):
#     print("B")
# elif(Average>=75) and (Average<=90):
#     print("B+")
# else:
#     print("A")




# name=input("Enter the name : ")

# name1=name[::-1]

# if name==name1:
#     print(f"{name} is a palindrome")
# else:
#     print(f"{name} is not a palindrome")


import math as m
a =int(input("Enter a number"))
res = int(m.log10(a)+1)
print(res)