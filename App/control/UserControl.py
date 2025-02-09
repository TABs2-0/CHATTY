from App.models import UserModel


class Usercontrol:
    def __init__(self):
        super().__init__()
        self.usermodel = UserModel.Usermodel()

    def get_credentials(self, password):
        return self.usermodel.get_credentials(password)

    def Sign_in(self, identity, user_name, email, password, firstname, lastname, phonenumber):
        self.usermodel.create_user(identity, user_name, email, password, firstname, lastname, phonenumber)

    def ge_user_name(self, password):
        return self.usermodel.get_user_name(password)

    def modify_user_name(self, password, new):
        return self.usermodel.modify_user_name(password, new)
