hourSec = int(input('введите часы (в секундах) '))
minSec = int(input('введите минуты (в секундах) '))
sec = int(input('введите секунды '))

hour = str (hourSec // 3600)
min = minSec // 60
print(f'0{hour}: 0{min}: {sec}')
