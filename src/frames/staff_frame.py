import customtkinter as ctk
import tkinter as tk

from data_manager import *
from tkinter import ttk, messagebox
from libra import *

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

# Убираем поле ID, т.к. оно автоинкрементное
def create_staff_frame(root):
    frame = root
    name_label = ctk.CTkLabel(frame, font=font1, text='Name:', text_color='#fff', bg_color='#161C25')
    name_label.place(x=20, y=20)

    name_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
    name_entry.place(x=100, y=20)

    position_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    position_label.place(x=20, y=80)

    position_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
    position_entry.place(x=100, y=80)

    gender_label = ctk.CTkLabel(frame, font=font1, text='Sex:', text_color='#fff', bg_color='#161C25')
    gender_label.place(x=20, y=140)

    options = ['Male', 'Female']
    variable1 = StringVar()

    gender_options = ctk.CTkComboBox(frame, font=font1, text_color='#000', fg_color='#fff',
                                     dropdown_hover_color='#0C9295', button_hover_color='#0C9295',
                                     border_color='#0C9295', width=180, variable=variable1,
                                     values=options, state='readonly')
    gender_options.set('Male')
    gender_options.place(x=100, y=140)

    birthday_label = ctk.CTkLabel(frame, font=font1, text='Birthday:', text_color='#fff', bg_color='#161C25')
    birthday_label.place(x=20, y=200)

    birthday_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295',
                                  border_width=2, width=180)
    birthday_entry.place(x=100, y=200)

    status_label = ctk.CTkLabel(frame, font=font1, text='Status:', text_color='#fff', bg_color='#161C25')
    status_label.place(x=20, y=260)

    status_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff', 
                                border_color='#0C9295', border_width=2, width=180)
    status_entry.place(x=100, y=260)

    add_btn = ctk.CTkButton(frame, command=insert, font=font1, text_color='#fff',
                            text='Add Staff', fg_color='#05A312', hover_color='#00850B',
                            bg_color='#161C25', cursor='hand2', corner_radius=15, width=260)
    add_btn.place(x=20, y=310)

    clear_btn = ctk.CTkButton(frame, command=lambda: clear(True), font=font1, text_color='#fff',
                              text='New Entry', fg_color='#161C25', hover_color='#FF5002',
                              bg_color='#161C25', border_color='#F15704', border_width=2,
                              cursor='hand2', corner_radius=15, width=260)
    clear_btn.place(x=20, y=360)

    update_btn = ctk.CTkButton(frame, command=update, font=font1, text_color='#fff',
                               text='Update Staff', fg_color='#161C25', hover_color='#FF5002',
                               bg_color='#161C25', border_color='#F15704', border_width=2,
                               cursor='hand2', corner_radius=15, width=260)
    update_btn.place(x=300, y=360)

    delete_btn = ctk.CTkButton(frame, command=delete, font=font1, text_color='#fff',
                               text='Delete Staff', fg_color='#E40404', hover_color='#AE0000',
                               bg_color='#161C25', border_color='#E40404', border_width=2,
                               cursor='hand2', corner_radius=15, width=260)
    delete_btn.place(x=580, y=360)

    style = ttk.Style(frame)
    style.theme_use('clam')
    style.configure('Treeview', font=font2, foreground='#fff', background='#000', fieldbackground='#313837')
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    tree = ttk.Treeview(frame, height=15)

    tree['columns'] = ('ID', 'Name', 'Position', 'Sex', 'Birthday', 'Status')

    tree.column('#0', width=0, stretch=tk.NO)  # Hide the default first column
    tree.column('ID', anchor=tk.CENTER, width=80)
    tree.column('Name', anchor=tk.CENTER, width=150)
    tree.column('Position', anchor=tk.CENTER, width=150)
    tree.column('Sex', anchor=tk.CENTER, width=100)
    tree.column('Birthday', anchor=tk.CENTER, width=120)
    tree.column('Status', anchor=tk.CENTER, width=120)

    tree.heading('ID', text='ID')
    tree.heading('Name', text='Name')
    tree.heading('Position', text='Position')
    tree.heading('Sex', text='Sex')
    tree.heading('Birthday', text='Birthday')
    tree.heading('Status', text='Status')

    tree.place(x=300, y=20)

    def add_to_treeview():
        staff_list = fetch_staff()
        tree.delete(*tree.get_children())
        for staff in staff_list:
            tree.insert('', END, values=(staff[0], staff[1], staff[2], staff[3], staff[4], staff[5]))

    def clear(*clicked):
        if clicked:
            tree.selection_remove(tree.focus())
            tree.focus('')
        # id_entry теперь скрыт, не очищаем
        name_entry.delete(0, END)
        position_entry.delete(0, END)
        variable1.set('Male')
        birthday_entry.delete(0, END)
        status_entry.delete(0, END)

    def display_data(event):
        selected_item = tree.focus()
        if selected_item:
            row = tree.item(selected_item)['values']
            clear()
            id = row[0]
            #conn = database.sqlite3.connect(database.DB_PATH)
            conn = connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT birthday FROM staff WHERE id = ?", (id,))
            birthday_row = cursor.fetchone()
            conn.close()
            birthday = birthday_row[0] if birthday_row else ''

            name_entry.insert(0, row[1])
            position_entry.insert(0, row[2])
            variable1.set(row[3])
            birthday_entry.insert(0, birthday)
            status_entry.insert(0, row[5])  # исправлено с row[4] на row[5]
        else:
            pass

    def delete():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a staff member to delete.')
        else:
            id = tree.item(selected_item)['values'][0]
            delete_staff(id)
            add_to_treeview()
            clear()
            messagebox.showinfo('Success', 'Data has been deleted.')

    def update():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a staff member to update.')
        else:
            id = tree.item(selected_item)['values'][0]
            name = name_entry.get()
            position = position_entry.get()
            sex = variable1.get()
            birthday = birthday_entry.get()
            status = status_entry.get()
            if not (name and position and sex and birthday and status):
                messagebox.showerror('Error', 'Enter all fields.')
                return
            update_staff(id, name, position, sex, birthday, status)
            add_to_treeview()
            clear()
            messagebox.showinfo('Success', 'Data has been updated.')

    def insert():
        # id не вводится, т.к. автоинкремент
        name = name_entry.get()
        position = position_entry.get()
        sex = variable1.get()
        birthday = birthday_entry.get()
        status = status_entry.get()
        if not (name and position and sex and birthday and status):
            messagebox.showerror('Error', 'Enter all fields.')
        else:
            insert_staff(name, position, sex, birthday, status)
            add_to_treeview()
            clear()
            messagebox.showinfo('Success', 'Data has been inserted.')
    
    tree.bind('<ButtonRelease>', display_data)

    add_to_treeview()
