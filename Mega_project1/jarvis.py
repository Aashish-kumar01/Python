import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
# from openai import OpenAI   # Only use if you plan to use aiprocess()

rec = sr.Recognizer()
engine = pyttsx3.init()

api_key = "3502412bcfe24f87acfe864701a36cf6"
search_term = "technology"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.1)  # tiny delay to avoid overlapping audio with mic listening

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Song not found in music library.")
    elif "news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/everything?q=keyword&apiKey={api_key}")
            data = r.json()
            articles = data.get("articles", [])
            for i, article in enumerate(articles[:3], start=1):
                title = article.get("title")
                source = article.get("source", {}).get("name")
                speak(f"News {i}: {title} — {source}")
        except Exception as e:
            speak("Unable to fetch news right now.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    mic = sr.Microphone()

    with mic as source:
        print("Calibrating microphone...")
        rec.adjust_for_ambient_noise(source, duration=1)
        print("Calibrated. Say 'Jarvis' to wake me.")

    while True:
        try:
            with mic as source:
                print("Listening for wake word...")
                audio = rec.listen(source, timeout=5, phrase_time_limit=2)

            try:
                word = rec.recognize_google(audio)
                print(f"You said: {word}")

                if word.lower() == "jarvis":
                    # ✅ Stop listening before speaking
                    speak("Ya")

                    # Now listen for actual command
                    with mic as source:
                        print("Jarvis Active... Listening for command.")
                        audio = rec.listen(source, timeout=5, phrase_time_limit=7)
                        command = rec.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)

            except sr.UnknownValueError:
                # No valid speech recognized, just keep looping
                pass
            except sr.RequestError as e:
                print("Speech recognition service error:", e)

        except sr.WaitTimeoutError:
            # No speech detected within timeout, loop again
            pass
        except KeyboardInterrupt:
            print("Exiting...")
            break
