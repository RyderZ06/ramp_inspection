import customtkinter as ctk
import tkinter as tk

from data_manager import *
from tkinter import ttk, messagebox, StringVar, END
from libra import *

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

def create_ramp_frame(root):
    frame = root
    
    reg_number_label = ctk.CTkLabel(frame, font=font1, text='Reg Number:', text_color='#fff', bg_color='#161C25')
    reg_number_label.grid(row=0, column=0, sticky='w', padx=20, pady=(20, 10))
    
    reg_number_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                    border_color='#0C9295', border_width=2, width=180)
    reg_number_entry.grid(row=0, column=1, sticky='w', padx=10, pady=(20, 10))
    
    open_date_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    open_date_label.grid(row=1, column=0, sticky='w', padx=20, pady=10)
    
    open_date_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                   border_color='#0C9295', border_width=2, width=180)
    open_date_entry.grid(row=1, column=1, sticky='w', padx=10, pady=10)
    
    finding_status_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    finding_status_label.grid(row=2, column=0, sticky='w', padx=20, pady=10)
    
    finding_status_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    finding_status_entry.grid(row=2, column=1, sticky='w', padx=10, pady=10)
    
    close_date_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    close_date_label.grid(row=3, column=0, sticky='w', padx=20, pady=10)
    
    close_date_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    close_date_entry.grid(row=3, column=1, sticky='w', padx=10, pady=10)
    
    aircraft_type_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    aircraft_type_label.grid(row=4, column=0, sticky='w', padx=20, pady=10)
    
    aircraft_type_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    aircraft_type_entry.grid(row=4, column=1, sticky='w', padx=10, pady=10)
    
    finding_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    finding_label.grid(row=5, column=0, sticky='w', padx=10, pady=10)
    
    finding_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    finding_entry.grid(row=5, column=1, sticky='w', padx=10, pady=10)
    
    category_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    category_label.grid(row=6, column=0, sticky='w', padx=10, pady=10)
    
    category_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    category_entry.grid(row=6, column=1, sticky='w', padx=10, pady=10)
    
    reference_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    reference_label.grid(row=7, column=0, sticky='w', padx=10, pady=10)
    
    reference_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    reference_entry.grid(row=7, column=1, sticky='w', padx=10, pady=10)
    
    action_taken_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    action_taken_label.grid(row=8, column=0, sticky='w', padx=10, pady=10)
    
    action_taken_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    action_taken_entry.grid(row=8, column=1, sticky='w', padx=10, pady=10)
    
    audit_number_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    audit_number_label.grid(row=9, column=0, sticky='w', padx=10, pady=10)
    
    audit_number_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    audit_number_entry.grid(row=9, column=1, sticky='w', padx=10, pady=10)
    
    audit_type_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    audit_type_label.grid(row=10, column=0, sticky='w', padx=10, pady=10)
    
    audit_type_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    audit_type_entry.grid(row=10, column=1, sticky='w', padx=10, pady=10)
    
    auditor_name_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    auditor_name_label.grid(row=11, column=0, sticky='w', padx=10, pady=10)
    
    auditor_name_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    auditor_name_entry.grid(row=11, column=1, sticky='w', padx=10, pady=10)
    
    location_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    location_label.grid(row=12, column=0, sticky='w', padx=10, pady=10)
    
    location_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    location_entry.grid(row=12, column=1, sticky='w', padx=10, pady=10)
    
    finding_number_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    finding_number_label.grid(row=13, column=0, sticky='w', padx=10, pady=10)
    
    finding_number_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    finding_number_entry.grid(row=13, column=1, sticky='w', padx=10, pady=10)
    
    item_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    item_label.grid(row=14, column=0, sticky='w', padx=10, pady=10)
    
    item_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    item_entry.grid(row=14, column=1, sticky='w', padx=10, pady=10)
    
    customer_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    customer_label.grid(row=15, column=0, sticky='w', padx=10, pady=10)
    
    customer_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    customer_entry.grid(row=15, column=1, sticky='w', padx=10, pady=10)
    
    department_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    department_label.grid(row=16, column=0, sticky='w', padx=10, pady=10)
    
    department_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    department_entry.grid(row=16, column=1, sticky='w', padx=10, pady=10)
    
    recommended_corrective_action_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    recommended_corrective_action_label.grid(row=17, column=0, sticky='w', padx=10, pady=10)
    
    recommended_corrective_action_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    recommended_corrective_action_entry.grid(row=17, column=1, sticky='w', padx=10, pady=10)
    
    country_label = ctk.CTkLabel(frame, font=font1, text='Position:', text_color='#fff', bg_color='#161C25')
    country_label.grid(row=18, column=0, sticky='w', padx=10, pady=10)
    
    country_entry = ctk.CTkEntry(frame, font=font1, text_color='#000', fg_color='#fff',
                                  border_color='#0C9295', border_width=2, width=180)
    country_entry.grid(row=18, column=1, sticky='w', padx=10, pady=10)