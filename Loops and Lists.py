paychecks = [238 , 105 , 265 , 198 , 202 , 98]

def even_bonus(paychecks):
    new_paychecks = []
    for i in paychecks:
         new_paychecks.append (i + 50)
    return (new_paychecks)

print(even_bonus(paychecks))