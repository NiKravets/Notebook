import db
import cNote


def checkList(id):
    listOfNotes = db.readFromFile()
    for note in listOfNotes:
        if id == cNote.Note.getId(note):
            return True
