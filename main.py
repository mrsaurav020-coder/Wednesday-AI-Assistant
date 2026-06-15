from modules.speak import speak
from modules.speech import listen
from modules.commands import execute_command
from modules.web_search import search_google
from modules.notes import save_note, get_notes
from modules.ai_chat import ask_ai

speak("Wednesday is online. What do you want me to do Sir?")
command = listen()

if command:
    if "search" in command:             #Google Search 
        term = search_google(command)
        speak(f"Searching {term}")

    elif command.startswith("remember"): # Remember a note
        note = command.replace("remember", "").strip()
        save_note(note)
        speak("I will remember that Sir.")

    elif "show my notes" in command:     # Show all saved notes
        notes = get_notes()
        if notes:
            speak("Here are your notes, Sir:")
            for note in notes:
                speak(note)
        else:
            speak("You do not have any saved notes Sir.")
    else:
        response = execute_command(command)

        if response == "Command not recognized.":
            speak("Let me think about that, Sir.")
            ai_response = ask_ai(command)
            print(ai_response)
            speak(ai_response)
        else:
            speak(response)