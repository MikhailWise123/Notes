import UI.MainMenu as m


def menu_console():
        m.printNenuTitle("Главное меню\n           ЖУРНАЛ ЗАМЕТОК")
        print("1 - вывод всего списка \n2 - вывод заметки по id \n3 - выбор заметки по дате \n4 - редактировать заметку"
              " \n5 - добавить заметку \n6 - удалить заметку \n7 - выход")
        m.printMenuLine()
        print("\n введите пункт из меню ")
        