import os
# This function receives the user's command and performs the required action.

def execute_command(command):

    # Open Google Chrome
    if "open chrome" in command:
        os.startfile(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        return "Opening Google Chrome"

    # Open Calculator
    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator"

    # Open Notepad
    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    # Open VS Code
    elif "open code" in command or "open vscode" in command:
        os.system("code")
        return "Opening VS Code"

    # Open Paint
    elif "open paint" in command:
        os.system("mspaint")
        return "Opening Paint"

    else:
        return "Command not recognized."