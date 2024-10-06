from user import User
class Employee(User):
    def __init__(self, username, password, role="Employee"):
        super().__init__(username, password, role)