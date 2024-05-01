from colorama import init
init()
from colorama import Fore, Back, Style
from layout import d_print, error, empty_dialog

def help():
    d_print((Style.BRIGHT + 'Выберите один из выше доступных пунктов. ' + Style.RESET_ALL + "\nНо, также, Вы в любой момент можете воспользоваться такими командами как:" + Fore.BLUE + \
    "\n" \
    "\n /help" + Style.RESET_ALL + " - помощь" + Fore.BLUE + \
    "\n /back" + Style.RESET_ALL + " - вернуться" + Fore.BLUE + \
    "\n /exit" + Style.RESET_ALL + " - выход" \
), "1110")
    back(history_data)

history_data = []
def history_for_back(id: str | int, history_data: list):
    history_data.append(id) 
    return history_data

def back(history_data: list):
    from pages import start_list
    match int(history_data[-1]):
        case 1:
            start_list(history_data)
            return
        case _:
            error(5)
            empty_dialog()

def command(text):
    match text[0]:
        case "/":
            match text:
                case "/help":
                    help()
                    back(history_data)
                case "/exit":
                    exit()
                case "/back":
                    back(history_data)
                case _:
                    error(3)
                    back(history_data)
        case _:
            return text