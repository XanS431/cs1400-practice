words = ["school" , "pencils" , "paper" , "lunchbox" , "books" , "bus"]


def hyphenate():
    print(words)
    for w in words:
        print(w, end=" - ")

hyphenate()

n = 6

s = "Pie"

def repeater(s , n):
    for x in range(n):
        print(s)

repeater(s , n)