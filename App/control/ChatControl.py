from App.models import ChatModel, UserModel


class Chat_control:
    def __init__(self):
        super().__init__()
        self.C = ChatModel.Chat()
        self.U = UserModel.Usermodel()

    def get_user_contact_from_control(self, user_id):
        C = ChatModel.Chat()
        result = self.C.get_user_contacts(user_id)
        return result

    def get_user_id_from_control(self, password):
        return self.U.get_user_id(password)

    def add_group(self, chatid, name, type, userid, description, avatar):
        return self.C.add_chat(chatid, name, type, userid, description, avatar)
