import tkinter as tk
from tkinter import filedialog
import os, sys, subprocess
from data import tkinter_values as tv

class Setup(tk.Frame):
    def __init__(self, root=None, project_label=None, project_path_label=None, status_information=None, terminal_command=None):
        super().__init__(root)
        self.root = root
        self.project_label = project_label
        self.project_path_label = project_path_label
        self.status_information = status_information
        self.terminal_command = terminal_command

    def init_repo(self, event=None):
        # Open dialog box to select working folder
        self.init_directory = filedialog.askdirectory()
        if not self.init_directory:
            pass
        else:
            print(self.init_directory) # Value check
            tv.project_path_string = self.init_directory.replace('/',"\\")
            # Change directory into working folder
            os.chdir(tv.project_path_string)
            # Initilize project and display update in terminal
            os.system('cls || clear')
            command_line = subprocess.check_output('git init')
            #os.system('git init')
            print(command_line.decode('utf-8'), end='\n'*2)
            print('Current working Dicrectory')
            os.system('cd || pwd')
            print(tv.project_path_string)
            # Updating frame information
            path_split = tv.project_path_string.split('\\')
            print(path_split)
            tv.project_title = path_split[-1]
            self.project_label.config(text=f'Working on {path_split[-1].title()}')
            self.project_path_label.config(text=tv.project_path_string)
            self.status_information.config(text=tv.init_prompt)
            self.terminal_command.config(text='git init')

    def download_repo(self, repo, path):
        # Preping local machine for repo download
        os.chdir(path)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Cloning Repo
        url_list = repo[8:].split('/')
        if url_list[0] == 'github.com' and url_list[2][-4:] == '.git':    
            clone_string = 'git clone ' + repo 
            os.system(clone_string)
        self.terminal_command.config(text=f'git clone {repo}')
        # Entering project
        project = url_list[2].split('.')
        os.chdir(project[0])
        print('Current Directory')
        os.system('cd')
        tv.project_path_string = os.getcwd()
        # Updating frame
        path_split = tv.project_path_string.split('\\')
        tv.project_title = path_split[-1]
        self.project_label.config(text=f'Working on {path_split[-1].title()}')
        self.project_path_label.config(text=tv.project_path_string)
        self.status_information.config(text=tv.clone_prompt)
        # Closing repo cloning dialog box
        for widget in self.clone_window.winfo_children():
            widget.destroy()
        self.clone_window.destroy()

    def clone_repo(self, event=None):
        # Create dialog for user to select file destination
        self.clone_directory = filedialog.askdirectory()
        # Saving path for later use
        tv.project_path_string = self.clone_directory
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
                    command=lambda: self.download_repo(self.url_entry.get(), tv.project_path_string))
            self.url_entry.place(x=0, y=0, width=300, height=25)
            self.clone_btn.place(x=75, y=35, width=150, height=30)

    def set_username(self, name):
        tv.name = name
        # Clear terminal
        os.system('cls || clear')
        # Update username
        name_update = f'git config --global user.name "{tv.name}"'
        os.system(name_update)
        print(f'Your new username is {name}')
        self.status_information.config(text=tv.name_prompt)
        self.terminal_command.config(text=name_update)
        # Close dialog box
        for widget in self.update_name_frame.winfo_children():
            widget.destroy()
        self.update_name_frame.destroy()

    def update_name(self):
        self.update_name_frame = tk.Tk()
        self.update_name_frame.geometry('300x75')
        self.update_name_frame.title('Update Name')
        self.name_entry = tk.Entry(self.update_name_frame)
        self.update_name_btn = tk.Button(self.update_name_frame, text='Set Name', font=tv.buttons,
            command=lambda: self.set_username(self.name_entry.get()))
        # Placement
        self.name_entry.place(x=0, y=0, width=300, height=25)
        self.update_name_btn.place(x=75, y=30, width=150, height=30)

    def set_email(self, email):
        tv.email = email
        # Clear terminal
        os.system('cls || clear')
        # Update email
        email_update = f'git config --global user.email "{email}"'
        os.system(email_update)
        # Explination
        print(f'Your new email is {email}')
        self.status_information.config(text=tv.email_prompt)
        self.terminal_command.config(text=email_update)
        # Close dialog box
        for widget in self.update_email_frame.winfo_children():
            widget.destroy()
        self.update_email_frame.destroy()

    def update_email(self):
        self.update_email_frame = tk.Tk()
        self.update_email_frame.geometry('300x75')
        self.update_email_frame.title('Update Email')
        self.email_entry = tk.Entry(self.update_email_frame)
        self.update_email_btn = tk.Button(self.update_email_frame, text='Set Email', font=tv.buttons,
            command=lambda: self.set_email(self.email_entry.get()))
        # Placement
        self.email_entry.place(x=0, y=0, width=300, height=25)
        self.update_email_btn.place(x=75, y=30, width=150, height=30)