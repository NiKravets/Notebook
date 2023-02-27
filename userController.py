import check
import commands
import userInterface



def start():
    userInput = ''
    while userInput != '7':
        userInterface.menu()
        userInput = input('Вариант из меню: ').strip()
        print('\n')
        if userInput == '1':
            commands.showAllNotes()
            userInterface.backToMenu()
        if userInput == '2':
            note = userInterface.createNote()
            commands.add(note)
            userInterface.backToMenu()
        if userInput =='3':
            commands.showAllNotes()
            print('\n')
            userInput = input('Введите id заметки: ')
            if check.checkList(userInput):
                editNote = userInterface.editNote()
                commands.edit(userInput,editNote[0],editNote[1])
            else:
                print('С таким id заметок нет\n')
            userInterface.backToMenu()
        if userInput =='4':
            commands.showAllNotes()
            print('\n')
            commands.delete(input('Введите id заметки: '))
            userInterface.backToMenu()
        if userInput =='5':
            commands.showDate(input('Введите дату заметки в формате dd.mm.yyyy: '))
            print('\n')
            userInterface.backToMenu()
        if userInput == '6':
            commands.showAllId()
            print('\n')
            commands.showId(input('Введите id заметки: '))
            userInterface.backToMenu()
        if userInput == '7':
            break