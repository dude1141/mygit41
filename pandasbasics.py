#!/usr/bin/env python
# coding: utf-8

# In[1]:


cities=['hyd','guntur']


# In[ ]:





# In[3]:


city='Chennai'



if city in cities:
    print("ohyay")
print('program completed')


# In[6]:


n=int(input("e4nter value\n"))

if n==1:
    print("Enter value is one")
elif n==2:
    print("Enter value is 2")
else:
    print("values printed")
print("program completed")


# In[1]:


ch=input("Enter character")
vowels=['a','e','i','o','u']

if ch in vowels:
    print("Entered value is vowel")
else:
    print("not an owel")


# In[2]:


n=int(input("e4nter value\n"))

if n%2==1:
    print("Enter value is odd")
else:
    print("values is even")
print("program completed")


# In[2]:


x,y=0,1

while y<10:
    print(y)
    x,y=y,x+y


# In[2]:


dict = {1:20.5, 2:3.03, 3:23.22, 4:33.12}

dict[3]


# In[9]:


d = {'Red': 1, 'Green': 2, 'Blue': 4} 

for a,b in d.items():
    print(a,d[a])


# In[4]:


str1="ARYA"

# cnt=0

for i in str1:
    cnt+1
    print(i)
    


# In[22]:


def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
    
nterms=10


# In[23]:



if nterms<= 0:
    print("postive number")
else:
    for i in range(nterms):
        print(fib(i))  


# In[3]:


cities=['Hyderabad','Bengalore']
for i in cities:
    cities.append(i.upper())
print(cities)



# In[12]:


lsta=['srinivas','male',2000]
print(lst)
i=0;

for i in lsta:
#     i+=1
    print(i)


# In[16]:


lsta=['srinivas','male','2000']
res='#'.join(lst)
print(res)


# In[14]:


class Birds:
    wings=2
    eyes=3
a=Birds()

# a.eyes
# print("what is a"a)
print(a)
    
    


# In[35]:


class Birds:
    wings=2
    eyes=3
    def fly():
        print("i can fly ")
a=Birds()


# a.eyes
# print("what is a"a)
# Birds.fly()    
print(a)
    


# In[44]:


class Birds:
    wings=2
    eyes=3
    def fly(self):
        print("i can fly ")
    def display(self):
        print("display birds information")
a=Birds()
# a.eyes
a.fly()
a.display()

# //self can access all variables in class
# 


# In[49]:


class School:
    school='DPS'
    loc='PKL'
    def prints(self):
        print("school------------------->",self.school)
        print("loc--------------------->",self.loc)        
    def display(self):
        print("display school information")
s1=School()
# a.eyes
s1.prints()
s1.display()

# //self can access all variables in class
# 


# In[60]:


class Computer:
    def __init__(self,cpu,ram):
            self.cpu=cpu
            self.ram=ram
            
    def display(self):
        print("display comp information",self.cpu,self.ram)
        
c1=Computer('8','64')
c2=Computer('10','120')

# c1---this is object
# display()--automatically calls init 


c1.display()
c2.display()


        
        
        
# //self can access all variables in class
# 


# In[64]:


class Computer:
#     def __init__(self,pu,ram):
#             self.cpu=cpu
#             self.ram=ram
            
    def display(self):
        print("display comp information------>",'15','25')
        
c1=Computer()
c2=Computer()

# c1---this is object
# display()--automatically calls init 


c1.display()
c2.display()


        
        
        
# //self can access all variables in class
# 


# In[ ]:





# In[75]:


class Computer:
    def __init__(self,cpu,ram):
          self.cpu=cpu
          self.ram=ram
            
    def display(self):
        print("computer information------>",self.cpu,self.ram)
        print("computer information------>")

c1=Computer('15','25')

# c1 here is equaivalent to (self,'15','25')
# here you are passing three parameters self,15,25---self is by default
c2=Computer('21','44')

# c1---this is object
# display()--automatically calls init 


c1.display()
c2.display()


        
        
        
# //self can access all variables in class
# 


# In[7]:


class Flat:
    x=2
    def display():
        print("rooms",self.x)
f1=Flat()
print(f1.display())
f1.display()
# f1.display() is equivalent to Flat.info(f1)
# position parameters expecting value here in the definition




# In[37]:


class Flat:
    x=2
    def display(self):
        print("rooms#######################",self.x)
    def display2(self):
        print("rooms")

f1=Flat()
f1.display()
f1.display2()
# f1.display() is equivalent to Flat.info(f1)


# In[31]:


class Student:
    
    def abc(self):
        print("student information")
    
    def __init__(self):
        print("student informationssss")
        
    s1=Student()
#     s1.abc()
    
#     when you create a object ,initialisation method(init) is called in python 
#     s1
        
        
    


# In[48]:


class Flat:
    room =2
    def abc(self):
        print("student information$$$$$$$$$$$$$$$$$")
        print("rooms=",self.room)
        print("student information")
#     def abc(self):
#         print("student information$$$$$$$$$$$$$$$$$")
#         print("rooms=",self.room)
#         print("student information")
        
s1=Flat()
s1.abc()
# s1
      
    
    


# In[59]:


class Flat:
    room =2
    def abc(self):
        print("student information$$$$$$$$$$$$$$$$$")
        print("rooms=",self.room)
        print("student information")
        self.color='blue'
#     def abc(self):
#         print("student information$$$$$$$$$$$$$$$$$")
#         print("rooms=",self.room)
#         print("student information")
        
s1=Flat()
s1.abc()
# s1.color()
# print("color################=",s1.color())
print("color=",s1.color)
# s1
      
    
    


# In[1]:


from pyspark.sql import Row


# In[7]:


data =[Row(id=101,name='Mithelesh'),Row(id=102,name='Mounica')]


# In[8]:


sqlContext=SQLContext(sc)


# In[9]:


df=sqlContext.createDataFrame(data)
df.show()


# In[9]:


a = range(1, 10)
print(type(a))



for x in a:
    print(x)


# In[10]:


import pandas as pd

df=pd.read_csv("C:\\Users\\solas\\Downloads\\developer_survey_2019\\survey_results_public.csv")

df.shape


# In[13]:


df=pd.read_csv("C:\\Users\\solas\\Downloads\\developer_survey_2019\\survey_results_schema.csv")
df.head(10)


# In[16]:


data=[['p',1],['q',2]]
df=pd.DataFrame(data,columns=['Letter','Number'])
df

