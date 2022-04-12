#!/usr/bin/env python3

import os, subprocess, shutil
import tkinter as tk
from tkinter import filedialog
import webbrowser
from commands import gui, setup
from data import tkinter_values as tv


class App(tk.Frame):

    def __init__(self, root=None):
        # Setting up GUI window for rendering
        super().__init__(root)
        self.root = root
        # Rendering app menu and main window.
        self.gui = gui.GUI(self.root)   
        self.key_bindings()

    def key_bindings(self):
        self.root.bind('<Control-o>', self.gui.setup_commands.init_repo)
'''
    def frame(self):
        # Labels
        self.project_label = tk.Label(self.root, text="No Project Currently Loaded", font=App.title,
                anchor='center')
        self.project_path = tk.Label(self.root, text=self.project_path_string, font=App.information)
        self.project_information = tk.Label(self.root, text='', font=App.information, wraplength=250, anchor='n')
        self.project_commit_message = tk.Text(self.root, font=App.buttons) 
        self.project_info_title = tk.Label(self.root, text="Terminal Outputs", font=App.title)
        # Placement
        self.project_label.place(x=25, y=10, width=550, height=25)
        self.project_path.place(x=25, y=40, width=550, height=30)
        self.project_info_title.place(x=15, y=75, width=275, height=25)
        self.project_information.place(x=15, y=110, width=275, height=375)
        self.project_commit_message.place(x=310, y=100, width=275, height=375)

    def init_repo(self, event=None):
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

    def clone_repo(self, event=None):
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

    def status(self):
        os.system('cls || clear')
        self.current_status = subprocess.getoutput('git status')
        self.project_information.config(text=self.current_status)
        print(self.current_status)

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

    def remove_files(self):
        files = filedialog.askopenfilenames()
        file_list = self.root.splitlist(files)
        os.system('cls || clear')
        for file in file_list:
            file_name = file.split('/')
            print(file_name[-1])
            os.system(f'git reset {file_name[-1]}')
        self.status()
        '''

if __name__ == '__main__':
    if shutil.which('git') == None:
        root = tk.Tk()
        root.title('Git Not Found')
        root.geometry('300x100')
        error_label = tk.Label(root, text='Please install git', font=('Arial', 18))
        get_git_btn = tk.Button(root, text='Get Git', command=lambda: webbrowser.open('https://git-scm.com/downloads'), font=('Arial', 14))
        error_label.pack()
        get_git_btn.pack()
        root.mainloop()
    else:
        root = tk.Tk()
        root.geometry(f'{tv.width}x{tv.height}')
        root.title('GitPy')
        app = App(root=root)
        app.mainloop()
       