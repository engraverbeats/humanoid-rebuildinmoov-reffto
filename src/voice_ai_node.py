import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"Command: {command}")
            if 'stop' in command.lower():
                engine.say("Shutting down")
                engine.runAndWait()
                break
            else:
                engine.say(f"You said {command}")
                engine.runAndWait()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except KeyboardInterrupt:
        break
