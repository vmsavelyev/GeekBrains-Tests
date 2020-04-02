firstDayDist = float(input('Сколько км спортсмен пробежал в 1-й день  '))
needDist = float(input('Введите необходимое количество км день  '))
day = int(1)

if day == 1:
    print(day, 'день =', '%.3f' % firstDayDist)

while True:
    firstDayDist = firstDayDist + (firstDayDist*0.1)
    day = day + 1
    if firstDayDist >= needDist:
        print(day, 'день =', '%.3f' % firstDayDist)
        break
    if firstDayDist < needDist:
        print(day, 'день =', '%.3f' % firstDayDist)
        continue