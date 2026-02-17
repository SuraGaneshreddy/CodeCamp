#Write a program to input Principal Amount, Rate and Year and
#display Simple Interest
amount = int(input("Enter Principal Amount: "))
rate = int(input("Enter Rate of Interest: "))
years = int(input("Enter Number of Years: "))
si = (amount * rate * years) / 100
print("Simple Interest is: ",si) 