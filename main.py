from warehouse import Warehouse

warehouse = Warehouse()

print("1. добавить продукт")
print("2. взять продукт")
print("3. показать все продукты")
print('4. выход')

user_input = int(input("выберите дейсвие"))

if user_input == "1":
    name = input("введите название товара - ")
    count = int(input('введите количество товара - '))
    warehouse.add_item(name, count)
    print("товар добавлен!")

elif user_input == "2":
    name  = input("введите название  товара - ")
    count = int(input("введите количество списания товара - "))
    print("товар удален")

elif user_input == "3":
    warehouse.show()


