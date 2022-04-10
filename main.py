#!/usr/bin/env python3
''' Source commands https://education.github.com/git-cheat-sheet-education.pdf
                    https://git-scm.com/docs/git
                    https://about.gitlab.com/images/press/git-cheat-sheet.pdf
'''
import os, subprocess, shutil
import tkinter as tk
from tkinter import filedialog
import webbrowser

def check_git():
    if shutil.which('git') == None:
        return False
    return True

def download_git():
    webbrowser.open('https://git-scm.com/downloads')

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
        self.setupmenu.add_command(label="Update Name", command=self.update_name)
        self.setupmenu.add_command(label="Update Email", command=self.update_email)
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
        self.project_label = tk.Label(self.root, text="No Project Currently Loaded", font=App.title,
                anchor='center')
        self.project_path = tk.Label(self.root, text=self.project_path_string, font=App.information)
        # Placement
        self.project_label.place(x=25, y=15, width=450, height=25)
        self.project_path.place(x=25, y=50, width=450, height=50)

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
        # Preping local machine for repo download
        os.chdir(path)
        os.system('cls' if os.name == 'nt' else 'clear')
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
        print(f'git clone {repo}', end='\n'*2)
        # Entering project
        project = url_list[2].split('.')
        os.chdir(project[0])
        print('Current Directory')
        os.system('cd')
        self.project_path_string = os.getcwd()
        # Updating frame
        path_split = self.project_path_string.split('/')
        self.project_label.config(text=f'Working on {path_split[-1].title()}')
        self.project_path.config(text=self.project_path_string)
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

    def set_username(self, name):
        # Clear terminal
        os.system('cls || clear')
        # Update username
        name_update = f'git config --global user.name "{name}"'
        os.system(name_update)
        # Explination
        print()
        print('The line below changes the name attached to your commits. The name assoicated with this '+
        'command is how you are represented when you push your commits to a repo.', end='\n'*2)
        print(f'The following command was ran: {name_update}')
        print(f'Your new username is {name}')
        # Close dialog box
        for widget in self.update_name_frame.winfo_children():
            widget.destroy()
        self.update_name_frame.destroy()

    def update_name(self):
        self.update_name_frame = tk.Tk()
        self.update_name_frame.geometry('300x75')
        self.update_name_frame.title('Update Name')
        self.name_entry = tk.Entry(self.update_name_frame)
        self.update_name_btn = tk.Button(self.update_name_frame, text='Set Name', font=App.buttons,
            command=lambda: self.set_username(self.name_entry.get()))
        # Placement
        self.name_entry.place(x=0, y=0, width=300, height=25)
        self.update_name_btn.place(x=75, y=30, width=150, height=30)

    def set_email(self, email):
        # Clear terminal
        os.system('cls || clear')
        # Update email
        email_update = f'git config --global user.email "{email}"'
        os.system(email_update)
        # Explination
        print()
        print('The line below changes the email attached to your commits. The email assoicated with this '+
        'command is how you are represented when you push your commits to a repo.', end='\n'*2)
        print(f'The following command was ran: {email_update}')
        print(f'Your new email is {email}')
        # Close dialog box
        for widget in self.update_email_frame.winfo_children():
            widget.destroy()
        self.update_email_frame.destroy()

    def update_email(self):
        self.update_email_frame = tk.Tk()
        self.update_email_frame.geometry('300x75')
        self.update_email_frame.title('Update Email')
        self.email_entry = tk.Entry(self.update_email_frame)
        self.update_email_btn = tk.Button(self.update_email_frame, text='Set Email', font=App.buttons,
            command=lambda: self.set_email(self.email_entry.get()))
        # Placement
        self.email_entry.place(x=0, y=0, width=300, height=25)
        self.update_email_btn.place(x=75, y=30, width=150, height=30)

if __name__ == '__main__':
    if check_git() == True:
        root = tk.Tk()
        root.geometry('500x300')
        root.title('GitPy')
        app = App(root=root)
        app.mainloop()
    else:
        root = tk.Tk()
        root.title('Git Not Found')
        root.geometry('300x100')
        error_label = tk.Label(root, text='Please install git', font=('Arial', 18))
        get_git_btn = tk.Button(root, text='Get Git', command=download_git, font=('Arial', 14))
        error_label.pack()
        get_git_btn.pack()
        root.mainloop()