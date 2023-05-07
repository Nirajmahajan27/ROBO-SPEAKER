import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
print("I'm Created by Niraj Mahajan")
while True:
    print("Enter the text: ")
    text=input()
    if text=="stop":
        break
    engine.say(text)
        # play the speech
    engine.runAndWait()