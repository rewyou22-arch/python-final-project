class Product:
    def __init__(self,name,count):
        self.name = name
        self.count = count

    def show_info(self):
        print(f"{self.name} - имя продукта\n {self.count} - количество продукта")     