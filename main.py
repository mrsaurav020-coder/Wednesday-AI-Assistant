from modules.speak import speak
from modules.speech import listen
from modules.commands import execute_command
from modules.web_search import search_google
from modules.notes import save_note, get_notes
from modules.ai_chat import ask_ai
from modules.memory_commands import handle_memory_command

speak("Wednesday at your service. What do you want me to do Sir?")
command = listen()

if command:
    print("Recognized command:", command)
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
        memory_response = handle_memory_command(command)
        if memory_response:
            speak(memory_response)

        else:
            response = execute_command(command)   
            if "Command not recognized" in response:    # If the command is not recognized, ask Gemini for a response
                speak("Let me think about that, Sir.")
                ai_response = ask_ai(command)
                print(ai_response)
                speak(ai_response)
            else:
                speak(response)