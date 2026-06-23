from modules.memory import save_memory, get_memory
def handle_memory_command(command):
    command = command.lower().strip()
    
    # SAVE MEMORY COMMANDS
    if command.startswith("my name is"):
        value = command.replace("my name is", "").strip()
        save_memory("name", value)
        return f"I will remember that. Your name is {value}, Sir."

    elif command.startswith("my favorite color is"):
        value = command.replace("my favorite color is", "").strip()
        save_memory("favorite_color", value)
        return f"I will remember that. Your favorite color is {value}, Sir."

    elif command.startswith("my favorite food is"):
        value = command.replace("my favorite food is", "").strip()
        save_memory("favorite_food", value)
        return f"I will remember that. Your favorite food is {value}, Sir."

    elif command.startswith("my hobby is"):
        value = command.replace("my hobby is", "").strip()
        save_memory("hobby", value)
        return f"I will remember that. Your hobby is {value}, Sir."
    
    elif command.startswith("my goal is"):
        value = command.replace("my goal is", "").strip()
        save_memory("goal", value)
        return f"I will remember that. Your goal is {value}, Sir."

    elif command.startswith("i study at"):
        value = command.replace("i study at", "").strip()
        save_memory("college", value)
        return f"I will remember that. You study at {value}, Sir."

    elif command.startswith("i live in"):
        value = command.replace("i live in", "").strip()
        save_memory("city", value)
        return f"I will remember that. You live in {value}, Sir."

    # RECALL MEMORY COMMANDS
    elif "what is my name" in command:
        value = get_memory("name")
        if value:
            return f"Your name is {value}, Sir."
        return "I do not know your name yet, Sir."

    elif "what is my favourite colour" in command:
        value = get_memory("favourite_colour")
        if value:
            return f"Your favourite colour is {value}, Sir."
        return "I do not know your favourite colour yet, Sir."

    elif "what is my favourite food" in command:
        value = get_memory("favourite_food")
        if value:
            return f"Your favourite food is {value}, Sir."
        return "I do not know your favourite food yet, Sir."

    elif "what is my hobby" in command:
        value = get_memory("hobby")
        if value:
            return f"Your hobby is {value}, Sir."
        return "I do not know your hobby yet, Sir."

    elif "what is my goal" in command:
        value = get_memory("goal")
        if value:
            return f"Your goal is {value}, Sir."
        return "I do not know your goal yet, Sir."

    elif "where do i study" in command:
        value = get_memory("college")
        if value:
            return f"You study at {value}, Sir."
        return "I do not know where you study yet, Sir."

    elif "where do i live" in command:
        value = get_memory("city")
        if value:
            return f"You live in {value}, Sir."
        return "I do not know where you live yet, Sir."

    return None