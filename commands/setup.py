import tkinter as tk
from tkinter import filedialog
import os, sys, subprocess
from data import tkinter_values as tv

class Setup(tk.Frame):
    def __init__(self, root=None, project_label=None, project_path_label=None, status_label=None):
        super().__init__(root)
        self.root = root
        self.project_label = project_label
        self.project_path_label = project_path_label
        self.status_label = status_label

    def init_repo(self, event=None):
        # Open dialog box to select working folder
        self.init_directory = filedialog.askdirectory()
        if not self.init_directory:
            pass
        else:
            print(self.init_directory) # Value check
            tv.project_path_string = self.init_directory.replace('/','\\')
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
            path_split = tv.project_path_string.split('/')
            self.project_label.config(text=f'Working on {path_split[-1].title()}')
            self.project_path_label.config(text=tv.project_path_string)
            self.status_label.config(text=tv.init_prompt)

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