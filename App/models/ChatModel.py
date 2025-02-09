import mysql.connector


class Chat:
    def __init__(self):
        super().__init__()
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",  # Changed 'name' to 'user' as per mysql.connector syntax
            password="MySqlPa$$",
            database="youmee",
            port=3307
        )
        self.cursor = self.mydb.cursor()

    def get_user_contacts(self, user_id):
        print(type(user_id))
        try:
            self.cursor.execute("SELECT contact_name FROM user_contacts WHERE user_id=%s", (user_id,))
            result = self.cursor.fetchall()
            for r in result:
                print(r[0])
                return r[0]
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()


    def add_chat(self, chatid, name, type, userid, description, avatar):
        try:
            self.cursor.execute(
                "INSERT INTO chats (chat_id, chat_name, chat_type, user_id, description, avatar, created_at, updated_at) "
                "VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW())",
                (chatid, name, type, userid, description, avatar)
            )
            self.mydb.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            if self.mydb.is_connected():
                self.cursor.close()
                self.mydb.close()



    def remove_chat(self, chat_id):
        try:
            self.cursor.execute("DELETE FROM chats WHERE chat_id = %s", (chat_id,))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()


C = Chat()
#C.add_chat(1, 'BEST GCE GROUP', "group", "U03", "an Amazing meeting point for 2020 GCE A level graduates", "C:/Users/Tab's/PycharmProjects/Chatty/images/chat icons.png")
#C.get_user_contacts("U03")