import cNote


def writeToList(listOfNote, mode):
    file = open("db.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("db.csv", mode=mode, encoding='utf-8')
    for note in listOfNote:
        strNote = cNote.Note.toString(note)
        file.write(strNote)
        file.write('\n')
    file.close()


def readFromFile():
    try:
        file = open("db.csv", mode='r', encoding='utf-8')
        notes = file.read().strip().split('\n')
        listNotes = []
        for n in notes:
            splitNote = n.split(',')
            note = cNote.Note(id=splitNote[0], title=splitNote[1], body=splitNote[2], date=splitNote[3])
            listNotes.append(note)
    except Exception:
        print('Заметок нет')
    finally:
        return listNotes
