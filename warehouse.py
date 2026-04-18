from product import Product

class Warehouse:
    def __init__(self):
        self.products =[]

    def add_item(self,name,count):
        product = self.find_product(name)
        if product:
            product.count += count
        else:
            self.product.append(Product(name, count))

    def take(self, name,count):
        products = self.find_product(name)

        if products is None:
            print("товар не найден")
            return
        
        if products.count < count:
            print("недостачно товара на складе")
            return 
        
        products.count -= count

        if products.count == 0:
            self.products.remove(products)
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
            if product.name.lover() == name.lower():
                return product
        return None
