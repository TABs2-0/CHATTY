import customtkinter as ctk
from App.control.UserControl import Usercontrol
from App.view.mainPage import MainPage
from tkinter import messagebox
from PIL import  Image,ImageTk


class SignIn(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("450x800")
        self.resizable(False, False)
        self.title("Sign_in Page")
        self.usercontrol=Usercontrol()

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.configure(bg="#7BDCC8",fg_color="#7BDCC8")

        img = Image.open("C:/Users/Tab's/PycharmProjects/Chatty/images/jonathan.png")
       # zoom_factor = 1  # Increase for more zoom
        #new_size = (img.width * zoom_factor, img.height * zoom_factor)
        #img = img.resize(new_size, Image.Resampling.LANCZOS)#this is to zoom the image
        photo = ctk.CTkImage(light_image=img,size=(200,200)) # light image makes the image more malleable

        self.avatar_label = ctk.CTkLabel(self, image=photo, height=150, width=150, text="")
        self.avatar_label.place(x=110, y=10)

        entry_width, entry_height = 300, 50
        spacing = 20
        start_y = 200

        self.id_entry = ctk.CTkEntry(self, placeholder_text="Fill in the User_Id",
                                     width=entry_width, height=entry_height,
                                     fg_color="#E6E6FA", text_color="black",
                                     corner_radius=20)
        self.id_entry.place(x=75, y=start_y)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Enter your User name",
                                       width=entry_width, height=entry_height,
                                       fg_color="#E6E6FA", text_color="black",
                                       corner_radius=20)
        self.name_entry.place(x=75, y=start_y + entry_height + spacing)

        self.email_entry = ctk.CTkEntry(self, placeholder_text="Enter your Email",
                                        width=entry_width, height=entry_height,
                                        fg_color="#E6E6FA", text_color="black",
                                        corner_radius=20)
        self.email_entry.place(x=75, y=start_y + 2 * (entry_height + spacing))

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Enter your password",
                                           width=entry_width, height=entry_height,
                                           fg_color="#E6E6FA", text_color="black",
                                           corner_radius=20)
        self.password_entry.place(x=75, y=start_y + 3 * (entry_height + spacing))

        self.first_entry = ctk.CTkEntry(self, placeholder_text="Enter your First_name",
                                        width=entry_width, height=entry_height,
                                        fg_color="#E6E6FA", text_color="black",
                                        corner_radius=20)
        self.first_entry.place(x=75, y=start_y + 4 * (entry_height + spacing))

        self.second_entry = ctk.CTkEntry(self, placeholder_text="Enter your Surname",
                                         width=entry_width, height=entry_height,
                                         fg_color="#E6E6FA", text_color="black",
                                         corner_radius=20)
        self.second_entry.place(x=75, y=start_y + 5 * (entry_height + spacing))

        self.phone_entry = ctk.CTkEntry(self, placeholder_text="Enter your Phone_number",
                                        width=entry_width, height=entry_height,
                                        fg_color="#E6E6FA", text_color="black",
                                        corner_radius=20)
        self.phone_entry.place(x=75, y=start_y + 6 * (entry_height + spacing))

        self.sign_in_button = ctk.CTkButton(self, text="Sign_in", command=self.sign_in,
                                            width=204, height=35,
                                            fg_color="#E6E6FA", text_color="black",
                                            corner_radius=20)
        self.sign_in_button.place(x=125, y=700)

    def sign_in(self):
        ide = self.id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        firstname = self.first_entry.get()
        secondname = self.second_entry.get()
        phonenumber = self.phone_entry.get()

        self.usercontrol.Sign_in(ide, name, email, password, firstname, secondname, phonenumber)
        messagebox.showinfo("Info", "Sign In Successful")


if __name__ == '__main__':
    app = SignIn()
    app.mainloop()
