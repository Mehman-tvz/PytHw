# Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2.
# Напишите код, который проверяет какая из этих строк длиннее.
phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(phrase_1) > len(phrase_2):
    print("Фраза 1 длиннее фразы 2")
elif len(phrase_1) < len(phrase_2):
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фразы равной длины")

# Дана переменная, в которой хранится число (год). Необходимо написать программу, которая выведет, является ли данный
# год високосным или обычным.

vYear = 2012

if (vYear % 400 == 0) or (vYear % 100 != 0) and (vYear % 4 == 0):
    print("Високосный год")
else:
    print("Обычный год")

# Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить
# соответствующий знак зодиака.

vDay = int(input("Введите день:"))
vMonth = int(input("Введите месяц:"))

if (vMonth == 3 and vDay >= 21) or (vMonth == 4 and vDay <= 19):
    print("Ваш знак зодиака: Овен")
elif (vMonth == 4 and vDay >= 20) or (vMonth == 5 and vDay <= 20):
    print("Ваш знак зодиака: Телец")
elif (vMonth == 5 and vDay >= 21) or (vMonth == 6 and vDay <= 21):
    print("Ваш знак зодиака: Близнецы")
elif (vMonth == 6 and vDay >= 22) or (vMonth == 7 and vDay <= 22):
    print("Ваш знак зодиака: Рак")
elif (vMonth == 7 and vDay >= 23) or (vMonth == 8 and vDay <= 22):
    print("Ваш знак зодиака: Лев")
elif (vMonth == 8 and vDay >= 23) or (vMonth == 9 and vDay <= 22):
    print("Ваш знак зодиака: Дева")
elif (vMonth == 9 and vDay >= 23) or (vMonth == 10 and vDay <= 23):
    print("Ваш знак зодиака: Весы")
elif (vMonth == 10 and vDay >= 24) or (vMonth == 11 and vDay <= 22):
    print("Ваш знак зодиака: Скорпион")
elif (vMonth == 11 and vDay >= 23) or (vMonth == 12 and vDay <= 21):
    print("Ваш знак зодиака: Стрелец")
elif (vMonth == 12 and vDay >= 22) or (vMonth == 1 and vDay <= 20):
    print("Ваш знак зодиака: Козерог")
else:
    print("Ваш знак зодиака: Водолей")

# Вам нужно написать программу для подбора упаковок по размерам товара. Размеры (ширина, длина, высота) хранятся в
# переменных (в сантиметрах):

# Используйте следующие правила:
# если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран "Коробка №1";
# если хотя бы одно из измерений больше 2 метров, то выводите "Упаковка для лыж";
# если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите "Коробка №2";
# во всех остальных случаях выводите "Коробка №3".

width = 15
length = 55
height = 15

if width <= 15 and length <= 15 and height <= 15:
    print("Коробка №3")
elif width > 120 or length > 120 or height > 120:
    print("Упаковка для лыж")
elif 15 < width < 50 or 15 < length < 50 or 15 < height < 50:
    print("Коробка №2")
else:
    print("Коробка №3")
