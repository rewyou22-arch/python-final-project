from warehouse import Warehouse

def main():
    warehouse = Warehouse()

    while True:
        print("\nМеню:")
        print("1. Добавить товар")
        print("2. Списать товар")
        print("3. Показать склад")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите название товара: ")
            count = int(input("Введите количество: "))
            warehouse.add_item(name, count)
            print("Товар добавлен")

        elif choice == "2":
            name = input("Введите название товара: ")
            count = int(input("Введите количество для списания: "))
            warehouse.take(name, count)

        elif choice == "3":
            warehouse.show()

        elif choice == "4":
            print("Выход из программы")
            break

        else:
            print("Неверный пункт меню")


main()