  
import random  
import string
def Upper_Lower_string(n): # define the function and pass the length as argument  
        f=open("entrada.IN","w")
        f.write(str(n)+'\n')  

        for i in range(0,n):
            randd=random.randint(20, 200)
            result = ''.join((random.choice(string.ascii_lowercase) for x in range(randd))) # run loop until the define length  
            result2 = ''.join((random.choice(result) for x in range(2))) # run loop until the define length  
            m=random.randint(10, 100)
            f.write(result+' '+result2+' '+str(m)+'\n')  
      
       
      
Upper_Lower_string(1000000) # define the length  