import tkinter as tk
from commands import setup

class GUI(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.setup_commands = setup.Setup(self.root)
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
        pass