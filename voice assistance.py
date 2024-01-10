import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Couldn't request results from Google Speech Recognition service; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I am your simple voice assistant. How can I assist you today?")

    while True:
        user_input = listen()

        if "exit" in user_input:
            speak("Exiting the program. Goodbye!")
            break

        if user_input:
            response = f"You said: {user_input}"
            print(response)
            speak(response)
