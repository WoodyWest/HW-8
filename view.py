import json

def JsonRead(viewMode,num):
     with open("persons.json", "r", encoding="utf-8") as file:
            persons=json.loads(file.read())
     with open("departments.json", "r", encoding="utf-8") as file:
            departments=json.loads(file.read())  
     with open("positions.json", "r", encoding="utf-8") as file:
            positions=json.loads(file.read())    
     if viewMode=='1':
        print("--------------------------------------")
        print(f"Запись номер {num}:")
        print()
        print(f"ФИО и телефон сотрудника: {persons[num]}")
        print()
        print(f"Отдел, за которым закреплен сотрудник: {departments[num]}")
        print()
        print(f"Должность сотрудника: {positions[num]}")
        print("--------------------------------------")   
     else:
        for i in range(int(num)):
                print(f"Запись номер {i+1}:")
                print()
                print(f"ФИО и телефон сотрудника: {persons[str(i+1)]}")
                print()
                print(f"Отдел, за которым закреплен сотрудник: {departments[str(i+1)]}")
                print()
                print(f"Должность сотрудника: {positions[str(i+1)]}")
                print("--------------------------------------")  


