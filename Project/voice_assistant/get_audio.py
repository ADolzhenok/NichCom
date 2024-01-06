import speech_recognition as sr
import voice_assistant.speak


def get_audio_eng():
    flag = 0
    while flag == 0:
        recognition = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Speaking...")
            try:
                audio = recognition.listen(mic, phrase_time_limit=3.5)
                said = ""
                said = recognition.recognize_google(audio, language='en-US')
                print(said)
                flag = 1
            except Exception:
                text_for_speak = "Excuse me but I didn't understand what you said, please repeat"
                speak.speak_eng(text_for_speak)
                print(text_for_speak)
    return said.lower()


def get_audio_rus():
    flag = 0
    while flag == 0:
        print("work")
        recognition = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Говорите...")
            try:
                audio = recognition.listen(mic, phrase_time_limit=3.5)
                said = ""
                said = recognition.recognize_google(audio, language='ru-RU')
                print(said)
                flag = 1
            except Exception:
                text_for_speak = "Извините, я не поняла, что Вы сказали, повторите пожалуйста"
                speak.speak_rus(text_for_speak)
                print(text_for_speak)
    return said.lower()

