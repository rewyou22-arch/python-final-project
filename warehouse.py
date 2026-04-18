from product import Product

class Warehouse:
    def __init__(self):
        self.products =[]

    def add_item(self,name,count):
        product = self.find_product(name)
        if product:
            product.count += count
        else:
            self.products.append(Product(name, count))

    def take(self, name,count):
        product = self.find_product(name)

        if product is None:
            print("товар не найден")
            return
        
        if product.count < count:
            print("недостачно товара на складе")
            return 
        
        product.count -= count

        if product.count == 0:
            self.products.remove(product)
            print("товар списан")

    def show(self):
        if not self.products:
            print("склад пуст")
        else:
            print('\n товары на складе' )

            for product in self.products:
                product.show_info()
                print("-----")

    def find_product(self,name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None
