from datetime import datetime


def handle_datetime_command(command):
    command = command.lower().strip()
    now = datetime.now()

    # Current date
    if "date" in command and "today" in command:
        return now.strftime("Today's date is %d %B %Y, Sir.")

    # Current time
    elif "time" in command:
        return now.strftime("The time is %I:%M %p, Sir.")

    # Current day
    elif "day" in command and "today" in command:
        return now.strftime("Today is %A, Sir.")

    # Current month
    elif "month" in command and "this" in command:
        return now.strftime("This is %B, Sir.")

    # Current year
    elif "year" in command and "this" in command:
        return now.strftime("The current year is %Y, Sir.")

    return None