a=int(input("Number of fresg loaves purchased:"))
b=int(input("Number of day old loaves purchased:"))
print("\n")
print("Regular prince:Rs.185")
print("Amount of new loaves:",a*185)
print("Amount of day loaves:",(a*185)*(60/100))
print("Total Amount to be paid:",(a*185)+((a*185)*(60/100)))
