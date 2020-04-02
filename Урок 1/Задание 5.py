revenue = float(input('Введите выручку фирмы  '))
coast = float(input('Введите издержки фирмы '))

if revenue > coast:
    profit = revenue - coast
    print('Ваша  прибыль', profit)
    rent = profit/coast
    print('Ваша рентабельность равна ', rent)
    pers = int(input('Введите численность персонала '))
    profPerPers = pers / profit
    print('прибыль на одного сотрудника равна ', profPerPers)
else:
    print('Вы работаете в убыток')




