MEMORY_FILE = "data/memory.txt"

def save_memory(key, value):              # Save a fact in memory
    memories = {}
    try:                               
        with open(MEMORY_FILE, "r") as file:
            for line in file:
                if ":" in line:
                    k, v = line.strip().split(":", 1)
                    memories[k] = v
    except FileNotFoundError:
        pass
    memories[key] = value
    with open(MEMORY_FILE, "w") as file:
        for k, v in memories.items():
            file.write(f"{k}:{v}\n")

def get_memory(key):
    try:                                 # Retrieve the fact from memory
        with open(MEMORY_FILE, "r") as file:
            for line in file:
                if ":" in line:
                    stored_key, stored_value = line.strip().split(":", 1)
                    if stored_key == key:
                        return stored_value
    except FileNotFoundError:
        pass
    return None
