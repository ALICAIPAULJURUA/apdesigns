import speech_recognition as sr
import pyttsx3

def listen_and_repeat():
    # Initialize recognizer and TTS engine
    recognizer = sr.Recognizer()
    tts_engine = pyttsx3.init()

    # Function to listen to the microphone
    def listen():
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            audio = recognizer.listen(source)
            return audio

    # Function to recognize speech
    def recognize(audio):
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results from the speech recognition service.")
            return None

    # Function to speak the text
    def speak(text):
        tts_engine.say(text)
        tts_engine.runAndWait()

    # Main loop to continuously listen and repeat
    while True:
        try:
            audio = listen()
            text = recognize(audio)
            if text:
                speak(text)
        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    listen_and_repeat()
