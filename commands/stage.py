import tkinter as tk
from tkinter import filedialog
import os
import subprocess
from data import tkinter_values as tv
import datetime as dt


class Stage(tk.Frame):
    def __init__(
        self,
        root=None,
        project_label=None,
        project_path_label=None,
        status_information=None,
        terminal_command=None,
    ):
        # Importing information for class to use
        super().__init__(root)
        self.root = root
        self.project_label = project_label
        self.project_path_label = project_path_label
        self.status_information = status_information
        self.terminal_command = terminal_command

    def status(self):
        """Get an overview of whats currently going on in git"""
        os.system("cls || clear")
        os.system("git status")
        self.status_information.config(text=tv.status_prompt)
        self.terminal_command.config(text="git status")

    def add_files(self):
        """A dialog box is presented to the user to add file(s) to
        staging in git"""
        file = filedialog.askopenfilenames()
        files = self.root.splitlist(file)
        os.system("cls || clear")
        # Adding files to staged area
        for file_to_add in files:
            file_name = file_to_add.split("/")
            print(file_name[-1])
            os.system(f"git add {file_name[-1]}")
        # Displaying status to comfirm additions
        self.status()
        # Updating tkinter widgets
        self.status_information.config(text=tv.add_file_prompt)
        self.terminal_command.config(text="git add {filename}")

    def remove_files(self):
        """A dialog box is presented to the user to remove file(s) to
        staging in git"""
        files = filedialog.askopenfilenames()
        file_list = self.root.splitlist(files)
        os.system("cls || clear")
        for file in file_list:
            file_name = file.split("/")
            print(file_name[-1])
            os.system(f"git reset {file_name[-1]}")
        # Displaying status to comfirm removables
        self.status()
        # Updating tkinter widgets
        self.status_information.config(text=tv.add_file_prompt)
        self.terminal_command.config(text="git remove {filename}")

    def staged_files(self, event=None):
        """Output difference within staged files from last commit"""
        os.system("cls || clear")
        staged_difference = subprocess.getoutput("git diff --staged")
        # Getting time stamp for file name
        date_item = dt.datetime.now().strftime("%Y_%m_%d-%I%M%S_%p")
        os.chdir(tv.home_path)
        # Changing location to save report
        os.chdir("outputs\\staged")
        # Creation and inserting information into file
        with open(f"{tv.project_title}_staged_{date_item}.txt", "w") as file:
            file.write(staged_difference)
        # Opening file in notepad
        os.system(f"notepad {tv.project_title}_staged_{date_item}")
        os.chdir(tv.project_path_string)
        print("Check the output files for more information")
        self.terminal_command.config(text="git diff")

    def unstaged_files(self, event=None):
        """Output difference of unstaged files from last commit"""
        os.system("cls || clear")
        staged_difference = subprocess.getoutput("git diff")
        # Getting time stamp for file name
        date_item = dt.datetime.now().strftime("%Y_%m_%d-%I%M%S_%p")
        os.chdir(tv.home_path)
        # Changing location to save report
        os.chdir("outputs\\unstaged")
        # Creation and inserting information into file
        with open(f"{tv.project_title}_unstaged_{date_item}.txt", "w") as file:
            file.write(staged_difference)
            # Opening file in notepad
        os.system(f"notepad {tv.project_title}_unstaged_{date_item}")
        os.chdir(tv.project_path_string)
        print("Check the output files for more information")

    def output_files(self, event=None):
        """Quick access to all output files"""
        os.system("cls || clear")
        os.chdir(tv.home_path)
        os.chdir("outputs")
        print(os.getcwd())
        os.system("start ..\\outputs")
        if tv.project_path_string != "":
            os.chdir(tv.project_path_string)
        os.chdir(tv.home_path)

    def commit(self, event=None):
        """Starting a full commit, this must be finished from the terminal"""
        os.system("git commit")
        self.status_information.config(text=tv.commit_prompt)

    def send_commit(self, message, event=None):
        """Helper function that completes quick commit"""
        os.system("cls || clear")
        commit_message = subprocess.getoutput(f'git commit -m "{message}"')
        print(commit_message)
        for widget in self.commit_window.winfo_children():
            widget.destroy()
        self.commit_window.destroy()

    def quick_commit(self, event=None):
        """Presents user with a dialog box to input information for a
        quick commit"""
        self.commit_window = tk.Tk()
        self.commit_window.geometry("300x75")
        self.commit_window.title("Quick Commit Message")
        self.commit_entry = tk.Entry(self.commit_window)
        self.commit_btn = tk.Button(
            self.commit_window,
            text="Quick Commit",
            command=lambda: self.send_commit(message=self.commit_entry.get()),
        )
        self.commit_entry.place(x=0, y=0, width=300, height=25)
        self.commit_btn.place(x=75, y=35, width=150, height=30)

    def push(self, event=None):
        """Pushing local commits to github repository"""
        os.system("git push")
        self.status_information.config(text=tv.push_prompt)

    def pull(self, event=None):
        """Retriving and update of the repository from github"""
        os.system("git pull")
        self.status_information.config(text=tv.pull_prompt)
