import mysql.connector
import datetime


class Usermodel:
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

    def create_user(self, identity, name, email, password, firstname, lastname, phonenumber):
        self.cursor.execute(
            "INSERT INTO User(user_id,user_name,email,password,first_name,last_name,phone_number,last_seen) VALUES ("
            "%s,%s,%s,%s,%s,%s,%s,NOW())",
            (
                identity, name, email, password, firstname, lastname, phonenumber))
        self.mydb.commit()
        self.mydb.close()

    def get_users(self, user_name):
        self.cursor.execute("SELECT * FROM User WHERE user_name=%s", (user_name,))
        result = self.cursor.fetchall()
        for r in result:
            print(r)
        self.mydb.commit()
        self.mydb.close()
        return result

    def get_user_id(self, password):
        self.cursor.execute("SELECT user_id FROM User WHERE password=%s", (password,))
        result = self.cursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def get_user_name(self, password):
        self.cursor.execute("SELECT user_name FROM User WHERE password=%s", (password,))
        result = self.cursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def modify_user_name(self, password, new_username):
        try:
            self.cursor.execute(
                "UPDATE User SET user_name=%s WHERE password=%s",
                (new_username, password)
            )
            self.mydb.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            if self.mydb.is_connected():
                self.cursor.close()
                self.mydb.close()

    def get_credentials(self, password):
        self.cursor.execute("SELECT email, password FROM User WHERE password=%s", (password,))
        result = self.cursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM User WHERE user_id = %s", (user_id,))
        self.mydb.commit()
        self.mydb.close()


Test = Usermodel()
#Test.create_user("U02", "yoanTheBEst", "tabs@gmail.com", "y", "Tabs", "yoan", "C:/Users/Tab's/Downloads/logo.png",
#              654782135)
#Test.get_users('John Wick')
#Test.delete_user("U02")
#Test.modify_user_name("john_pass","John")
#Test.get_user_id("yoan1661@gmail.com")
