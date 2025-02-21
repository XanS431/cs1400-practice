scores = [23, 18, 12, 16, 36, 20, 32]
people = [ "Rob", "Chance", "Jacob" , "Xander" , "Jade" , "Robert", "Genievive"]
for i in range(len(people)):
    print(people [i], "scored a" , scores[i], "on their ACT test for mathematics.")

total = 0
for i in range(len(scores)):
    total = total + scores[i]
print("Average ACT test score for Mathametics: " , total//len(scores))

Print_customers = ["Tom" , "Marlee", "Marian", "Bob", "Joe" , "Wayne", "Vivienne", "Bonnie"]
print ("Customers Today:")
for i in range(len(Print_customers)):
    print(f'{i + 1}. {Print_customers[i]}')

guest_list = ["Nathaniel", "Alex", "Alix", "Nicholas"]
tagAlong = print(guest_list + ["Xander"])
print(tagAlong)

points = [32, 98, 105, 102]
sum = 0
for n in points:
    if n >= 100:
        sum = sum + n
print(sum)