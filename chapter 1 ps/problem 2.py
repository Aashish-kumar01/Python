import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("According to Newton's first law of motion, if an object is in the state of rest then it will continue to be in the state of rest, and when an object is in the state of motion then it will continue to be in the state of motion in a straight line, unless and otherwise an external force is appplied on it.")
engine.runAndWait()