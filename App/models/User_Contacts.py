import mysql.connector


class Usercontactmodel:
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

    def add_contact(self, contact_id, user_id, contact_name):
        self.cursor.execute("INSERT INTO user_contacts(contact_id,user_id,contact_name,created_at) VALUES(%s,%s,%s,"
                            "Now())", (contact_id, user_id, contact_name))
        self.mydb.commit()
        self.mydb.close()

    def delete_contact(self, contact_id):
        self.cursor.execute("DELETE FROM user_contacts WHERE contact_id=%s", (contact_id,))
        self.mydb.commit()
        self.mydb.close()

    def get_user_contacts(self, user_id):
        try:
            self.cursor.execute("SELECT * FROM user_contacts WHERE user_id=%s", (user_id,))

            result = self.cursor.fetchall()
            for r in result:
                print(r)
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()
            return result

    def block_contact(self,contact_name):
        self.cursor.execute("UPDATE user_contacts  SET blocked = TRUE WHERE contact_name =%s", (contact_name,))
        self.mydb.commit()
        self.mydb.close()

    def unblock_contact(self, contact_name):
        self.cursor.execute("UPDATE user_contacts  SET blocked = FALSE WHERE contact_name =%s", (contact_name,))
        self.mydb.commit()
        self.mydb.close()

    def favorites(self, contact_name):
        self.cursor.execute("UPDATE user_contacts  SET favourite = TRUE WHERE contact_name =%s", (contact_name,))
        self.mydb.commit()
        self.mydb.close()

    def non_favoorites(self, contact_name):
        self.cursor.execute("UPDATE user_contacts  SET favourite = FALSE WHERE contact_name =%s", (contact_name,))
        self.mydb.commit()
        self.mydb.close()

    def change_name(self, contact_name,new):
        self.cursor.execute("UPDATE user_contacts  SET contact_name = %s WHERE contact_name =%s", (new,contact_name,))
        self.mydb.commit()
        self.mydb.close()


T = Usercontactmodel()
#T.add_contact("C02", "U01", "besty")
#T.get_user_contacts("U01")
#T.block_contact("My Rib")
#T.favorites("My Rib")
#T.non_favoorites("My Rib")
#T.unblock_contact("My Rib")
#T.change_name("twinny","My Rib")