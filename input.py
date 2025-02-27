name = input("Enter your name: ")
print("Your name is ", name)
print("Welcome " , name)

num = input("Enter a number: ")
num = int(num) # convert num from a string to a number
print("What is", num, "+ 5?") # had to use print to combine output values
ans = input()
ans = int(ans) # convert ans from a string to a number
if ans == num + 5:
    print("You are correct!!")
else:
    print("Incorrect.")

nameloop = input("Enter your name: ")
for i in range(10):
    print(nameloop)

guess_the_number = input("Guess the number: ")
number = 32
if number == 32:
    print("That's correct!")
else:
    print("That's incorrect. Keep trying!")

average = input("Score: ")
for i in range(i):
    print(average)