a = 18
b = 12

limited_sum = print(a + b)

def limited_sum():
    if a + b == 30:
        return("Sum Valid!")
    else:
        return("Invalid")

print(limited_sum())

c = 7
d = print(10 - 3)

super_sevens = print(input("Choose c or d: "))

def super_sevens():
    if c or d == 7:
        return("Sevens Galore!!")
    else:
        return("Sorry, no sevens here.")

print(super_sevens())

num = 27

close_to_ten = print(num + 3)
i = 30
def close_to_ten(i):
    if i % 10 == 0 or i % 10 == 1 or i % 10 == 2 or i % 10 == 3:
        return(True)
    else:
        return(False)


print(close_to_ten(i))