def generate_report(users, shop):
    with open("report.txt", "w") as file:
        file.write("Raport \n")
        file.write("="*20 + "\n")
        file.write("Uzytkownicy:\n")
        for user in users:
            file.write(f"- {user.username} ({user.role})\n")

        file.write("\nProdukty:\n")
        for product in shop.products:
            file.write(f"- {product['name']} (${product['price']})\n")

        file.write(f"\nStan finansow: ${shop.balance}\n")
