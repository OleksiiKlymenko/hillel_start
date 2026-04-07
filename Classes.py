class Product:
    def __init__(self, name, price, category, quantity):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    def priceChange(self, new_price):
        self.price = new_price
        return f"new price: {self.price}"


    def quantityChange(self, new_quantity):
        self.quantity = new_quantity
        return f"new quantity: {self.quantity}"

product1 = Product("Teddy", 10, "soft", 60)
product1.priceChange(50)
product1.quantityChange(5)

print(product1.price)
print(product1.quantity)


##############

class Customer:
    def __init__(self, first_name, last_name, email, orders=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.orders = orders if orders is not None else []

    def add_order(self, order):
        self.orders.append(order)
        return f"Замовлення '{order}' успішно додано для клієнта {self.first_name} {self.last_name}."


FirstCustomer = Customer("Ivan", "Ivanov", "ivan@gmail.com", ["Soft toy"])
print(FirstCustomer.orders)
print(FirstCustomer.add_order("Softer toy v2"))
print(FirstCustomer.orders)


#############
class Order():
    def __init__(self, ordersList = None):
        self.ordersList = ordersList if ordersList is not None else []
        self.sumTotal = 0

    def add_product(self, product):
        self.ordersList.append(product)
        self.count_sum_total()

    def count_sum_total(self):
        total = 0
        for order in self.ordersList:
            total += order.price

        self.sumTotal = total
        return self.sumTotal

p1 = Product("М'яч", 100, "Спорт", 5)
p2 = Product("Лялька", 250, "Іграшки", 3)

my_order = Order()
my_order.add_product(p1)
my_order.add_product(p2)
print(f"Загальна сума: {my_order.sumTotal}")

#################
#data_store
products = []
customers = []


with open('data.txt', 'r', encoding='utf-8-sig') as file:
    for line in file:
        row = line.strip().split(',')

        if row[0] == 'P':
            new_p = Product(row[1], row[2], row[3], row[4])
            products.append(new_p)

        elif row[0] == 'C':
            new_c = Customer(row[1], row[2], row[3])
            customers.append(new_c)

print(f"Клієнт: {customers[0].first_name} {customers[0].last_name}")
print("Продукти в базі:")
for p in products:
    print(f"- {p.name} (Категорія: {p.category}, Ціна: {p.price}, Кількість: {p.quantity})")

