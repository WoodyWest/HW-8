import json
import menu
import view
import controller

def ViewRecord():
    viewList=["Показать все записи","Вывести запись по номеру"]
    with open("IDs.txt", 'r') as file:
               numID = file.read()
    print(f"Доступно для отображения {numID} записей.")           
    viewMode=menu.DrawMenu(viewList)[0]
    if viewMode=="1":
        view.JsonRead(viewMode,numID)
    else:
        numOfRecord=input("Введине номер записи: ")
        view.JsonRead(viewMode,numOfRecord)
    
def AddRecord():
    CreateID()
    id=GetId()
    AddPerson(id)
    AddDepartment(id)
    AddPosition(id)
    controller.button_click()
  
def AddPerson(idPerson):
    print("Введите ФИО и телефон нового пользователя.")
    print()
    personDict={}
    firstName=input("Enter First Name: ")
    midleName=input("Enter Midle Name: ")
    lastName=input("Enter Last Name: ")
    phoneNumber=input("Enter Phone Number: ")
    personInfo=firstName+' '+midleName+' '+ lastName +' >>> '+"Phone number: "+phoneNumber
    personDict[idPerson]=personInfo
    with open ('persons.json','a+', encoding="utf-8") as file:
        json.dump(personDict, file)
    print("Данные успешно добавлены.")
    print()

def AddDepartment(idDepart):
    print("Выбирете номер отдела, к которому относиться новый пользователь.")
    print()
    departmentDict={}
    departmentList=["ПТО","Бухгалтерия","Снабжение"]
    departmentInfo=menu.DrawMenu(departmentList)[1]
    departmentDict[idDepart]=departmentInfo
    with open ('departments.json','a+', encoding="utf-8") as file:
        json.dump(departmentDict, file)
    print("Данные успешно добавлены.")
    print()

def AddPosition(idPosition):
    print("Выбирете должность нового пользователя.")
    print()
    positionDict={}
    positionList=["Руководитель","Инженер","Специалист"]
    positionInfo=menu.DrawMenu(positionList)[1]
    positionDict[idPosition]=positionInfo
    with open ('positions.json','a+', encoding="utf-8") as file:
        json.dump(positionDict, file)
    print("Данные успешно добавлены.")
    print()

def GetId():
    with open('IDs.txt','r') as file:
           ID = int(file.read())
    return ID
           
def CreateID():
    with open("IDs.txt", 'r') as file:
               ID = file.read()
               ID = str(int(ID) + 1)
    with open("IDs.txt", 'w') as file:
               file.write(ID)

      

