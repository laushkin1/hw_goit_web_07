from my_select import all_selections

if __name__ == "__main__":
    print("To select a request, \nselect a num from 1 to 10. \nTo view the requests, enter \n'help'")
    print("To exit enter 'exit'")
    while True:
        num = input(">>> ")
        if num == 'exit':
            break
        
        if num == "help":
            print("""1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
2. Знайти студента із найвищим середнім балом з певного предмета.
3. Знайти середній бал у групах з певного предмета.
4. Знайти середній бал на потоці (по всій таблиці оцінок).
5. Знайти, які курси читає певний викладач.
6. Знайти список студентів у певній групі.
7. Знайти оцінки студентів в окремій групі з певного предмета.
8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
9. Знайти список курсів, які відвідує певний студент.
10. Список курсів, які певному студенту читає певний викладач.

To exit enter 'exit'""")
            continue
        try:
            num = int(num)
        except ValueError:
            print(f"{num} is not a number")
            continue
            
        if 1 <= num <= 10:
            all_selections[num-1]()
        else:
            print("Please enter a number between 1 and 10")