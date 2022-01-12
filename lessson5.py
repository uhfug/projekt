#exercise 1
'''
n = int(input('Введите число n: '))

def generator_of_nums(max_num):
   for num in range(1, max_num + 1, 2):
       yield num

odd_to_n = generator_of_nums(n)

print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(list(odd_to_n))
print()

#exercise 2
odd_to_n = (num for num in range(1, n + 1, 2))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(next(odd_to_n))
print(list(odd_to_n))
'''
#exercise 3

from itertools import zip_longest

tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]
tutors_and_klasses =  zip_longest(tutors, klasses)
for i in tutors_and_klasses:
    print(i)


'''
tutors_and_klasses =[(tutors, klasses) for tutors, klasses in zip(tutors, klasses)]
'''

print(tutors_and_klasses)

print((list(tutors_and_klasses)))