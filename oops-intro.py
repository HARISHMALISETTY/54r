# OOPS---INTRO:
# -----------
# 1.POPS-->PROCEDURAL ORIENTED PROGRAMMING SYSTEM
# 2.FOPS-->FUNTIONAL ORIENTED PROGRAMMING SYSTEM
# 3.OOPS-->OBJECT ORIENTED PROGRAMMING SYSTEM

# POPS AND FOPS ARE NOT THAT MUCH SUITABLE FOR COMPLEX LEVEL PROJECTS.

# THEY ONLY FOCUS ON HOW TO USE DATA AND PERFORM OPERATIONS/COMPUTATIONS ON IT BUT NOT HOW TO SECURE IT.

# POPS--->CREATES SUB PROCEDURES AND PROCESS THE CODE
# FOPS-->IT WILL USES PURE FUNCTIONS I.E, RECURSIVE , MAP AND FILTER.

# OOPS WAS INTRODUCED BY ALAN KAY IN  1966 FOR SIMULATION PROGRAMMING.

# IT WAS DEVELOPED  AND WIDELY ADOPTED IN C++

# AND THEN

# JAVA
# PYTHON
# JS
# C
# PHP

# PYTHON WILL SUPPORTS ALL 3 TYPES OF PARADIGMS.SO WE CAN CALL IT AS A MULTI PARADIGM SUPPORTING LANGUAGE.

# OOPS IN PYTHON:
# ---------------
# 1.here programming style will completely based on the object oriented
# 2.we may require multiple objects . so each and every different object should have reference. that can be provided by class.
# 3.class is a blueprint for creating multiple objects. class is a boss for objects.
# 4.once we create object from the instance of class.
# 5.object should have 2 things in it -->properties and behaviour.



# everything in this universe can be consider as a object.
# 1.human being
# 2.pen
# 3.house
# 4.car
# 5.cycle and so on...

# For defining properties--->variable/attributes will use
# For defining Behaviour---->methods/procedure

# OOPS is widely used in

# AI
# EXPERT SYSTEMS
# CLIENT-SERVER MODELS
# DATABASES.

# concepts of oops:
# 1.class
# 2.object
# 3.inheritance
# 4.abstraction
# 5.polymorphism
# 6.encapsulation

# class ClassName:
# 	stst1-
# 	stst2-
# 	----
# 	----
# 	-----
# 	ststn-1
# 	ststn


# class SampleClass:
#     name="harish"
#     city="hyd"

# obj1=SampleClass() #creates one object
# obj2=SampleClass() #create one more object
# obj3=SampleClass()

# print(obj1)
# print(obj2)
# print(obj3)


class InstaGram:
    name="insta"
    source="meta"
    invented_by="Mark Jucker Burg"


insta1=InstaGram() 
insta2=InstaGram()
insta3=InstaGram()

# print(insta1,insta2,insta3)
print(insta1.name)
print(insta2.source)
print(InstaGram().invented_by)

insta1.name="fb"

print(insta1.name)
print(InstaGram().name)
