from modules.speak import speak
from modules.speech import listen
from modules.commands import execute_command

speak("Wednesday is online.")
command = listen()
if command:
    speak(f"You said {command}")
    execute_command(command)
    