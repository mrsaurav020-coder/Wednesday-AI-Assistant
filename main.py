from modules.speak import speak
from modules.speech import listen
from modules.command_processor import process_command

speak("Wednesday is online. What do you want me to do, Sir?")
while True:
    command = listen()
    if not command:
        continue
    # User wants to exit
    if command in ["exit", "quit", "goodbye", "shutdown"]:
        speak("Before I shut down, is there anything else you need, Sir?")
        reply = listen()

        # User really wants to exit
        if reply in ["no", "no thanks", "nothing", "that's all", "bye"]:
            speak("Alright Sir. Have a wonderful day. Goodbye.")
            break

        # User changed their mind
        elif reply:
            process_command(reply)

        continue

    process_command(command)