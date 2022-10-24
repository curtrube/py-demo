class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.admin = False
        self.formatted_name = f"{first_name} {last_name}"
        
    def greet_user(self):
        return f"Hello, {self.formatted_name}"

    def is_admin(self):
        if self.admin:
            return True
        else:
            return False


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
        

class Privileges:
    def __init__(self):
        self.permission_policies = ['create', 'read', 'update', 'delete']

    def show_permissions(self):
        return self.permission_policies


curtis = Admin('curtis', 'rubeck')
print(curtis.privileges.show_permissions())