#!/usr/bin/env python3
# Source commands https://education.github.com/git-cheat-sheet-education.pdf

import os
import tkinter as tk
from tkinter import filedialog

class App(tk.Frame):
    # Fonts
    title = ('Arial', 16)
    buttons = ('Arial', 14)
    information = ('Arial', 12)

    def __init__(self, root=None):
        # Setting up GUI window for rendering
        super().__init__(root)
        self.root = root
        # Creating empty working path variable for alter useage
        self.project_path_string = ''
        # Rendering app menu and main window.
        self.menu()
        root.config(menu=self.menubar)
        self.frame()

    def menu(self):
        # Creation of window menu options
        self.menubar = tk.Menu(self.root)
        self.setupmenu = tk.Menu(self.menubar, tearoff=0)
        # Setup Menu Options
        self.setupmenu.add_command(label="Init Project", command=self.init_repo)
        self.setupmenu.add_command(label="Clone Project", command=self.clone_repo)
        self.setupmenu.add_separator()
        self.setupmenu.add_command(label="Update Name")
        self.setupmenu.add_command(label="Update Email")
        self.setupmenu.add_separator()
        self.setupmenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="Setup", menu=self.setupmenu)
        # Stage Menu Options
        self.stagemenu = tk.Menu(self.menubar, tearoff=0)
        self.stagemenu.add_command(label="Status")
        self.stagemenu.add_separator()
        self.stagemenu.add_command(label="Stage File(s)")
        self.stagemenu.add_command(label="Unstage File(s)")
        self.stagemenu.add_separator()
        self.stagemenu.add_command(label="Show Unstaged Changes")
        self.stagemenu.add_command(label="Show Staged Changes")
        self.stagemenu.add_separator()
        self.stagemenu.add_command(label="Commit")
        self.menubar.add_cascade(label="Staging", menu=self.stagemenu)
        # Help Menu Options
        self.branchmenu = tk.Menu(self.menubar, tearoff=0)
        self.branchmenu.add_command(label="List Branches")
        self.branchmenu.add_command(label="New Branch")
        self.branchmenu.add_separator()
        self.branchmenu.add_command(label="Switch Branch")
        self.branchmenu.add_command(label="Merge Branch")
        self.branchmenu.add_separator()
        self.branchmenu.add_command(label="Commit History")
        self.branchmenu.add_command(label="Compare Commits")
        self.branchmenu.add_command(label="Compare Changes")
        self.menubar.add_cascade(label="Branch", menu=self.branchmenu)

        self.updatemenu = tk.Menu(self.menubar, tearoff=0)
        self.updatemenu.add_command(label="Fetch")
        self.updatemenu.add_command(label="Pull")
        self.updatemenu.add_separator()
        self.updatemenu.add_command(label="Merge")
        self.updatemenu.add_command(label="Push")
        self.menubar.add_cascade(label='Update', menu=self.updatemenu)

    def frame(self):
        # Labels
        self.project_label = tk.Label(root, text="No Project Currently Loaded", font=App.title,
                anchor='center')
        self.project_path = tk.Label(root, text=self.project_path_string, font=App.information)
        # Placement
        self.project_label.place(x=100, y=15, width=300, height=25)
        self.project_path.place(x=50, y=40, width=400, height=25)

    def init_repo(self):
        # Open dialog box to select working folder
        self.init_directory = filedialog.askdirectory()
        if not self.init_directory:
            pass
        else:
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

    def download_repo(self, repo, path):
        ###########################################################################
        #       This section of code needs to be put through testing for
        #       error handling. When preforming actions as you should everything
        #       works but pressing cancel throws errors
        ###########################################################################
        # Preping local machine for repo download
        os.chdir(path)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Current working Dicrectory')
        os.system('cd' if os.name == 'nt' else 'pwd')
        print()
        # Cloning Repo
        url_list = repo[8:].split('/')
        if url_list[0] == 'github.com' and url_list[2][-4:] == '.git':    
            clone_string = 'git clone ' + repo 
            os.system(clone_string)
        print()
        print('This will retrive a github repo and install it locally on your '+
        'machine at the specified path. The above code is what git displays while retriving '+
        'the repo. If the repo fails, there will be an error message. The follow line of '+
        'code was ran.', end='\n'*2)
        print(f'git clone {repo}')
        # Closing repo cloning dialog box
        for widget in self.clone_window.winfo_children():
            widget.destroy()
        self.clone_window.destroy()

    def clone_repo(self):
        # Create dialog for user to select file destination
        self.clone_directory = filedialog.askdirectory()
        # Saving path for later use
        self.project_path_string = self.clone_directory
        # Checking if folder was selected
        if not self.clone_directory:
            pass
        else:
            # Creating clone repo dialog box
            self.clone_window = tk.Tk()
            self.clone_window.geometry('300x75')
            self.clone_window.title('Clone Repo')
            self.url_entry = tk.Entry(self.clone_window)
            self.clone_btn = tk.Button(self.clone_window, text='Clone',
                    command=lambda: self.download_repo(self.url_entry.get(), self.project_path_string))
            self.url_entry.place(x=0, y=0, width=300, height=25)
            self.clone_btn.place(x=75, y=35, width=150, height=30)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x300')
    root.title('GitPy')
    app = App(root=root)
    app.mainloop()