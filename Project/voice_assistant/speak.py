import pyttsx3


def speak_eng(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    print(text)
    engine.runAndWait()
    # return text


def speak_rus(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    print(text)
    engine.runAndWait()

