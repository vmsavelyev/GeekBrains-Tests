#6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

first_day_dist = float(input('Сколько км спортсмен пробежал в 1-й день  '))
need_dist = float(input('Введите необходимое количество км день  '))
day = int(1)

if day == 1:
    print(day, 'день =', '%.3f' % first_day_dist)

while True:
    first_day_dist = first_day_dist + (first_day_dist * 0.1)
    day = day + 1
    if first_day_dist >= need_dist:
        print(day, 'день =', '%.3f' % first_day_dist)
        break
    if first_day_dist < need_dist:
        print(day, 'день =', '%.3f' % first_day_dist)
        continue
