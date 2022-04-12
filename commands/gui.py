import tkinter as tk
from commands import setup
import os
from data import tkinter_values as tv

class GUI(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.window()
        self.setup_commands = setup.Setup(root=self.root,
            project_label=self.project_label,
            project_path_label=self.project_path_label,
            status_label=self.status_label)
        self.menu()
        root.config(menu=self.menubar)

    def menu(self):
        # Creation of window menu options
        self.menubar = tk.Menu(self.root)
        self.setupmenu = tk.Menu(self.menubar, tearoff=0)
        # Setup Menu Options
        self.setupmenu.add_command(label="Init Project(Ctrl+o)", command=self.setup_commands.init_repo)
        self.setupmenu.add_command(label="Clone Project")
        self.setupmenu.add_separator()
        self.setupmenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="Setup", menu=self.setupmenu)
    
    def window(self):
        # Labels
        self.project_label = tk.Label(self.root, text="No Project Currently Loaded", font=tv.title,
                anchor='center')
        self.project_path_label = tk.Label(self.root, text=tv.project_path_string, font=tv.information)
        self.project_commit_message = tk.Text(self.root, font=tv.buttons) 
        self.status_label = tk.Label(self.root, text='Welcome to GitPY!', font=tv.information,
        wraplength=(tv.width)-(50*2))
        
        # Placement
        self.project_label.place(x=25, y=10, width=550, height=25)
        self.project_path_label.place(x=25, y=40, width=550, height=30)
        self.project_commit_message.place(x=25, y=100, width=(tv.width - (25*2)), height=300)
        self.status_label.place(x=50, y=425, width=(tv.width)-(50*2), height=100)