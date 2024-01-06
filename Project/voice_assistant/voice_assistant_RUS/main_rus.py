import sys
from voice_assistant.get_audio import get_audio_rus
from voice_assistant.speak import speak_rus
from voice_assistant.voice_assistant_RUS import commands_rus
from voice_assistant.Games_rus.tic_tac_toe_RUS import tic_tac_toe_rus
# import pyodbc
# import pymongo

login = ''

sys.path.append("../get_audio")
sys.path.append("../speak")


def introductory_talk():
    speak_rus(f"Нужна ли ещё помощь?")
    text = get_audio_rus()
    agreement = ('да', 'ага', 'нужна', 'надо', 'конечно')
    refusal = ('нет', 'не надо', 'до свидания', 'нет не нужна', 'не')
    print(text)
    if text in agreement:
        main_rus_va("")
    elif text in refusal:
        # conn.commit()
        speak_rus("Хорошего дня")
    else:
        speak_rus("Извини, скажи только да или нет?")
        introductory_talk()


# def main_rus_va(check_command="", name="ERROR"):
def main_rus_va(check_command=""):
    # global login
    # login = name
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # mydb = myclient["voice_assistant"]
    # mongo_collect = mydb["actions"]
    if check_command == "":
        speak_rus(f'Как я могу тебе помочь?')
        text = get_audio_rus()
        # conn = pyodbc.connect('Driver={SQL Server};'
        #                       'Server=USER-PC\SQLEXP;'
        #                       'Database=Voice_assistant;'
        #                       'Trusted_Connection=yes;')
        # cursor = conn.cursor()
    else:
        text = check_command
    if "таймер" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'включение таймера')")
        # commands_rus.timer(mongo_collect, login)
        commands_rus.timer()
        # cursor.commit()
    elif "врем" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'озвучивание текущего времени')")
        commands_rus.time()
        # cursor.commit()
    elif "погода" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'озвучивание текущей погоды')")
        commands_rus.weather()
        # cursor.commit()
    elif "файл" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'создание файла')")
        commands_rus.creating_word_file()
        # cursor.commit()
    elif "компьютер" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'открытие папки Мой Компьютер')")
        commands_rus.open_my_computer()
        # cursor.commit()
    elif "корзин" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'очистка корзины')")
        commands_rus.cleaning_recycle_bin()
        # cursor.commit()
    elif "браузер" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'Открытие браузера')")
        commands_rus.opening_the_browser()
        # cursor.commit()
    elif "вычислить" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'произведение математических вычислений')")
        commands_rus.calculator()
        # cursor.commit()
    elif "что" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'озвучивание списка команд')")
        commands_rus.capability()
        # cursor.commit()
    elif "поиск" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'произведение поиска на компьютере')")
        commands_rus.search()
        # cursor.commit()
    elif "язык" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'изменение языка раскладки')")
        commands_rus.change_keyboard_lang()
        # cursor.commit()
    elif "громкость" in text:
        if "увеличить" in text or "больше сделать" in text:
            # cursor.execute(f"Insert into dbo.История values('{login}', 'увеличение громкости')")
            commands_rus.volume("увеличить")
            # cursor.commit()
        else:
            # cursor.execute(f"Insert into dbo.История values('{login}', 'уменьшение громкости')")
            commands_rus.volume("уменьшить")
            # cursor.commit()
    elif "диспетчер задач" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'открытие диспетчера задач')")
        commands_rus.task_manager()
        # cursor.commit()
    elif "команд" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'проверка команд')")
        commands_rus.check_command()
        # cursor.commit()
    elif "игр" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'открытие игры')")
        tic_tac_toe_rus()
        # cursor.commit()
    elif "истори" in text:
        # cursor.execute(f"Insert into dbo.История values('{login}', 'проверка истории')")
        commands_rus.history()
        # cursor.commit()
    elif "money" in text:
        # cursor.execute(f"Insert into dbo.History values('{login}', 'checking money')")
        commands_rus.money()
        # cursor.commit()
    else:
        speak_rus("Изивните, я не могу это сделать, повторите, пожалуйста")
    if check_command == "":
        # introductory_talk(conn)
        introductory_talk()
