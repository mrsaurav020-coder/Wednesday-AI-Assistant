NOTES_FILE = "data/notes.txt" # File used to store notes permanently

def save_note(note):       #Save a note into notes.txt
    with open(NOTES_FILE, "a") as file:      # a means append mode
        file.write(note + "\n")

def get_notes():            #Read all saved notes and return them.
    try:
        with open(NOTES_FILE, "r") as file:  # r means read mode
            notes = file.readlines()
            return [note.strip() for note in notes]
    except FileNotFoundError:
        return []