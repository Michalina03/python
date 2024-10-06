from user import User
class Admin(User):
    def __init__(self, username, password, role="Admin"):
        super().__init__(username, password, role)

    def admin_function(self, users, data):
        print("1. Dodaj użytkownika")
        print("2. Usuń użytkownika")
        print("3. Zmień nazwe użytkownika")
        print("4. Zmień hasło użytkownika")
        print("5. Zmień role użytkownika")
        choice = int(input("Wybierz opcję: "))

        if choice == 1:
            new_username = input("Podaj nazwę użytkownika: ")
            new_password = input("Podaj hasło: ")
            new_role = input("Podaj rolę (Admin/Employee/Importer): ")
            users.append(User(new_username, new_password, new_role))
            print(f"Użytkownik {new_username} został dodany.")

        elif choice == 2:
            del_username = input("Podaj nazwę użytkownika do usunięcia: ")
            user_found = False
            for user in users:
                if user.username == del_username:
                    users.remove(user)
                    user_found = True
                    break

            if user_found:
                print(f"Użytkownik {del_username} został usunięty.")
            else:
                print(f"Użytkownik {del_username} nie istnieje.")
        
        
        elif choice == 3:
            old_username = input("Podaj obecną nazwę użytkownika: ")
            for user in users:
                if user.username == old_username:
                    new_username = input("Podaj nową nazwę użytkownika: ")
                    user.username = new_username
                    print(f"Nazwa użytkownika zmieniona na {new_username}.")
                    break
            else:
                print(f"Użytkownik {old_username} nie istnieje.")

        elif choice == 4:
            username = input("Podaj nazwę użytkownika, dla którego chcesz zmienić hasło: ")
            for user in users:
                if user.username == username:
                    new_password = input("Podaj nowe hasło: ")
                    user.password = new_password
                    print("Hasło zostało zmienione.")
                    break
            else:
                print(f"Użytkownik {username} nie istnieje.")

        elif choice == 5:
            username = input("Podaj nazwę użytkownika, dla którego chcesz zmienić rolę: ")
            for user in users:
                if user.username == username:
                    new_role = input("Podaj nową rolę (Admin/Employee): ")
                    user.role = new_role
                    print(f"Rola użytkownika {username} została zmieniona na {new_role}.")
                    break
            else:
                print(f"Użytkownik {username} nie istnieje.")
            