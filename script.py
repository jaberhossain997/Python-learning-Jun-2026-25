# class 2 2026-25-jun
#String
#Length from typing import final

"""str1="ALii's"
len1=(len(str1))
print(len1)

str2="Collage"
len2=(len(str2))
print(len2)


All_str= str1 +" "+ str2
print(All_str)
print(len(All_str))"""


#indexing (inderect)
"""str="Alli's Collage"
ch=str[3]
print(ch)"""

"""#indexing (derect)
str="Alli's Collage"
print(str[6])"""

#slicing(index)   A p p l e
#                 0 1 2 3 4
#                -> -> -> ->  count from first
"""str="Alli's collage"
print(str[0:8]) # we need to do how many index we khow
print(str[1:])# when we need to go last but we don't khow where is last
print(str[0:len(str)]) #same like  ( when we need to go last but we don't khow where is last) this
"""
#slicing(Negative index)
#                 A p p l e
#                 4 3 2 1 0
#                 <- <- <- <- count from last


"""str= "apple"
print(str[-5 : -1])"""

#string Function (endswith)
"""str = "I learning python from youtube"
print(str.endswith("tube"))"""

#string Function (Capitalize)
"""str="i learning python from youtube"
str=str.capitalize() # if we want to change in old str (original str) we need to wrrite like this
print(str)

print(str.capitalize()) # this change in new strin not in old string
"""


##string Function (replace). reples old valu intu new valu ,

"""str = "I learning python from youtube"
print(str.replace("from","cowm"))"""


#string Function (find).it's find caracture is it exsist or not if it exsist give us first index
"""str ="I learning python from youtube"
print(str.find("from"))"""

#string Function (count).  show us how many time this word exist in our string
""""str="I learning python from youtube from"
print(str.count("f"))"""

#Practice Question
#write a peigrum to input user's first name & print it's leantd (Question)
"""
#solv by me
name= input("inter your name:")
len=(len(name))
print("leanth of your namr is",len)

#solv by teacher
name= input("inter your name:")
print("leanth of your name is ", len(name))
"""

#write a peigrum to find occurrence of '$' in a string  (question)
#solv by me (first), then teacher
"""str=" i love $ and $ or $ also $"
print(str.count("$"))
"""

#Conditional Statement (if, elif, else)
#if
"""age=21
if (age>=15):
    print("can vote ")"""

#also cna write (for this every time yes)
"""age=24
if(True):
    print("can vote")"""


#Conditional Statement elif
"""light="green"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")"""


num=5 # if we ren both are going to execute if we use if

"""if(num>2):
    print("Number grather then 2")
if(num>5):
    print("number not gratther then 5")"""

# if we use elif then chack first if true if true will execute if noe then chack elif

"""num=5

if(num>6):
   print("Number is grather then 2")
elif(num>3):
    print ("number is geather then 5")"""


# else
"""light = "black"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("lock")
else:
    print("light is brocken")
"""

#voting project
"""
age=18

if(age>=18):
    print("can vote ")
elif(age==17):
    print("you can vote next year")
else:
    print("can't vote")"""

#conditional statement
#own
"""marks= int(input("Enter user marks:-"))


if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=71:
    print("C")
elif marks<=70:
    print("D")
"""

#teacher

"""marks = int(input("Enter Student Maeks:-"))

if (marks>=90):
    grade="A"
elif(marks>=80 and marks<=90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"

print("your grade is ->", grade)
"""


#Nesting
"""age=34

if age>=18:
    if age>=80:\
        print("cannot")
    else:
        print("can drive")
else:
    print("can drive")
"""




#practice question
#Write a progrum to chack number entered by user is odd or even

"""num=int(input("enter number:"))

rem=num%2

if(rem==0):
    print("EVEN")
else:
    print("ODD")

"""
"""a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if(a>=b and a>=c):
    print("first number is grater then ",a)
elif(b >= c):
    print("second number is grater then ",b)
else:
    print(third number is grater then ",c)"""

"""x =int(input("enter number"))

if(x%7==0):
    print("mul ty of 7")
else:
    print("not a munty")"""