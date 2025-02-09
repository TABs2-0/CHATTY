import mysql.connector
import datetime


class Attachment:
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

    def insert_attachment(self, id, filename, filetype, filesize, width, height):
        self.cursor.execute("INSERT INTO attachments (attachment_id,file_name,file_type,file_size,width,height,"
                            "created_at) VALUES (%s,%s,%s,%s,%s,%s,NOW())",
                            (id, filename, filetype, filesize, width, height))
        self.mydb.commit()
        self.mydb.close()

    def delete_attachment(self, attachment_id):
        try:
            self.cursor.execute("DELETE FROM attachments WHERE attachment_id = %s", (attachment_id,))
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()

    def get_attachment(self,id):
        try:
            self.cursor.execute("SELECT * FROM attachments WHERE attachment_id=%s", (id,))
            result = self.cursor.fetchall()
            for r in result:
                print(r)
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()
            return result
