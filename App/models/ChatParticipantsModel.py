import mysql.connector


class ChatParticipants:
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

    def add_participants(self, chat_id, user_id, role, nickname):
        try:
            self.cursor.execute("INSERT INTO chat_participants (chat_id,user_id,role,nickname,joined_at) VALUES (%s,"
                                "%s,%s,%s,"
                                "NOW())",
                                (chat_id, user_id, role, nickname))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()

    def remove_participants(self, user_id):
        try:
            self.cursor.execute("DELETE FROM chat_participants WHERE user_id = %s", (user_id,))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()

    def update_participant_role(self, user_id):
        try:
            self.cursor.execute("UPDATE chat_participants SET role ='admin'  WHERE user_id =%s", (user_id,))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()

