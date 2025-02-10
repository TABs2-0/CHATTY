import os.path
import shutil
import threading
from tkinter import filedialog
#import vlc
import customtkinter as ctk
from PIL import Image, ImageTk
from App.control import ChatControl, UserControl
from Client.client_socket import start_client, send_message, send_file, received_message, received_file


class MainPage(ctk.CTk):
    def __init__(self, password):
        super().__init__()
        self.geometry("1200x700")
        self.title("Main Page")
        self.configure(fg_color="white")

        self.control = ChatControl.Chat_control()
        self.userconrol = UserControl.Usercontrol()
        self.username = UserControl.Usercontrol().ge_user_name(password)
        self.password = password
        self.delay = 0  #
        self.frame_count = -1  #number of frames from o to n
        self.gif_frame = []  # array to store the frames
        self.stop = False
        #self.instance = vlc.Instance()
        #self.player = self.instance.media_player_new()
        #self.audio_player = self.instance.media_player_new()

        # Navigation Bar
        self.nav_frame = ctk.CTkFrame(self, width=100, height=700, fg_color="#E6E6FA", corner_radius=20)
        self.nav_frame.pack(side="left", fill="y")

        self.nav_button = ctk.CTkButton(self.nav_frame, text="", image=ctk.CTkImage(
            Image.open("C:/Users/Tab's/PycharmProjects/Chatty/images/Menu Bar.png")),
                                        width=62, height=50, fg_color="transparent")
        self.nav_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", width=80, fg_color="red",
                                         command=self.restore_original_ui)
        self.back_button.pack(padx=100)

        self.chat_button = ctk.CTkButton(self.nav_frame, text="", image=ctk.CTkImage(
            Image.open("C:/Users/Tab's/PycharmProjects/Chatty/images/chat icons.png")),
                                         width=62, height=50, fg_color="transparent", command=self.chat_update)
        self.chat_button.pack(pady=10)
        self.group_chat = ctk.CTkButton(self.nav_frame, text="", image=ctk.CTkImage(
            Image.open("C:/Users/Tab's/PycharmProjects/Chatty/images/ulysse.png")), width=62, height=50,
                                        fg_color="transparent", command=self.group_chat_layout)
        self.group_chat.pack(pady=10)

        self.account_button = ctk.CTkButton(self.nav_frame, text="", image=ctk.CTkImage(
            Image.open("C:/Users/Tab's/PycharmProjects/Chatty/images/account.png")),
                                            width=62, height=50, fg_color="transparent", command=self.myaccount_layout)
        self.account_button.pack(pady=10)

        self.notify_button = ctk.CTkButton(self.nav_frame, text="", image=ctk.CTkImage(
            Image.open("C:/Users/Tab's/PycharmProjects/Chatty/images/notification.png")),
                                           width=62, height=50, fg_color="transparent",
                                           command=self.notification_layout)
        self.notify_button.pack(pady=10)

        self.home_button = ctk.CTkButton(self.nav_frame, text="", image=ctk.CTkImage(
            Image.open("C:/Users/Tab's/PycharmProjects/Chatty/images/home_page.png")),
                                         width=62, height=50, fg_color="transparent")
        self.home_button.pack(pady=10)

        # Contacts Section
        self.contacts_frame = ctk.CTkFrame(self, width=200, height=700, fg_color="white", corner_radius=2)
        self.contacts_frame.pack(side="left", fill="y")

        self.search_bar = ctk.CTkEntry(self.contacts_frame, placeholder_text="SEARCH CONTACTS",
                                       width=180, height=40, fg_color="#E6E6FA", corner_radius=20)
        self.search_bar.pack(pady=20)

        self.user_id = self.control.get_user_id_from_control(self.password)
        #contacts = self.control.get_user_contact_from_control(user_id)
        #print(contacts)
        contacts = ["Ulysse", "JONATHAN", "Annelle", "Dylan", "Amy"]

        for contact in contacts:
            btn = ctk.CTkButton(self.contacts_frame, text=contact, width=180, height=50, fg_color="white",
                                text_color="black", font=("Just Me Again Down Here", 30),
                                corner_radius=20, command=self.contact_layout, image=ctk.CTkImage(
                    Image.open(f"C:/Users/Tab's/PycharmProjects/Chatty/images/{contact.lower()}.png")))
            btn.pack(pady=5)

            #chat section
        self.chat_frame = ctk.CTkFrame(self, fg_color="white")
        self.chat_frame.pack(side="bottom", pady=5, padx=50, fill="x")

        self.chat_entry = ctk.CTkEntry(self.chat_frame, placeholder_text="Start A Chat",
                                       width=700, height=30, fg_color="#E6E6FA", corner_radius=50)
        self.chat_entry.pack(side="left", padx=5, expand=True)

        self.send_message_btn = ctk.CTkButton(self.chat_frame, text="Send", width=80, fg_color="black",
                                              command=self.send_chat_message)
        self.send_message_btn.pack(side="left", padx=5)

        self.select_media_btn = ctk.CTkButton(self.chat_frame, text="Select_File", width=80, fg_color="black",
                                              command=self.send_media)
        self.select_media_btn.pack(side="left", padx=5)

    def contact_layout(self):
        self.contacts_layout()

    def chat_layout(self):
        self.chat_update()

    def group_chat_layout(self):
        self.update_group_chat()

    def notification_layout(self):
        self.contacts_frame.destroy()
        self.chat_frame.destroy()
        self.notif_label = ctk.CTkLabel(self, text="No Notifications For Now")
        self.notif_label.pack()

    def myaccount_layout(self):
        self.update_my_account()

    def update_my_account(self):
        self.chat_frame.destroy()
        self.contacts_frame.destroy()
        operations = ["Set Status", "Change Profile Picture", "Create Group", "Change Username"]

        for operation in operations:
            btn = ctk.CTkButton(self, text=operation, width=180, height=50, fg_color="white",
                                text_color="black", font=("Just Me Again Down Here", 30),
                                corner_radius=20, command=lambda op=operation: self.handle_account_action(op),
                                image=ctk.CTkImage(Image.open(
                                    f"C:/Users/Tab's/PycharmProjects/Chatty/images/{operation.lower()}.png")))
            btn.pack(padx=5)

    def handle_account_action(self, operation):
        print(f"{operation} button clicked")
        # We can now perform different actions based on which button was clicked
        if operation == "Set Status":
            self.set_status_ui()
        elif operation == "Change Profile Picture":
            self.change_profile_picture()
        elif operation == "Create Group":
            self.create_group()
        elif operation == "Change Username":
            self.change_username_ui()

    def update_group_chat(self):
        self.contacts_frame.destroy()
        self.group_members_frame = ctk.CTkFrame(self, width=200, height=700, fg_color="white", corner_radius=2)
        self.group_members_frame.pack(side="right", fill="y")

        self.group_frame = ctk.CTkFrame(self, width=200, height=700, fg_color="white", corner_radius=2)
        self.group_frame.pack(side="left", fill="y")

        groups = ["BEST GCE GROUP", "Common"]
        for g in groups:
            btn = ctk.CTkButton(self.group_frame, text=g, width=180, height=50, fg_color="white",
                                text_color="black", font=("Just Me Again Down Here", 30),
                                corner_radius=20, command=self.contact_layout, image=ctk.CTkImage(
                    Image.open(f"C:/Users/Tab's/PycharmProjects/Chatty/images/{g.lower()}.png")))
            btn.pack(pady=5)

        group_members = ["Ulysse", "JONATHAN", "Annelle"]
        for group in group_members:
            btn = ctk.CTkButton(self.group_members_frame, text=group, width=180, height=50, fg_color="white",
                                text_color="black", font=("Just Me Again Down Here", 30),
                                corner_radius=20, command=self.contact_layout, image=ctk.CTkImage(
                    Image.open(f"C:/Users/Tab's/PycharmProjects/Chatty/images/{group.lower()}.png")))
            btn.pack(pady=5)

    def chat_update(self):
        # Refresh contacts list
        if hasattr(self, 'contacts_frame'):
            self.contacts_frame.destroy()

        self.contacts_frame = ctk.CTkFrame(self, width=200, height=700, fg_color="white", corner_radius=2)
        self.contacts_frame.pack(side="left", fill="y")

        self.search_bar = ctk.CTkEntry(self.contacts_frame, placeholder_text="SEARCH CONTACTS",
                                       width=180, height=40, fg_color="#E6E6FA", corner_radius=20)
        self.search_bar.pack(pady=20)

        user_id = self.control.get_user_id_from_control(self.password)
        contacts = self.control.get_user_contact_from_control(user_id)

        for contact in contacts:
            btn = ctk.CTkButton(self.contacts_frame, text=contact, width=180, height=50, fg_color="white",
                                text_color="black", font=("Just Me Again Down Here", 30),
                                corner_radius=20, command=self.contact_layout, image=ctk.CTkImage(
                    Image.open(f"C:/Users/Tab's/PycharmProjects/Chatty/images/{contact.lower()}.png")))
            btn.pack(pady=5)

    def contacts_layout(self):
        self.contact_label = ctk.CTkLabel(self, text=self.username)
        self.contact_label.pack()

    #messaging logic

    def send_chat_message(self):
        message_list = []
        message = self.chat_entry.get()
        message_list.append(message)
        send_message(message)

        for i, msg in enumerate(message_list):
            step = 2 * (i + 1)
            self.message_label = ctk.CTkLabel(self, fg_color="#E6E6FA", corner_radius=20, text_color="black",
                                              text=message)
            self.message_label.pack(side="right", anchor="sw", padx=10, pady=(5 + step), fill="x")

            self.chat_entry.delete(0, "end")

    def send_media(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        send_file(filepath)

    """ def recieve_media(self):
        file_info = received_file()
        file_path = file_info[1]
        filetype = file_info[0]
        file_data = file_info[2]
        with open(file_path, "wb") as file:
            file.write(file_data)
        if filetype in ["png", "jpg", "jpeg"]:
            self.display_image(file_path)
        elif filetype in ["mp4", "avi", "mkv"]:
            self.play_video(file_path)
        elif filetype in ["mp3", "wav"]:
            self.play_audio(file_path)
        print((file_info[0]))

    def display_image(self, filepath):
        img = Image.open(filepath)
        img = img.resize((200, 200))
        #img_tk = ImageTk.PhotoImage(img)
        image = []
        image.append(img)
        for i in image:
            self.message_label = ctk.CTkLabel(self, fg_color="#E6E6FA", corner_radius=20, text_color="black",
                                              image=ctk.CTkImage(i))
            self.message_label.pack(side="right", anchor="sw", padx=10, pady=5, fill="x")

   def play_video(self, filepath):
        self.player.set_mrl(filepath)
        self.player.play()

    def play_audio(self, filepath):
        self.audio_player.set_mrl(filepath)
        self.audio_player.play()
    """

    def restore_original_ui(self):
        self.destroy()
        app = MainPage("Upass")
        app.mainloop()

    def change_username_ui(self):
        self.username_window = ctk.CTkToplevel(self)  #the use of Top level is to avoid multiple main windows
        self.username_window.title("Username Modification")
        self.username_window.geometry("300x200")
        self.username_window.configure(bg="white")

        ctk.CTkLabel(self.username_window, text="Provide your password:").pack(pady=5)
        self.pass_entry = ctk.CTkEntry(self.username_window, placeholder_text="Enter password", width=250, height=30,
                                       fg_color="#E6E6FA", corner_radius=20)
        self.pass_entry.pack(pady=5)

        ctk.CTkLabel(self.username_window, text="Provide new username:").pack(pady=5)
        self.name_entry = ctk.CTkEntry(self.username_window, placeholder_text="Enter new username", width=250,
                                       height=30,
                                       fg_color="#E6E6FA", corner_radius=20)
        self.name_entry.pack(pady=5)

        self.change_btn = ctk.CTkButton(self.username_window, text="Set", width=80, fg_color="violet",
                                        command=self.change_username)
        self.change_btn.pack(pady=10)

    def change_username(self):
        user_id = self.pass_entry.get()
        new_name = self.name_entry.get()

        if user_id == self.password:
            self.userconrol.modify_user_name(user_id, new_name)
            ctk.CTkLabel(self.username_window, text="Username changed successfully!", fg_color="green").pack(pady=5)
        else:
            ctk.CTkLabel(self.username_window, text="Incorrect password!", fg_color="red").pack(pady=5)

        self.pass_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.username_window.destroy()

    #this change profile picture has a pb it deletes the previous image so correct it
    def change_profile_picture(self):
        path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        file_name = "change profile picture.png"  #get the filename
        destination_folder = "C:/Users/Tab's/PycharmProjects/Chatty/images/"
        destination_path = os.path.join(destination_folder, file_name)  #create the new directory

        try:
            shutil.copy(path, destination_path)  # Copy the file to the destination folder
            print(f"Profile picture updated: {destination_path}")

        except Exception as e:
            print(f"Error updating profile picture: {e}")

    def create_group(self):
        self.group_window = ctk.CTkToplevel(self, fg_color="white")
        self.group_window.geometry("400x500")

        ctk.CTkLabel(
            self.group_window, text="Create Group", font=("Arial", 24, "bold"), text_color="black"
        ).pack(pady=20)

        fields = [
            ("Group_id", "id"),
            ("Group_name", "name"),
            ("Description", "description"),
        ]

        self.entries = {}
        for field_name, field_id in fields:
            frame = ctk.CTkFrame(self.group_window, fg_color="#E6E6FA", corner_radius=10)
            frame.pack(fill="x", padx=20, pady=5)

            label = ctk.CTkLabel(frame, text=f"{field_name}:", font=("Arial", 14), text_color="black")
            label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            entry = ctk.CTkEntry(frame, fg_color="#E6E6FA", text_color="black", corner_radius=5)
            entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

            frame.columnconfigure(1, weight=1)
            self.entries[field_id] = entry

        add_frame = ctk.CTkFrame(self.group_window, fg_color="#E6E6FA", corner_radius=10)
        add_frame.pack(fill="x", padx=20, pady=5)

        avatar_label = ctk.CTkLabel(add_frame, text="Avatar Entry:", font=("Arial", 14), text_color="black")
        avatar_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.add_entry = ctk.CTkEntry(add_frame, fg_color="#E6E6FA", text_color="black", corner_radius=5)
        self.add_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.upload_button = ctk.CTkButton(
            self.group_window, text="Select Avatar", fg_color="#E6E6FA", hover_color="grey",
            command=self.select_file, text_color="black"
        )
        self.upload_button.pack(pady=10)

        submit_button = ctk.CTkButton(
            self.group_window, text="Create", fg_color="#E6E6FA", hover_color="grey",
            command=self.submit, text_color="black"
        )
        submit_button.pack(pady=20)

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        entry_field = self.add_entry
        entry_field.delete(0, "end")
        entry_field.insert(0, path)

    def set_status_ui(self):
        self.status_window = ctk.CTkToplevel()
        self.status_window.geometry("200x200")
        self.status_window.configure(fg_color="white")
        self.status_window.title("Your Status")
        self.status_frame = ctk.CTkFrame(self.status_window)
        self.status_frame.pack()

        self.display_label = ctk.CTkLabel(self.status_frame, text="")
        self.display_label.pack(fill=ctk.BOTH)

        self.set_btn = ctk.CTkButton(self.status_frame, text="Set", width=80, fg_color="violet",
                                     command=self.change_status())
        self.set_btn.pack(pady=50, padx=50, side="bottom")

        threading.Thread(
            target=self.read_gif).start()  # the fact that this reading process is complex makes threading necessary to protect our window
        self.status_window.bind("<space>", lambda e: self.stop_gif())

    def read_gif(self):
        print("initialising reading")
        self.gif_frame = []

        gif_file = Image.open("C:/Users/Tab's/PycharmProjects/Chatty/status/ironman.gif")
        print(f"your gif contains {gif_file.n_frames} frames")  #get the number of frames
        for r in range(0, gif_file.n_frames):
            gif_file.seek(r)  #gets each image of the frame
            self.gif_frame.append(gif_file.copy())  # paste reach image of the frame
        # print(gif_file.info["duration"])# get the frquency
        self.delay = gif_file.info["duration"]  #100ms
        print("reading is completed")
        self.play_gif()

    def play_gif(self):
        if not self.gif_frame:
            print("Error: No frames loaded.")
            return

        if self.stop:
            return  # Stop animation if stop flag is set

        self.frame_count = (self.frame_count + 1) % len(self.gif_frame)
        self.current_frame = ImageTk.PhotoImage(self.gif_frame[self.frame_count])
        self.display_label.configure(image=self.current_frame)

        self.status_window.after(self.delay, self.play_gif)

    def stop_gif(self):
        self.stop = not self.stop
        if not self.stop:
            self.play_gif()

    def change_status(self):
        pass

    def submit(self):
        group_name = self.entries["name"].get()
        des = self.entries["description"].get()
        avatar = self.add_entry.get()
        user_id = self.user_id

        #if not self.control.db_connection_is_open():
        #   print("Database connection is not open!")
        #  return

        print(group_name)
        self.control.add_group(user_id, group_name, "group", user_id, des, avatar)


if __name__ == "__main__":
    app = MainPage("Upass")
    app.mainloop()

#M = MainPage("Upass")
#M.read_gif()
