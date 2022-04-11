import tkinter as tk
from tkinter import filedialog
import os, sys, subprocess

class Setup(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root

    def init_repo(self, event=None):
        # Open dialog box to select working folder
        self.init_directory = filedialog.askdirectory()
        if not self.init_directory:
            pass
        else:
            print(self.init_directory)
            self.project_path_string = self.init_directory
            # Change directory into working folder
            os.chdir(self.project_path_string)
            # Initilize project and display update in terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print('The following line of code will initialize the selected folder as the parent folder \
            for your project. Your folder should be named after your project')
            print('The follow command will be ran: git init', end='\n'*2)
            os.system('git init')
            print('')
            print('Current working Dicrectory')
            os.system('cd' if os.name == 'nt' else 'pwd')
            # Updating frame information
            path_split = self.project_path_string.split('/')
            self.project_label.config(text=f'Working on {path_split[-1].title()}')
            self.project_path.config(text=self.project_path_string)