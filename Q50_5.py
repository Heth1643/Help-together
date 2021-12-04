num = int(input("Enter Number: "))
temp = num 
rev = 0

while num > 0:
    rem = num % 10
    rev = (rev*10) + rem
    num = num // 10
    
if rev == temp:
    print("Palindrone")
else:
    print("Not")
