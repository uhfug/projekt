#exercise 1
import math

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 3))
print(type(15 ** 3))

#exercise 2
weather = ['в ', '5', ' часов ', '17', ' минут ', ' температура ', ' воздуха ', ' была ', '+5', ' градусов ']

for i in weather[0:]:
    if i == '5':
        weather[1] = '05'
        weather.insert(1, '"')
        weather.insert(3, '"')
    elif i == '17':
        weather.insert(5, '"')
        weather.insert(7, '"')
    elif i == '+5':
        weather[12] = '+05'
        weather.insert(12, '"')
        weather.insert(14, '"')

print("".join(weather))

#exercise 4
workers_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
just_names = []

for i in workers_names[0:]:
    caps_names = i.title()
    section = caps_names.split(' ')
    just_names.append(section[-1])

for i in just_names[0:]:
    print(f'Привет, {i}!')

#exercise 5
prices = [57.8, 467.51, 97, 6578.88, 76.3, 34.9, 34, 54.5, 65.37, 75, 43.5, 34.7]
low_prices = []
for i in prices:
    low_prices.append(i)
low_prices.sort(reverse=True)
print('До сортировки: ' + str(id(prices)))
prices.sort()

revers_coast = []
final_coast = []
for i in prices[0:]:
    coast = (str(i).split('.'))
    if coast[-1] == coast[0]:
        coast.append('00')
    elif int(coast[-1]) < 10:
        coast.append(f'0{coast[-1]}')
    final_coast.append(coast)
print(",".join(str(f'{coast[0]} руб {coast[-1]} коп')for coast in final_coast))


for i in low_prices[0:]:
    low_coast = (str(i).split('.'))
    if low_coast[-1] == low_coast[0]:
        low_coast.append('00')
    elif int(low_coast[-1]) < 10:
        low_coast.append(f'0{low_coast[-1]}')
    revers_coast.append(low_coast)
print(",".join(str(f'{low_coast[0]} руб {low_coast[-1]} коп')for low_coast in revers_coast))
print('Пятерка самых дорогих товаров: ' + (",".join(str(f'{low_coast[0]} руб {low_coast[-1]} коп')for low_coast in revers_coast[0:5])))
print('После сортировки: ' + str(id(prices)))
