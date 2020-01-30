a =[]
for i in range(11):
   n=int(input())
   if n%2==0:
        a.append(n)

print("Your list is",list(set(a)))    
