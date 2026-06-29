from modules.speak import speak
from modules.commands import execute_command
from modules.web_search import search_google
from modules.notes import save_note, get_notes
from modules.ai_chat import ask_ai
from modules.memory_commands import handle_memory_command
from modules.datetime_commands import handle_datetime_command


def process_command(command):
    """
    Process the user's voice command and perform the appropriate action.
    """

    # ---------------- GOOGLE SEARCH ----------------
    if "search" in command:
        term = search_google(command)
        speak(f"Searching {term}")

    # ---------------- NOTES ----------------
    elif command.startswith("remember"):
        note = command.replace("remember", "").strip()
        save_note(note)
        speak("I will remember that, Sir.")

    elif "show my notes" in command:
        notes = get_notes()

        if notes:
            speak("Here are your notes, Sir.")
            for note in notes:
                speak(note)
        else:
            speak("You do not have any saved notes, Sir.")

    # ---------------- PERSONAL MEMORY ----------------
    else:
        memory_response = handle_memory_command(command)

        if memory_response:
            speak(memory_response)

        else:
            # ---------------- DATE & TIME ----------------
            datetime_response = handle_datetime_command(command)

            if datetime_response:
                speak(datetime_response)

            else:
                # ---------------- SYSTEM COMMANDS ----------------
                response = execute_command(command)

                if "Command not recognized" in response:
                    speak("Let me think about that, Sir.")

                    ai_response = ask_ai(command)

                    print(ai_response)

                    # Prevent extremely long responses
                    speak(ai_response[:500])

                else:
                    speak(response)