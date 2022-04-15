import tkinter as tk
from tkinter import filedialog
import os, sys, subprocess
from data import tkinter_values as tv

class Branch(tk.Frame):
    def __init__(self, root=None, project_label=None, project_path_label=None, status_information=None, terminal_command=None):
        super().__init__(root)
        self.root = root
        self.project_label = project_label
        self.project_path_label = project_path_label
        self.status_information = status_information
        self.terminal_command = terminal_command
        
    def branches(self, event=None):
        os.system('cls || clear')
        branches = subprocess.getoutput('git branch')
        print(branches)
        self.status_information.config(text=tv.branch_prompt)
    
    def create_branch(self, branch):
        branch_output = subprocess.getoutput(f'git branch {branch}')
        self.status_information.config(text=tv.create_branch_prompt)
        self.terminal_command.config(text=f'git branch {branch}')
        for widget in self.branch_window.winfo_children():
            widget.destroy()
        self.branch_window.destroy()
    
    def new_branch(self):
        self.branch_window = tk.Tk()
        self.branch_window.geometry('300x75')
        self.branch_window.title('New Branch')
        self.branch_entry = tk.Entry(self.branch_window)
        self.branch_btn = tk.Button(self.branch_window, text='Create Branch',
                    command=lambda: self.create_branch(branch=self.branch_entry.get()))
        self.branch_entry.place(x=0, y=0, width=300, height=25)
        self.branch_btn.place(x=75, y=35, width=150, height=30)

    def checkout_branch(self, branch):
        os.system(f'git checkout {branch}')
        for widget in self.branch_window.winfo_children():
            widget.destroy()
        self.branch_window.destroy()
    
    def switch_branch(self):
        self.branch_list = subprocess.getoutput('git branch').split('\n')
        self.branch_window = tk.Tk()
        self.branch_window.geometry('300x100')
        self.branch_window.title('Switch Branch')
        self.selection = tk.StringVar(self.branch_window)
        current = [x for x in self.branch_list if x[0] == '*']
        print(current[0])
        self.selection.set(current[0])
        self.branch_dropdown = tk.OptionMenu(self.branch_window, self.selection, *self.branch_list)
        self.branch_btn = tk.Button(self.branch_window, text='Switch Branch',
                    command=lambda: self.checkout_branch(branch=self.selection.get()))
        self.branch_dropdown.place(x=75, y=0, width=150, height=40)
        self.branch_btn.place(x=75, y=50, width=150, height=30)
    