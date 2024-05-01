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
), "211158")
    back(history_data, True)

history_data = []
def history_for_back(id: str | int, history_data: list):
    history_data.append(id) 
    return history_data

def back(history_data: list, service_status):
    from pages import start_list

    if service_status != True:
        if len(history_data) == 1:
            error(7)
        elif len(history_data) != 1:
            if history_data[-1] == history_data[-2]:
                error(7)
            else:
                pass

    match int(history_data[-1]):
        case 1:
            start_list(history_data)
            return
        case _:
            error(5)
            back(history_data, True)

def command(text):
    match text[0]:
        case "/":
            match text:
                case "/help":
                    help()
                    back(history_data, True)
                case "/exit":
                    exit()
                case "/back":
                    back(history_data, False)
                case _:
                    error(3)
                    back(history_data, True)
        case _:
            return text