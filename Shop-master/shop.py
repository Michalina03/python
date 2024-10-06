class Shop:
    def __init__(self, shop_data):
        self.products = shop_data.get('products', [])
        self.balance = shop_data.get('balance', 0.0)

    def admin_shop(self):
        print("1. Dodaj produkt")
        print("2. Usuń produkt")
        choice = int(input("Wybierz opcję: "))
        if choice == 1:
            name = input("Podaj nazwę produktu: ")
            price = float(input("Podaj cenę produktu: "))
            self.products.append({"name": name, "price": price})
        elif choice == 2:
            name = input("Podaj nazwę produktu do usunięcia: ")
            self.products = [product for product in self.products if product['name'] != name]

    def employee_shop(self, user):
        print("Dostępne produkty:")
        for product in self.products:
            print(f"- {product['name']} (${product['price']})")
        
        name = input("Podaj nazwę produktu do sprzedaży: ")
        product = next((p for p in self.products if p['name'] == name), None)
        if product:
            self.balance += product['price']
            print(f"Sprzedano produkt: {product['name']} za ${product['price']}")
        else:
            print("Produkt niedostępny")

    def importer_shop(self, user):
        print("Dostępne produkty:")
        for product in self.products:
            print(f"- {product['name']} (${product['price']})")
        
        name = input("Podaj nazwę produktu do sprzedaży: ")
        product = next((p for p in self.products if p['name'] == name), None)
        if product:
            self.balance -= product['price']
            print(f"Sprowadzono produkt: {product['name']} za ${product['price']}")
        else:
            print("Produkt niedostępny")

    def to_dictionary(self):
        return {
            "products": self.products,
            "balance": self.balance
        }
