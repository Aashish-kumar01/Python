import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
from openai import OpenAI

rec = sr.Recognizer()
engine = pyttsx3.init()

api_key = "3502412bcfe24f87acfe864701a36cf6"
search_term = "technology"

def speak(text):
    engine.say(text)
    engine.runAndWait()


# def aiprocess(command):
#     client = OpenAI(api_key="",)

#     completion = client.chat.completion.create(
#     model="gpt-3.5-turbo",
#     message=[
#         {"role": "system", "content": "You are a virtual assitant named jarvis skilled in general tasks like Alexa and Google cloud"},
#         {"role": "user", "content": command}
#     ]
#     )

#     return (completion.choices[0].message.content)


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

        # parts = c.split(" ", 1)  # Split only once -> ["play", "ae dil hai mushkil"]
        # if len(parts) > 1:
        #     song = parts[1]  # This is the full song name
        #     found = None
        #     # Case-insensitive match
        #     for key in musicLibrary.music:
        #         if key.lower() == song:
        #             found = key
        #             break

        #     if found:
        #         link = musicLibrary.music[found]
        #         speak(f"Playing {found}")
        #         webbrowser.open(link)
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=keyword&apiKey={api_key}")
        data = r.json()
        articles = data.get("articles", [])
        # print(f"Found {len(articles)} articles for '{search_term}':\n")
        for i, article in enumerate(articles, start=1):
            title = article.get("title")
            source = article.get("source", {}).get("name")
            # print(f"{i}. {title} — {source}")
            speak(articles["title"])

    # else:
    #     # Let OpenAI handle the request
    #     output = aiprocess(c)
    #     speak(output)




    # print(C)

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone
        r = sr.Microphone()

        print("Recognizing...")

    # === Background callback / controller ===
    # stop_listening = None  # will hold the stopper returned by listen_in_background

    # def bg_callback(recognizer, audio):
    #     """
    #     Called in a background thread by listen_in_background whenever audio is captured.
    #     We detect the wake-word here. When detected:
    #     - stop background listening
    #     - speak a confirmation (e.g., "Ya")
    #     - listen synchronously for the full command
    #     - restart background listening
    #     """
    #     global stop_listening
    #     try:
    #         text = recognizer.recognize_google(audio)
    #         print("Background heard:", text)
    #     except sr.UnknownValueError:
    #         return
    #     except sr.RequestError as e:
    #         print("Speech API error (background):", e)
    #         return

        try: 
            with sr.Microphone() as source:
                print("Listening...")
                audio = rec.listen(source, timeout=2, phrase_time_limit=1)
            word = rec.recognize_google(audio)
            if(word.lower() == "alexa"):
                # if stop_listening is not None:
                #  stop_listening(wait_for_stop=False)

            # Speak confirmation (this should be audible because mic is not capturing now)
                speak("Ya")     # <-- you should now hear this reliably
                time.sleep(0.12)
            # speak("Ya")
            # time.sleep(1.0)
            # Listen for command
            with sr.Microphone() as source:
                print("Alexa Active...")
                audio = rec.listen(source)
                command = rec.recognize_google(audio)
                print(command)

                processCommand(command)


        except Exception as e:
            print("Error: {0}".format(e))

