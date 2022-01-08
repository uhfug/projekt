#exercise 1

eng_words = input("Введите чилсо на английском от 0 до 10: " )
translate = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}

def num_translate(eng_words):
    print(translate.get(eng_words, 'Перевод невозможен'))

num_translate(eng_words)


#exercise 3
import random




def thesaurus(name_one, name_two, name_three, name_four):
    names_dict = {name_one[0]:[name_one],
                  name_two[0]:[name_two],
                  name_three[0]:[name_three],
                  name_four[0]:[name_four]}
    for key, val in names_dict.items():
        if val != name_one or name_two or name_three or name_four:
            names_dict[val[0][0]] = [name_one, name_four]
            break
        print(val)

    print(names_dict)
thesaurus('Иван', 'Мария', 'Кирилл', 'Илья')

#exercise 5

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    i = 0
    jokes = []
    while i < n:
        random_index_nouns = random.randint(0, len(nouns) - 1)
        random_index_adverbs = random.randint(0, len(adverbs) - 1)
        random_index_adjectives = random.randint(0, len(adjectives) - 1)
        i += 1
        jokes.append(f'{nouns[random_index_nouns]} {adverbs[random_index_adverbs]} {adjectives[random_index_adjectives]}')
    print(jokes)
get_jokes(4)