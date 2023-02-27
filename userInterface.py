import cNote


def editNote():
    title = ''
    body = ''
    while len(title) <= 0:
        print('Заголовок должен содержать символы\n')
        title = input('Введите заголовок заметки: ')
    while len(body) <= 0:
        print('Описание должно содержать символы\n')
        body = input('Введите описание заметки: ')
    return (title, body)


def createNote():
    note = editNote()
    return cNote.Note(title=note[0], body=note[1])

def menu():
    print('\n'*10)
    print('Вы в главном меню программы "Заметки"\n')
    print("для просмотра всех заметок введите 1\n"
          "для добавления заметки введите 2\n"
          "для редактирования заметки введите 3\n"
          "для удаления заметки введите 4\n"
          "для вывода заметки по дате введите 5\n"
          "для выбора заметки по id введите 6\n"
          "для выхода из программы введите 7\n")


def backToMenu():
    userInput = ''
    while userInput != '0':
        userInput = input('Для возврата в меню введите 0: ')
        print('\n')
    return menu()

