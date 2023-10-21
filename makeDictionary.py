# 2 Практическая работа
menu = "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"
menu += "\n1. Добавить заметку"
menu += "\n2. Удалить заметку"
menu += "\n3. Вывод заметок"
menu += "\n4. Выход"
menu += "\n⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"

notes = dict()

def addNote():
    name_note = str(input("Введите заголовок:"))
    content_note = str(input("Введите описание: "))
    notes.update({name_note:content_note})

def delNote():
    name_note = str(input("Введите заголовок"))
    content_checker = notes.get(name_note)
    if content_checker is not None:
        notes.pop(name_note, None)

def showNote(notes):
    for key, value in notes.items():
        print(f"Заголовок: {key}; Описание: {value}")

while True:
    print(menu)
    print(notes)
    answer = int(input("Введите действие: "))
    match answer:
        case 1:
            addNote()
        case 2:
            delNote()
        case 3:
            showNote(notes)
        case 4:
            break
        case _:
            break
else:
    print("Прощай")