def sumFrom1ToN(n)
 :
    result=0
   
    for x in range(1, n+1) :
        if ((x%7)==0 or (x%3)==0):
            print()
        else:
            result=result+x
               
    return result 

n = 19
print("Sum of digits in numbers from 1 to", n, "is", sumdigits(n)) 
