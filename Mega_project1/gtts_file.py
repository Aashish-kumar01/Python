# way to imput a audio in the jarvis



# from gtts import gTTS
# import pygame
# import os

# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')

#     # Intialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 File
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 File
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

#     pygame.mixer.music.unload()
#     os.remove('temp.mp3')