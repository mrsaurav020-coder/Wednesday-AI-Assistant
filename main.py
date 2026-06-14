from modules.speak import speak
from modules.speech import listen
from modules.commands import execute_command
from modules.web_search import search_google

speak("Wednesday is online. What do you want me to do Sir?")
command = listen()
if command:
    if "search" in command:
        term = search_google(command)
        speak(f"Searching {term}")
    else:
        response = execute_command(command)
        speak(response)