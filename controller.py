import menu
import DB_operation as DBO
import sys

def button_click():
    menuList=["Добавить запись -->","Посмотреть записи -->","Выход -->"]
    menuChoice = menu.DrawMenu(menuList)
    match menuChoice[0]:
        case '1':
            DBO.AddRecord() 
        case '2':
            DBO.ViewRecord() 
        case '3':
            sys.exit


