import speech_recognition as sr
import winsound

recognizer = sr.Recognizer()          # Create the recognizer only once
# Improve recognition sensitivity
recognizer.pause_threshold = 0.8      # Wait before considering speech finished
recognizer.energy_threshold = 300     # Ignore low background noise
recognizer.dynamic_energy_threshold = True


def listen():
    with sr.Microphone() as source:
        # Listen to surrounding noise for 1 second
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        winsound.Beep(1000, 200)   # Play a 200 ms beep 

        try:
            audio = recognizer.listen(
                source,
                timeout=5,             # Wait max 5 sec for speech
                phrase_time_limit=8    # Maximum command length
            )
            command = recognizer.recognize_google(audio, language="en-IN")
            print("You said:", command)
            return command.lower()
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            return ""
        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return ""