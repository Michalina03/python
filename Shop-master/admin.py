from user import User
class Admin(User):
    def __init__(self, username, password, role="Admin"):
        super().__init__(username, password, role)

    def admin_function(self, users, data):
        print("1. Dodaj użytkownika")
        print("2. Usuń użytkownika")
        choice = int(input("Wybierz opcję: "))
        if choice == 1:
            new_username = input("Podaj nazwę użytkownika: ")
            new_password = input("Podaj hasło: ")
            new_role = input("Podaj rolę (Admin/Employee): ")
            users.append(User(new_username, new_password, new_role))
        elif choice == 2:
            del_username = input("Podaj nazwę użytkownika do usunięcia: ")
            for user in users:
                if user.username == del_username:
                    users.remove(user)
                break