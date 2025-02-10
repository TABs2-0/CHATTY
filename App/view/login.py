import customtkinter as ctk
from App.models import UserModel  # Adjust import path if needed
from App.view.sign_in import SignIn
from App.control.UserControl import Usercontrol
from App.view.mainPage import MainPage
from tkinter import messagebox
from PIL import Image


class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x450")
       # self.resizable(False, False)
        self.title("Login Page")
        self.usercontrol = Usercontrol()

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.configure(fg_color="#F6F0F5")

        # Left Section (Main Login UI)
        self.left_frame = ctk.CTkFrame(self, fg_color="#F6F0F5", width=400, height=450)
        self.left_frame.pack(side="left", fill="both", expand=False, pady=50)

        self.label = ctk.CTkLabel(self.left_frame, text="Login To Your Space😎😎",
                                  font=("Just Me Again Down Here", 30),
                                  text_color="black")
        self.label.pack(pady=20, padx=20)



        self.email_entry = ctk.CTkEntry(self.left_frame, placeholder_text="Email",
                                        width=204, height=35,
                                        fg_color="#D9D9D9", text_color="black",
                                        corner_radius=10)
        self.email_entry.pack(pady=10, padx=50)

        self.pass_entry = ctk.CTkEntry(self.left_frame, placeholder_text="Password",
                                       width=204, height=35,
                                       fg_color="#D9D9D9", text_color="black",
                                       corner_radius=10, show="*")
        self.pass_entry.pack(pady=10, padx=50)

        self.login_button = ctk.CTkButton(self.left_frame, text="Login", command=self.authentify,
                                          width=204, height=35,
                                          fg_color="#D9D9D9", text_color="black",
                                          corner_radius=10)
        self.login_button.pack(pady=20)

        img = Image.open("C:/Users/Tab's/PycharmProjects/Chatty/images/annelle.png")
        photo = ctk.CTkImage(light_image=img, size=(100, 100))

        ict_img = Image.open("C:/Users/Tab's/PycharmProjects/Chatty/images/ict.jpg")
        ict_photo = ctk.CTkImage(light_image=ict_img, size=(100, 100))

        self.image_label = ctk.CTkLabel(self.left_frame, image=photo,height=150,width=150,text="")
        self.image_label.pack(pady=2,padx=0)

        self.name_label = ctk.CTkLabel(self.left_frame, height=150, width=150, text="TABOUGUIA NGNOWA YOAN CABREL:ICTU20241135")
        self.name_label.pack(pady=4, padx=0)

        self.ict_label = ctk.CTkLabel(self.left_frame, image=ict_photo, height=150, width=150, text="")
        self.ict_label.pack(pady=4, padx=4)
        # Right Section (Sign-in Prompt)
        self.right_frame = ctk.CTkFrame(self, fg_color="#7BDCC8", width=200, height=450)
        self.right_frame.pack(side="right", fill="both", expand=False)

        self.label2 = ctk.CTkLabel(self.right_frame,
                                   text="NEW HERE?? Sign in and get in touch with the most amazing messaging app!",
                                   font=("Just Me Again Down Here", 30),
                                   text_color="black", wraplength=180)
        self.label2.pack(pady=100, padx=10)

        self.sign_in_button = ctk.CTkButton(self.right_frame, text="Sign In", command=self.sign_in,
                                            width=204, height=35,
                                            fg_color="#D9D9D9", text_color="black",
                                            corner_radius=10)
        self.sign_in_button.pack(pady=20)


    def authentify(self):
        email = self.email_entry.get()
        password = self.pass_entry.get()
        credentials = self.usercontrol.get_credentials(password)

        if email == '' or password == '':
            messagebox.showwarning("Required Fields", "Please fill in all fields to continue")
            return

        if credentials:
            if credentials[0] == email and credentials[1] == password:
                # messagebox.showinfo("Success", "Welcome back!")
                passw=credentials[1]
                self.main_window(passw)
                print("Login successful")
            else:
                messagebox.showwarning("Access Denied", "Invalid email or password")
                print("Login was not successful")
        else:
            messagebox.showinfo("Account Not Found", "No account found with these credentials")

    def sign_in(self):
        self.destroy()
        sign = SignIn()
        sign.mainloop()

    def main_window(self,password):
        self.destroy()
        win = MainPage(password)
        win.mainloop()


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()