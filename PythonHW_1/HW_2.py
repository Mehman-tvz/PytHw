#Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:

#среднюю букву, если число букв в слове нечетное;
#две средних буквы, если число букв четное.
vText= "testing"
vFrom=0
vTo=0

if len(vText)%2==0 and len(vText)>2:
    vFrom=int(len(vText)/2-1)
    vTo=int(len(vText)/2+1)
    print(vText[vFrom:vTo])
elif len(vText)%2!=0 and len(vText)>2:
    vFrom=int(len(vText)/2) #Так как я меняю тип то цифра идет к нижней границе и берет целую часть поэтому логика норм работает
    vTo=int(len(vText)/2)+1
    print(vText[vFrom:vTo])
else:
    print(vText) #Добавочная проверка

#Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз) и после первого нуля выводит сумму всех ранее введенных чисел.

vCounter=0
vNum=0

while 1==1:
    vNum=int(input("Введите число:"))
    if vNum!=0:
        vCounter+=vNum
    else:
        break
print(vCounter)



#Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
#Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки!
#Но мы не будем никого знакомить, если кто-то может остаться без пары:

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha','Mehman']
vCounter=0

if len(boys)==len(girls):
    boys=sorted(boys)
    girls=sorted(girls)
    print("Идеальные пары:")
    while vCounter<=len(boys)-1:
        print(boys[vCounter]+" и "+girls[vCounter])
        vCounter+=1
else:
    print("Внимание, кто-то может остаться без пары!")

#У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам (структура данных в примере).
#Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!) для каждой страны.

countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
print("Средняя температура в странах: ")
for i  in countries_temperature:
    print(i[0]+" - "+str(round(((sum(i[1])/len(i[1])-32)*5/9),2)))

#print(countries_temperature[0][1])