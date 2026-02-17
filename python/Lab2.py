price = int(input("Enter Your Price: "))
if price <= 0 :
    print("The price should be greater than 0")

discount = int(input("Enter discount: "))
if not 0 < discount < 100:
    print("The discount should be between 0 and 100")
apply_discount = price - (price*discount/100)
print("The total amount",apply_discount)