import speech_recognition as sr
import pyttsx3
import datetime

def speak(text):
    says = pyttsx3.init()
    says.say(text)
    says.runAndWait()


def listening():
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print("Try To Listening.....")
        a.adjust_for_ambient_noise(source)
        audio = a.listen(source)


    try:
        print("Recongnizing....")
        voice = a.recognize_google(audio)
        print(f"You said:{voice}")
        return voice.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand. Please repeat again?")
        return ""
    except sr.RequestError as e:
        print(f"Error with the speech recognition service;{e}")
        return ""
    
def voice_assistant():
    speak("Hello how can I Help you?")

    while True:
        voice = listening()
        if "hello" in voice:
            speak("Hello Sir. How Are You")

        elif "exit" in voice:
            speak("Bye Bye")
            break

        elif "what's your name" in voice:
            speak("I am a voice assistance.")
        
        elif voice:
            response = f"You said: {voice}"
            print(response)
            speak(response)

        else:
            speak("I will not understand. please speak again")


if __name__ == "__main__":
    voice_assistant()
    

