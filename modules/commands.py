import os
# This function receives the user's command and performs the required action.

def execute_command(command):

    # Open Google Chrome
    if "open chrome" in command:
        os.startfile(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )

    # Open Calculator
    elif "open calculator" in command:
        os.system("calc")

    # Open Notepad
    elif "open notepad" in command:
        os.system("notepad")

    # Open VS Code
    elif "open code" in command or "open vscode" in command:
        os.system("code")

    else:
        print("Command not recognized.")