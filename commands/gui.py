import tkinter as tk
from commands import setup, stage
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
            status_information=self.status_information,
            terminal_command = self.terminal_command)
        self.stage_commands = stage.Stage(root=self.root,
            project_label=self.project_label,
            project_path_label=self.project_path_label,
            status_information=self.status_information,
            terminal_command = self.terminal_command)
        self.menu()
        root.config(menu=self.menubar)

    def menu(self):
        # Creation of window menu options
        self.menubar = tk.Menu(self.root)
        self.setupmenu = tk.Menu(self.menubar, tearoff=0)
        self.stagemenu = tk.Menu(self.menubar, tearoff=0)
        self.commitmenu = tk.Menu(self.menubar, tearoff=0)
        self.branchmenu = tk.Menu(self.menubar, tearoff=0)
        self.trackmenu = tk.Menu(self.menubar, tearoff=0)
        # Setup Menu Options
        self.setupmenu.add_command(label="Init Project   (Ctrl+O)", command=self.setup_commands.init_repo)
        self.setupmenu.add_command(label="Clone Project   (Ctrl+Shift+O)", command=self.setup_commands.clone_repo)
        self.setupmenu.add_separator()
        self.setupmenu.add_command(label="Change Name", command=self.setup_commands.update_name)
        self.setupmenu.add_command(label="Change Email", command=self.setup_commands.update_email)
        self.setupmenu.add_separator()
        self.setupmenu.add_command(label="Exit", command=self.root.quit)
        # Stage Menu
        self.stagemenu.add_command(label='Status', command=self.stage_commands.status)
        self.stagemenu.add_separator()
        self.stagemenu.add_command(label='Add File(s)', command=self.stage_commands.add_files)
        self.stagemenu.add_command(label='Remove File(s)', command=self.stage_commands.remove_files)
        self.stagemenu.add_separator()
        self.stagemenu.add_command(label="Unstaged Changes", command=self.stage_commands.unstaged_files)
        self.stagemenu.add_command(label="Staged Changes", command=self.stage_commands.staged_files)
        self.stagemenu.add_command(label="Open Changes Output   (Ctrl+c)", command=self.stage_commands.output_files)
        # Commit Menu
        self.commitmenu.add_command(label="Full Commit", command=self.stage_commands.commit)
        self.commitmenu.add_command(label="Quick Commit", command=self.stage_commands.quick_commit)
        self.commitmenu.add_separator()
        self.commitmenu.add_command(label='Push   (Ctrl+P)', command=self.stage_commands.push)
        self.commitmenu.add_command(label='Pull   (Ctrl+Shift+P)', command=self.stage_commands.pull)
        # Branch Menu
        self.branchmenu.add_command(label='List Branches')
        self.branchmenu.add_command(label='Switch Branch')
        self.branchmenu.add_command(label='New Branch')
        self.branchmenu.add_separator()
        self.branchmenu.add_command(label='Merge Branches')
        self.branchmenu.add_separator()
        self.branchmenu.add_command(label='Changes on Current Branch')
        self.branchmenu.add_command(label='Compare Branch Log')
        self.branchmenu.add_command(label='Compare Branch Changes')
        # Tracking Menu
        self.trackmenu.add_command(label='Track File')
        self.trackmenu.add_command(label='Remove File(s)')
        self.trackmenu.add_command(label='Move File(s)')
        self.trackmenu.add_separator()
        self.trackmenu.add_command(label='Show Tracking Log')
        # Adding Sub menus to main menu bar
        self.menubar.add_cascade(label="Setup", menu=self.setupmenu)
        self.menubar.add_cascade(label='Stage', menu=self.stagemenu)
        self.menubar.add_cascade(label='Commit', menu=self.commitmenu)
        self.menubar.add_cascade(label='Branch', menu=self.branchmenu)
        self.menubar.add_cascade(label='Tracking', menu=self.trackmenu)
    
    def window(self):
        # Labels
        self.project_label = tk.Label(self.root,text="No Project Currently Loaded", font=tv.title,     # Project name
                anchor='center')
        self.project_path_label = tk.Label(self.root, text=tv.project_path_string, font=tv.information) # Project path
        self.project_commit_message = tk.Text(self.root, font=tv.buttons)                               # Text box for commit message
        self.status_label = tk.Label(self.root, text='Information output', font=tv.title, anchor='n')   # Information label
        self.status_information = tk.Label(self.root, text='Welcome to GitPY!', font=tv.information,    # Information output
        wraplength=250, anchor='nw')
        self.terminal_command_label = tk.Label(self.root, text="Terminal Command", font=tv.title)       # Terminal Label
        self.terminal_command = tk.Label(self.root, text='', font=tv.information, wraplength=250,       # Terminal output
        anchor='n')
        
        # Placement
        self.project_label.place(x=25, y=10, width=550, height=25)              # Project name
        self.project_path_label.place(x=25, y=40, width=550, height=25)         # Project path
        self.project_commit_message.place(x=25, y=70, width=550, height=300)    # Text box for commit message
        self.status_label.place(x=25, y=375, width=250, height=25)              # Status label
        self.status_information.place(x=25, y=400, width=250, height=150)       # Information output
        self.terminal_command_label.place(x=325, y=375, width=250, height=25)
        self.terminal_command.place(x=325, y=400, width=250, height=125)