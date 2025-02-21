grade = 51
if grade > 90:
    print("A")
elif grade > 80:
    print("B")
elif grade > 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

grade = 51

def award(grade):
    if grade > 90:
        return "Deans List"
    if grade > 80:
        return "Honors"
    if grade >= 60:
        return "Passing"
    return "Failing"

r = award(51)
print(r)


