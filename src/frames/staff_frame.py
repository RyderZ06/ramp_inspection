import customtkinter as ctk
import tkinter as tk

from data_manager import *
from tkinter import ttk, messagebox, StringVar, END
from libra import *

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

# Убираем поле ID, т.к. оно автоинкрементное
def create_staff_frame(root):
    frame = root
    name_label = ctk.CTkLabel(frame, font=font1, text='Name:', text_color='#fff', bg_color='#161C25')
    name_label.grid(row=0, column=0, sticky='w', padx=20, pady=(20, 10))
    name_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                              border_color='#0C9295', border_width=2, width=180)
    name_entry.grid(row=0, column=1, sticky='w', padx=10, pady=(20, 10))

    position_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    position_label.grid(row=1, column=0, sticky='w', padx=20, pady=10)
    position_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                 border_color='#0C9295', border_width=2, width=180)
    position_entry.grid(row=1, column=1, sticky='w', padx=10, pady=10)

    gender_label = ctk.CTkLabel(frame, font=font1, text='Gender:', text_color='#fff', bg_color='#161C25')
    gender_label.grid(row=2, column=0, sticky='w', padx=20, pady=10)
    options = ['муж', 'жен']
    variable1 = StringVar()
    gender_options = ctk.CTkComboBox(frame, font=font1, text_color='#000', fg_color='#fff',
                                     dropdown_hover_color='#0C9295', button_hover_color='#0C9295',
                                     border_color='#0C9295', width=180, variable=variable1,
                                     values=options, state='readonly')
    gender_options.set('муж')
    gender_options.grid(row=2, column=1, sticky='w', padx=10, pady=10)

    birthday_label = ctk.CTkLabel(frame, font=font1, text='Birthday:', text_color='#fff', bg_color='#161C25')
    birthday_label.grid(row=3, column=0, sticky='w', padx=20, pady=10)
    birthday_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    birthday_entry.grid(row=3, column=1, sticky='w', padx=10, pady=10)

    status_label = ctk.CTkLabel(frame, font=font1, text='Status:', text_color='#fff', bg_color='#161C25')
    status_label.grid(row=4, column=0, sticky='w', padx=20, pady=10)
    status_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                border_color='#0C9295', border_width=2, width=180)
    status_entry.grid(row=4, column=1, sticky='w', padx=10, pady=10)

    # Frame для Treeview и Scrollbar'ов
    tree_frame = tk.Frame(frame)
    tree_frame.grid(row=0, column=2, rowspan=8, columnspan=7, padx=20, pady=20, sticky='nsew')

    
    style = ttk.Style(frame)
    style.theme_use('clam')
    style.configure('Treeview', font=font2, foreground='#fff', background='#000', fieldbackground='#313837')
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    tree = ttk.Treeview(tree_frame, height=15)

    # Вертикальный скроллбар
    vsb = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
    vsb.grid(row=0, column=1, sticky='ns')

    # Горизонтальный скроллбар
    hsb = ttk.Scrollbar(tree_frame, orient='horizontal', command=tree.xview)
    hsb.grid(row=1, column=0, sticky='ew')

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree['columns'] = ('ID', 'Name', 'Position', 'Gender', 'Birthday', 'Status')

    tree.column('#0', width=0, stretch=tk.NO)  # Hide the default first column
    tree.column('ID', anchor=tk.CENTER, width=80)
    tree.column('Name', anchor=tk.CENTER, width=150)
    tree.column('Position', anchor=tk.CENTER, width=150)
    tree.column('Gender', anchor=tk.CENTER, width=100)
    tree.column('Birthday', anchor=tk.CENTER, width=120)
    tree.column('Status', anchor=tk.CENTER, width=120)

    tree.heading('ID', text='ID')
    tree.heading('Name', text='Name')
    tree.heading('Position', text='Position')
    tree.heading('Gender', text='Gender')
    tree.heading('Birthday', text='Birthday')
    tree.heading('Status', text='Status')

    tree.grid(row=0, column=0, sticky='nsew')

    # Чтобы Frame с Treeview растягивался
    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

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
        variable1.set('муж')
        birthday_entry.delete(0, END)
        status_entry.delete(0, END)

    def display_data(event):
        selected_item = tree.focus()
        if selected_item:
            row = tree.item(selected_item)['values']
            clear()
            id = row[0]
            name_entry.insert(0, row[1])
            position_entry.insert(0, row[2])
            variable1.set(row[3])
            birthday_entry.insert(0, row[4])
            status_entry.insert(0, row[5])
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
            gender = variable1.get()
            birthday = birthday_entry.get()
            status = status_entry.get()
            if not (name and position and gender and birthday and status):
                messagebox.showerror('Error', 'Enter all fields.')
                return
            update_staff(id, name, position, gender, birthday, status)
            add_to_treeview()
            clear()
            messagebox.showinfo('Success', 'Data has been updated.')

    def insert():
        # id не вводится, т.к. автоинкремент
        name = name_entry.get()
        position = position_entry.get()
        gender = variable1.get()
        birthday = birthday_entry.get()
        status = status_entry.get()
        if not (name and position and gender and birthday and status):
            messagebox.showerror('Error', 'Enter all fields.')
        else:
            insert_staff(name, position, gender, birthday, status)
            add_to_treeview()
            clear()
            messagebox.showinfo('Success', 'Data has been inserted.')
    
    tree.bind('<ButtonRelease>', display_data)

    # Кнопки (ряд 7)
    add_btn = ctk.CTkButton(frame, command=insert, font=font1, text_color='#fff',
                            text='Add Staff', fg_color='#05A312', hover_color='#00850B',
                            bg_color='#161C25', cursor='hand2', corner_radius=15, width=260)
    add_btn.grid(row=7, column=0, columnspan=2, sticky='ew', padx=20, pady=(10, 5))

    clear_btn = ctk.CTkButton(frame, command=lambda: clear(True), font=font1, text_color='#fff',
                              text='New Entry', fg_color='#161C25', hover_color='#FF5002',
                              bg_color='#161C25', border_color='#F15704', border_width=2,
                              cursor='hand2', corner_radius=15, width=260)
    clear_btn.grid(row=8, column=0, columnspan=2, sticky='ew', padx=20, pady=5)

    update_btn = ctk.CTkButton(frame, command=update, font=font1, text_color='#fff',
                               text='Update Staff', fg_color='#161C25', hover_color='#FF5002',
                               bg_color='#161C25', border_color='#F15704', border_width=2,
                               cursor='hand2', corner_radius=15, width=260)
    update_btn.grid(row=8, column=2, columnspan=2, sticky='ew', padx=10, pady=5)

    delete_btn = ctk.CTkButton(frame, command=delete, font=font1, text_color='#fff',
                               text='Delete Staff', fg_color='#E40404', hover_color='#AE0000',
                               bg_color='#161C25', border_color='#E40404', border_width=2,
                               cursor='hand2', corner_radius=15, width=260)
    delete_btn.grid(row=8, column=4, columnspan=2, sticky='ew', padx=10, pady=5)

    # Привязка событий и начальная загрузка данных
    tree.bind('<ButtonRelease>', display_data)
   
    add_to_treeview()
