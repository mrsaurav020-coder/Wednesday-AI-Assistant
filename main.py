from modules.speak import speak
from modules.speech import listen
from modules.commands import execute_command
from modules.web_search import search_google

speak("Wednesday is online.")
command = listen()
if command:
    speak(f"You said {command}")
    if "search" in command:
        term = search_google(command)
        speak(f"Here are the search results for {term}")
    else:
        response = execute_command(command)
        speak(response)