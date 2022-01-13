#exercise 1

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

#exercise 3

tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А',
    ]

tutors_and_klasses =(
    (tutors[i], None) if i >= len(klasses)
    else (tutors[i], klasses[i])
    for i in range(len(tutors))
)

print(type(tutors_and_klasses), *tutors_and_klasses)

#exercise 4
<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> old

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_num = []

result = (
    result_num.append(src[i]) if i != 0 and src[i] > src[i - 1]
    else ()
    for i in range(len(src))
)

(list(result))
print(result_num)
<<<<<<< HEAD

#exercise 5

src_exercise_5 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

#unique_nums = [i for i in src_exercise_5 if src_exercise_5.count(i) == 1]

unique_nums = set()
tmp = set()
for i in src_exercise_5:
    if i not in tmp:
        unique_nums.add(i)
    else:
        unique_nums.discard(i)
    tmp.add(i)
unique_nums_final = [i for i in src_exercise_5 if i in unique_nums]
print((unique_nums_final))
=======
=======


>>>>>>> old
>>>>>>> old
