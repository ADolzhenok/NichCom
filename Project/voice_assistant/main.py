import voice_assistant.speak
from voice_assistant import speak
from voice_assistant.voice_assistant_ENG import main_eng
from voice_assistant.voice_assistant_RUS import main_rus

lang = ''

def language():
    if lang == 'english':
        main_eng.main_eng_va()
    elif lang == 'russian':
        main_rus.main_rus_va()
    else:
        speak.speak_eng("I know only Russian and English. Which will you choose?")
        language()


def startVA(chosenLang):
    global lang
    lang = chosenLang
    language()








