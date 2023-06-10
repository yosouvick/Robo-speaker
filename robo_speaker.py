import win32com.client as wincom
if __name__=="__main__":
    print("Welcome to Robospeaker..")
    while True:
        x=input("Enter what you want me to pronounce:")
        if x=="q":
            speak.Speak("Bye bye,my friend")
            break
        speak = wincom.Dispatch("SAPI.SpVoice")
        speak.Speak(x)