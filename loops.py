# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:16:24 2017

@author: Bhaskar Karn
"""
x=float(input("enter x"))
if x == 3:
    print ("x equals 3.")
elif x ==2:
    print ("x equals 2.")
else:
    print ("x equals something else.")
print ("this is outside the if")  

#for loops
for somechar in "hello world":
    print(somechar)
x= ['p','y','t','h','o','n']
for somechar in x:
    print(somechar) 
    
for (x,y) in [('a',1),('b',2),('c',3),('d',4)]:
    print(x)
    print(y) 
    
weekdays = ["mon","tue","wed","thu","fri","sat","sun"]
for x in weekdays:
    print(x) 
    
for y in range(15):
    print(y) 
    
x= [1,2,3,4,5,6]
for s in x:
    print(s+5) 
    
x = [1,2,3,4,5,6]
for s in x:
    s+=5
    print(s) 
    
x= [1,2,3,4,5,6] 
for s in x:
    if s in [2,3,4,5]:
        s+=5
    print(s) 
    
x = [1,2,3,4,5,6]
for s in x:
    if s%2 == 0:
        s+=5
    print(s) 
    
x=3
while x < 10:
    x = x + 1
    print("still in the loop.")
print("outside of the loop.")
    
x = 3
while x>10:
    x = x + 1
    print("still in the loop.")
print("outside the loop.") 

while 1:
    print("type ctrl-c to stop me!")
    
x = "spam"
while x:
    print(x)
    x = x[1:] 
    
while 1:
    name = input("apoorva")
    if name == "stop":
        break
age = input("5:")
print("hello",name,'=>',\
      int(age)**2) 


x = 10
while x:
    x = x-1
    if x % 2 !=0: 
        continue 
    print(x) 
    
x = 10
while x:
    if x % 2 ==0: 
        continue
    print(x) 
    
1 and 0
1 or 0
100 or 0
100 and 50

def myfun (b, c):
    return b + c     
myfun (3,4)

def hello ():
    name = str(input("enter your name:"))
    if name:
        print("hello" + str(name))
    else:
        print("hello world")
    return
hello() 

def hello():
    name = str (input("enter your name:"))
    age = (input("enter your age:"))
    if name:
        print("hello" + str(name))
        print("age" +age)
    else:
        print("helo world")
    return
hello() 

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
print(intersect("neena","meesha")) 

def union(seq1, seq2):
    res = []
    for x in seq1:
        res.append(x)
    for x in seq2:
        if x not in res:
            res.append(x)
    return res
print(union("neena","meesha")) 