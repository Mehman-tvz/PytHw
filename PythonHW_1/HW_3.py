# Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя (пример структуры данных
# приведен ниже). Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех
# пользователей.

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
allText = []

for i in ids:
    allText = ids[i] + allText

allText = list(dict.fromkeys(allText))
print(allText)

# Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже,
# но запросы потенциально могут быть любые). Вам необходимо написать программу, которая выведет на экран
# распределение количества слов в запросах в требуемом виде.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
_3word = 0
_2word = 0

for i in queries:
    if i.count(" ") == 1:
        _2word += 1
    else:
        _3word += 1

# print (_2word)
# print (_3word)
print("Поисковых запросов, содержащих 2 слов(а): " + str(
    round((_2word * 100 / (_2word + _3word)), 2)) + "\n Поисковых запросов, содержащих 3 слов(а): " + str(
    round((_3word * 100 / (_2word + _3word)), 2)))

# Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам.
# Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: ((revenue / cost) - 1) * 100
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for i in results:
    dictS = results[i]
    dictS['ROI'] = round(((dictS['revenue'] / dictS['cost'] - 1) * 100), 2)

print(results)

# Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных
# приведен ниже). Напишите программу, которая возвращает название канала с максимальным объемом продаж.

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
numG = 0

for i in stats:
    if numG < stats[i]:
        numG = stats[i]

for y, z in stats.items():
    if z == numG:
        print("Максимальный объем продаж на рекламном канале: "+str(y))
