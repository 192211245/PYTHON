E=[]
L=[]
T=int(input("Enter value of T:"))
for i in range(T):
    e=int(input("Enter the entry list:"))
    E.append(e)
print("\n")
for i in range(T):
    l=int(input("Enter the leaving list:"))
    L.append(l)
print(L)
print("\n")
Sum=0
Max=0
for i in range(T):
    Sum+=E[i]-l[I]
    Max=max(Sum,Max)
print("Maximun no.og guests present on crusises:",Max)
