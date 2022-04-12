import tkinter as tk
from tkinter import filedialog
import os, sys, subprocess
from data import tkinter_values as tv

class Stage(tk.Frame):
    def __init__(self, root=None, project_label=None, project_path_label=None, status_information=None, terminal_command=None):
        super().__init__(root)
        self.root = root
        self.project_label = project_label
        self.project_path_label = project_path_label
        self.status_information = status_information
        self.terminal_command = terminal_command

    def status(self):
        os.system('cls || clear')
        os.system('git status')
        self.status_information.config(text=tv.status_prompt)
        self.terminal_command.config(text='git status')

    def add_files(self):
        file = filedialog.askopenfilenames()
        files = self.root.splitlist(file)
        os.system('cls || clear')
        #self.status()
        for file_to_add in files:
            file_name = file_to_add.split('/')
            print(file_name[-1])
            os.system(f'git add {file_name[-1]}')
        self.status()
        self.status_information.config(text=tv.add_file_prompt)
        self.terminal_command.config(text='git add {filename}')

    def remove_files(self):
        files = filedialog.askopenfilenames()
        file_list = self.root.splitlist(files)
        os.system('cls || clear')
        for file in file_list:
            file_name = file.split('/')
            print(file_name[-1])
            os.system(f'git reset {file_name[-1]}')
        self.status()
        self.status_information.config(text=tv.add_file_prompt)
        self.terminal_command.config(text='git remove {filename}')