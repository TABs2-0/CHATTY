import mysql.connector
import datetime


class Messagemodel:
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

    def insert_message(self, messageid, chat_id, senderid, receiverid, status, messagetype, content):
        try:
            self.cursor.execute("INSERT INTO message (message_id,chat_id,sender_id,receiver_id,created_at,updated_at,"
                                "status,message_type,content) VALUES (%s,%s,%s,%s,NOW(),NOW(),%s,%s,%s)",
                                (messageid, chat_id, senderid, receiverid, status, messagetype, content))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()

    def deletemessage(self, message_id):
        try:
            self.cursor.execute("DELETE FROM message WHERE message_id = %s", (message_id,))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()

    def get_sender_messages(self, senderid):
        try:
            self.cursor.execute("SELECT * FROM message WHERE sender_id=%s", (senderid,))
            result = self.cursor.fetchall()
            for r in result:
                print(r)
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()
            return result

    def get_reciever_messages(self, receiverid):
        try:
            self.cursor.execute("SELECT * FROM message WHERE receiver_id=%s", (receiverid,))
            result = self.cursor.fetchall()
            for r in result:
                print(r)
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()
            return result

    def get_chat_messages(self, chatid):
        try:
            self.cursor.execute("SELECT * FROM message WHERE chat_id=%s", (chatid,))
            result = self.cursor.fetchall()
            for r in result:
                print(r)
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()
            return result

    #this function is to  impliment the edit function only for text messages
    def modify_or_edit_message(self, edited_text, messageid):
        try:
            self.cursor.execute("UPDATE message SET content =%s  WHERE message_id =%s", (edited_text, messageid))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()
