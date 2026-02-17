#Write a program to input Principal Amount, Rate and Year and
#display Compound Interest
amount = int(input("Enter Principal Amount: "))
rate = int(input("Enter Rate of Interest: "))
years = int(input("Enter Number of Years: "))
cp = amount * (pow((1 + rate / 100), years)) - amount
print("Compound Interest is:",cp)