# Discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Getting user input
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calling function and printing result
final_price = calculate_discount(price, discount)

if final_price != price:
    print(f"Discount applied! Final price is: {final_price}")
else:
    print(f"No discount applied. Final price is: {price}")










# Function with parameters
def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
print (large_power(20,20))

# Divibility  by 10
def divisible_by_ten(num):
    if num % 10 == 0|10:
        return True
    else:
        return False
print(divisible_by_ten(47))
