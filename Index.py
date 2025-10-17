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
