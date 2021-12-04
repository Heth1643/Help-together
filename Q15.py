

amount = int(input("Enter Amount You want to withdraw: "))

print("required notes of 100 will be",int(amount / 100))
print("required notes of 50 will be",int((amount % 100) / 50))
print("required notes of 10 will be",int(((amount % 100) % 50) / 10))

