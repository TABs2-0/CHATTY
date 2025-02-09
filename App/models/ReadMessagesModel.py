import mysql.connector


class ReadMessages:
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

    def add_message(self, message_id,user_id):
        try:
            self.cursor.execute("INSERT INTO message_reads  (message_id,user_id,read_at) VALUES (%s,%s,NOW())",
                                (message_id,user_id))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()

    def remove_message(self, message_id):
        try:
            self.cursor.execute("DELETE FROM message_reads WHERE message_id = %s", (message_id,))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()