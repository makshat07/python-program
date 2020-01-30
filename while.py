n =1
a =[]
while n:
   print("Enter a number")
   b=int(input())
   if b==0:
       n=0
   elif b%2==0:
        a.append(b)

print("Your list is",list(set(a)))    
