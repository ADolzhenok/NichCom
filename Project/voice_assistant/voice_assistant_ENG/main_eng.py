import sys


from voice_assistant.get_audio import get_audio_eng
from voice_assistant.speak import speak_eng
from voice_assistant.voice_assistant_ENG import commands_eng
from voice_assistant.Games_eng.tic_tac_toe_ENG import tic_tac_toe_eng

sys.path.append("../get_audio")
sys.path.append("../speak")


def introductory_talk():
    speak_eng(f"Do you need some more my help?")
    text = get_audio_eng()
    agreement = ('yes', 'yeah', 'that\'s right', 'Absolutely correct', 'correct')
    refusal = ('no', 'bye', 'goodbye', 'doesn\'t need', 'incorrect')
    if text in agreement:
        main_eng_va("")
    elif text in refusal:
        # conn.commit()
        speak_eng("Have a good day")
    else:
        speak_eng("Sorry, could you say yes or no")
        introductory_talk()


def main_eng_va(check_command=""):

    if check_command == "":
        speak_eng(f'Nice to meet you. How can I help you?')
        text = get_audio_eng()
    else:
        text = check_command
    if "timer" in text:
        commands_eng.timer()
    elif "time" in text:
        commands_eng.time()
    elif "weather" in text:
        commands_eng.weather()
    elif "word file" in text:
        commands_eng.creating_word_file()
    elif "computer" in text:
        commands_eng.open_my_computer()
    elif "recycle bin" in text:
        commands_eng.cleaning_recycle_bin()
    elif "browser" in text:
        commands_eng.opening_the_browser()
    elif "calculate" in text:
        commands_eng.calculator()
    elif "what can you do" in text:
        commands_eng.capability()
    elif "search" in text:
        commands_eng.search()
    elif "language" in text:
        commands_eng.change_keyboard_lang()
    elif "volume" in text:
        if "up" in text or "high" in text or "more" in text:
            commands_eng.volume("up")
        else:
            commands_eng.volume("down")
    elif "task manager" in text:
        commands_eng.task_manager()
    elif "command" in text:
        commands_eng.check_command()
    elif "game" in text:
        tic_tac_toe_eng()
    elif "money" in text:
        commands_eng.money()
    else:
        speak_eng(f"Excuse me,I can't do this or I couldn't hear you properly, please say something else or repeat")
    if check_command == "":
        introductory_talk()
