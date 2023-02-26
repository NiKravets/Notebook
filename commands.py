import db
import cNote


def add(input):
    listOfNotes = db.readFromFile()
    for note in listOfNotes:
        if cNote.Note.getId(input) == cNote.Note.getId(note):
            cNote.Note.setId(input)
    listOfNotes.append(input)
    db.writeToList(listOfNotes, 'a')
    print('Заметка добавлена\n')


def showAllId():
    try:
        listOfNotes = db.readFromFile()
        for note in listOfNotes:
            print('id: ' + cNote.Note.getId(note))
    except Exception:
        print('Нет ни одной заметки\n')


def showAllNotes():
    try:
        listOfNotes = db.readFromFile()
        for note in listOfNotes:
            print(cNote.Note.forShow(note))
    except Exception:
        print('Нет ни одной заметки\n')


def showId(input):
    isEmpty = True
    listOfNotes = db.readFromFile()
    for note in listOfNotes:
        if input == cNote.Note.getId(note):
            print(cNote.Note.forShow(note))
            isEmpty = False
    if isEmpty == True:
        print('С таким id заметок нет\n')


def showDate(input):
    isEmpty = True
    listOfNotes = db.readFromFile()
    for note in listOfNotes:
        if input == cNote.Note.getDate(note):
            print(cNote.Note.forShow(note))
            isEmpty = False
    if isEmpty == True:
        print('С такой датой заметок нет\n')


def delete(input):
    isDeleted = False
    listOfNotes = db.readFromFile()
    for note in listOfNotes:
        if input == cNote.Note.getId(note):
            listOfNotes.remove(note)
            isDeleted = True
            print('Заметка удалена\n')
    if isDeleted == False:
        print('С таким id заметок нет\n')


def edit(input, newTitle, newBody):
    listOfNotes = db.readFromFile()
    for note in listOfNotes:
        if input == cNote.Note.getId(note):
            cNote.Note.setTitle(note, newTitle)
            cNote.Note.setBody(note, newBody)
            cNote.Note.setDate(note)
            print('Заметка изменена\n')
    db.writeToList(listOfNotes, 'a')
