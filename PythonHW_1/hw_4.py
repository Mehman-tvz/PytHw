documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

# код должен быть грамотно декомпозирован (каждая функция отвечает за свою конкретную задачу, дублирующийся функционал переиспользуется, а его код не повторяется);
# в коде отсутствуют глобальные переменные (за исключением documents и directories);
# пользовательский ввод обрабатывается в цикле while до тех пор, пока пользователь явно не завершит программу (вводом команды "q")

def return_not_exists():
    print("Документ не найден в базе")

def list_directory_keys():
    v_directories = ''
    for y in directories.items():
        v_directories = str(v_directories + ',' + str(y[0]))
    v_directories = v_directories[1:]  # delete first comma cant't find another solution
    return v_directories

def get_name_by_number(v_number):
    v_checker=0
    for i in documents:
        if i["number"]==v_number:
            print("Владелец документа: "+i["name"])
            v_checker+=1
    if v_checker==0:
        return_not_exists()


def get_location_by_number(v_number):
    v_checker = 0
    for i in directories.items():
        if v_number in i[1]:
            print("Документ хранится на полке: " +str(i[0]))
            v_checker += 1
    if v_checker == 0:
        return_not_exists()

def get_all_info():
    for i in documents:
        v_type = i["type"]
        v_name = i["name"]
        v_number=i["number"]

        for y in directories.items():
            if v_number in y[1]:
                v_location=y[0]
        print("№: "+str(v_number)+", тип: "+v_type+", владелец: "+v_name+", полка хранения: "+str(v_location))


def add_directori(directori, number=None):#nummber added for the logic concistensy for example we want add number too
    res = [key for key, value in directories.items() if key == directori]
    if number is None and res == []:
        directories[directori] = []
    elif res == []:
        directories[directori] = number


    v_directories = list_directory_keys()  # delete first comma cant't find another solution
    if res != []:
        print("Такая полка уже существует. Текущий перечень полок: " + v_directories)
    else:
        print("Полка добавлена. Текущий перечень полок: " + v_directories)


def delete_directori(directori):
    key = [key for key, value in directories.items() if key == directori]
    value = [value for key, value in directories.items() if key == directori]

    v_directories=list_directory_keys()
    if key == []:
        print("Такой полки не существует. Текущий перечень полок: " + v_directories)
    elif key != [] and value[0]!= []:
        print("На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: " + v_directories)
    else:
        del directories[directori]
        v_directories=list_directory_keys()
        print("Полка удалена. Текущий перечень полок: " + v_directories)

while 1 == 1:  # Tolko ne ponyal odin moment esli polzovatel vvodit nepravilnuyu komandu k primeru t toqda je toje doljno cto to stat
    command = input("Введите команду: ")

    if command == 'p':
        v_number = input("Введите номер документа:")
        get_name_by_number(v_number)
    elif command == 's':
        v_number = input("Введите номер документа:")
        get_location_by_number(v_number)
    elif command == 'l':
        get_all_info()
    elif command == 'ads':
        v_location= input("Введите номер полки:")
        add_directori(v_location)
    elif command == 'ds':
        v_location = input("Введите номер полки:")
        delete_directori(v_location)
    elif command == 'q':
        break

