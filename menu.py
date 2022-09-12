
def DrawMenu(inputMenu):
    menu=inputMenu
    lenght=len(menu)
    print("-----------------------------------------------")
    for i in range(lenght):
        print(f"{i+1}. {menu[i]}")
    print("-----------------------------------------------")
    menuItem=input("Введите пункт меню и нажмите Enter: ")
    return [menuItem,inputMenu[int(menuItem)-1]]

