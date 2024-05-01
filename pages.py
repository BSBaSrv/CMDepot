from colorama import init
init()
from colorama import Fore, Back, Style
from art import tprint
from layout import d_print, dialog, error
from commands import back

version = "0.3.2 Alpha"

def page_start():
    d_print("", "10")
    tprint("CMDepot")
    d_print(("Добро пожаловать. Вы запустили мультимедийное консольное приложение " + (Fore.RED + Style.BRIGHT + 'CMDepot') + Style.RESET_ALL + " версии " + \
            (Fore.WHITE + Back.BLACK + Style.BRIGHT + version) + Style.RESET_ALL + ". \nПри любых ошибках в работе пишите на" + \
            (Style.BRIGHT + ' GitHub (github.com/BSBaSrv/CMDepot)') + Style.RESET_ALL + " проекта. \nДля навигации можно использовать команды " + Fore.WHITE + \
            Back.BLACK + Style.BRIGHT + "(подробнее /help)" + Style.RESET_ALL), 
            "111069"
    )

#ID: 1
def start_list():
    from commands import history_data, history_for_back
    history_data = history_for_back(1, history_data)
    start_list = ["Магазин программ", "О программе"]
    number_choice = dialog("", start_list, False, "10", "00")
    
    match str(number_choice):
        case "1":
            page_depot()
        case "2":
            page_about()
        case _:
            error(3)
        
def page_depot():
    d_print(Fore.GREEN + Style.BRIGHT + "Извините. " + Style.RESET_ALL + "Это вкладка ещё не готова", "111078")
    back(True)

def page_about():
    d_print((Fore.RED + Style.BRIGHT + "CMDepot." + Style.RESET_ALL + " Версия - " + Fore.WHITE + Back.BLACK + Style.BRIGHT + version + ". Исходный код программы открыт. " + Style.RESET_ALL + \
            "Найти можно на " + Style.BRIGHT + "GitHub (github.com/BSBaSrv/CMDepot)." + Style.RESET_ALL + "\nЗа плохой код простите."), "111078"
    )
    back(True)