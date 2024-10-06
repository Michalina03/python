from user import User
class Importer(User):
    def __init__(self, username, password, role="Importer"):
        super().__init__(username, password, role)