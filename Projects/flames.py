import random
import time

print("*****************************")  
print("***         FLAMES        ***")  
print("*****************************")  
  
 
name1=input("Type your name:")  
name2=input("Type your lovers name:")  
name1_=list(name1.lower()) 
name2_=list(name2.lower())

for i in name1_[:]:
    if i in name2_:
        name1_.remove(i)
        name2_.remove(i)




print(name1_ + name2_)
print(len(name1_ + name2_))
y = (name1_ + name2_)
x = len(name1_ + name2_)
#print(y)
#print(x)

print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
time.sleep(1)

if x == 1 or x == 7 or x == 13:
    print(f'{name1} and {name2} are FRIENDS')

elif x == 2 or x == 8 or x == 14:
    print(f'{name1} and {name2} are LOVERS')
            
elif x == 3 or x == 9 or x == 15:
    print(f'{name1} and {name2} are ADMIRERS')

elif x == 4 or x == 10 or x == 16:
    print(f'{name1} and {name2} are to be MARRIED')
            
elif x == 5 or x == 11 or x == 17:
    print(f'{name1} and {name2} are ENEMIES')
            
elif x == 6 or x == 12 or x == 18:
    print(f'{name1} and {name2} are SWEETHEARTS')                

else:
    pass    

        

        
    
+