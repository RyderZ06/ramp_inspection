import customtkinter as ctk
import tkinter as tk
import database

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

app = ctk.CTk()
app.title('RAMP INSPECTION STAFF')
app.geometry('900x420')
app.config(bg = '#161C25')
app.resizable(False, False)

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

id_label = ctk.CTkLabel(app, font=font1, text='ID:',
                        text_color='#fff', bg_color='#161C25')
id_label.place(x=20, y=20)

id_entry = ctk.CTkEntry(app, font=font1, text_color='#000',
                        fg_color='#fff', border_color='#0C9295', border_width=2,width=180)
id_entry.place(x=100, y=20)

name_label = ctk.CTkLabel(app, font=font1, text='Name:',
                          text_color='#fff', bg_color='#161C25')
name_label.place(x=20, y=80)

name_entry = ctk.CTkEntry(app, font=font1, text_color='#000',
                        fg_color='#fff', border_color='#0C9295', border_width=2,width=180)
name_entry.place(x=100, y=80)

role_label = ctk.CTkLabel(app, font=font1, text='Role:',
                          text_color='#fff', bg_color='#161C25')
role_label.place(x=20, y=140)

role_entry = ctk.CTkEntry(app, font=font1, text_color='#000',
                        fg_color='#fff', border_color='#0C9295', border_width=2,width=180)
role_entry.place(x=100,y=140)

gender_label = ctk.CTkLabel(app, font=font1, text='Gender:',
                          text_color='#fff', bg_color='#161C25')
gender_label.place(x=20,y=200)

options = ['Male','Female']
variable1 = StringVar()

gender_options = ctk.CTkComboBox(app, font=font1, text_color='#000', fg_color='#fff',
                                 dropdown_hover_color='#0C9295', button_hover_color='#0C9295',
                                 border_color='#0C9295',width=180, variable=variable1,
                                values=options, state='readonly')
gender_options.set('Male')
gender_options.place(x=100,y=200)



app.mainloop()