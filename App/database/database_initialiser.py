import mysql.connector


class Db():
    #create db
    def __init__(self):
        super().__init__()
        self.mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",  # Changed 'name' to 'user' as per mysql.connector syntax
            password="MySqlPa$$",
            port=3307

        )
        self.cursor1 = self.mydb1.cursor()
        try:
            self.cursor1.execute("CREATE DATABASE IF NOT EXISTS youmee")
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb1.commit()
            self.mydb1.close()

        #reconnecting to initialise db
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",  # Changed 'name' to 'user' as per mysql.connector syntax
            password="MySqlPa$$",
            database="youmee",
            port=3307
        )
        self.cursor = self.mydb.cursor()

    def initialise_db(self):
        # timestamp returns the current time it was created
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS User (
                    user_id VARCHAR(100) PRIMARY KEY,
                    user_name VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    password VARCHAR(100),
                    first_name VARCHAR(100),
                    last_name VARCHAR(100),
                    profile_picture VARCHAR(100),
                    phone_number DOUBLE,
                    last_seen DATETIME,
                    status ENUM('online','offline') DEFAULT 'online',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            #user_id is a foreign key to get the user_name
            #avatar is the group pp
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Chats (
                    chat_id DOUBLE AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    chat_name VARCHAR(100),
                    chat_type ENUM('direct','group') DEFAULT 'direct',
                    user_id VARCHAR(100),
                    description VARCHAR(100),
                    avatar VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES User(user_id)
                )
            """)

            # chat id and user id are foreign keys to chat and user
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Chat_participants (
                    chat_id DOUBLE  NOT NULL,
                    user_id VARCHAR(100),
                    role ENUM('admin','member') DEFAULT 'member',  
                    nickname VARCHAR(100),
                    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (chat_id, user_id),  
                    FOREIGN KEY (chat_id) REFERENCES Chats(chat_id),
                    FOREIGN KEY (user_id) REFERENCES User(user_id)
                )
            """)
            #Double is used for keys that will be used many times things like chat and message id's
            # sender id is the foreign key to user
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Message (
                    message_id DOUBLE AUTO_INCREMENT NOT NULL PRIMARY KEY,
                    chat_id DOUBLE  NOT NULL ,
                    sender_id VARCHAR(100),
                    receiver_id VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    status ENUM('sent','delivered','read'),
                    is_deleted BOOLEAN DEFAULT FALSE,
                    message_type ENUM('audio','text','video','file','location'),
                    content VARCHAR(100),
                    FOREIGN KEY (chat_id) REFERENCES Chats(chat_id),
                    FOREIGN KEY (sender_id) REFERENCES User(user_id),
                    FOREIGN KEY (receiver_id) REFERENCES User(user_id)
                )
            """)

            # message_id is the foreign key of message
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Message_reads (
                    message_id DOUBLE NOT NULL UNIQUE,
                    user_id VARCHAR(100),
                    read_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (message_id, user_id),
                    FOREIGN KEY (message_id) REFERENCES Message(message_id),
                    FOREIGN KEY (user_id) REFERENCES User(user_id)
                )
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Attachments (
                    attachment_id VARCHAR(100) PRIMARY KEY,
                    file_name VARCHAR(100),
                    file_type VARCHAR(100),
                    file_size VARCHAR(100),
                    width INT,
                    height INT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # user id is foreignkey to User
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS USER_CONTACTS (
                    contact_id VARCHAR(100),
                    user_id VARCHAR(100),
                    contact_name VARCHAR(100),
                    blocked BOOLEAN DEFAULT FALSE,
                    favourite BOOLEAN DEFAULT FALSE,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (contact_id, user_id),
                    FOREIGN KEY (user_id) REFERENCES User(user_id)
                )
            """)

            # Using parameterized query for data insertion
            insert_query = """
                INSERT INTO User (
                    user_id, user_name, email, password, first_name, last_name,
                    profile_picture, phone_number, last_seen
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """
            user_data = (
                "U01", "John Wick", "yoan1661@gmail.com", "john_pass", "JOHN", "Nzometiah",
                "C:/Users/Tab's/Downloads/Ict Tuto.png", 686582327
            )
            print("database initialised and partially filled")
            self.cursor.execute(insert_query, user_data)
        except mysql.connector.Error as e:
            print(e)
        finally:
            self.mydb.commit()
            self.mydb.close()


if __name__ == "__main__":
    db = Db()
    db.initialise_db()
