import time
import random
print("*****************************")  
print("***    Love Calculator    ***")  
print("*****************************")  
  
 
name1=input("Type your name:")  
name2=input("Type your lovers name:")  
name1=name1.lower()  
name2=name2.lower() 
names = name1 + name2
#print(names) 

t = names.count("t")  
r = names.count("r") 
u = names.count("u") 
e = names.count("e") 

true = t+r+u+e

l = names.count("l")  
o = names.count("o") 
v = names.count("v") 
e = names.count("e") 

love = l+o+v+e

love_score = int(str(true)+str(love))

print(love_score)



print("Calculating...")
time.sleep(random.randint(1,5))

print(f'{name1} and {name2} have a {love_score}% relationship.')

time.sleep(2)

if (love_score>=90):
    print("They have an unbreakable relationship that will last forever.")

elif (love_score<=89 and love_score>=70):
    print("They have a strong relationship that will most likely lead to a marriage.")

elif (love_score<=69 and love_score>=50):
    print("They have a good relationship that can lead to a honeymoon to Paris.")

elif (love_score<=49 and love_score>=20):
    print("They have a weak relationship that could have been a 'match made in heaven'.")
else:
  print("Do you really have to ask?")    
