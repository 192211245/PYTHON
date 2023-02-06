a=int(input('enter a number:'))
b=int(input('enter another number:'))
count=0
for i in range(1,min(a,b)+1):
    if a%1==b%i==0:
        count+=1
print(count)
