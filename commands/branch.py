import tkinter as tk
import os
import subprocess
from data import tkinter_values as tv
import datetime as dt


class Branch(tk.Frame):
    def __init__(
        self,
        root=None,
        project_label=None,
        project_path_label=None,
        status_information=None,
        terminal_command=None,
    ):
        super().__init__(root)
        self.root = root
        self.project_label = project_label
        self.project_path_label = project_path_label
        self.status_information = status_information
        self.terminal_command = terminal_command
    
    def project_warning(self):
        os.system('cls || clear')
        print('Please load a project first')
        self.status_information.config(text='Please load a project before \
            using commands')

    def branches(self, event=None):
        if tv.project_path_string != '':
            os.system("cls || clear")
            branches = subprocess.getoutput("git branch")
            print(branches)
            self.status_information.config(text=tv.branch_prompt)
        else:
            self.project_warning()

    def create_branch(self, branch):
        if tv.project_path_string != '':
            branch_output = subprocess.getoutput(f"git branch {branch}")
            self.status_information.config(text=tv.create_branch_prompt)
            self.terminal_command.config(text=f"git branch {branch}")
            for widget in self.branch_window.winfo_children():
                widget.destroy()
            self.branch_window.destroy()
            os.system("cls || clear")
            print(branch_output)
        else:
            self.project_warning()

    def new_branch(self):
        if tv.project_path_string != '':
            self.branch_window = tk.Tk()
            self.branch_window.geometry("300x75")
            self.branch_window.title("New Branch")
            self.branch_entry = tk.Entry(self.branch_window)
            self.branch_btn = tk.Button(
                self.branch_window,
                text="Create Branch",
                command=lambda: self.create_branch(branch=self.branch_entry.get()),
            )
            self.branch_entry.place(x=0, y=0, width=300, height=25)
            self.branch_btn.place(x=75, y=35, width=150, height=30)
        else:
            self.project_warning()

    def checkout_branch(self, branch):
        if tv.project_path_string != '':
            os.system(f"git checkout {branch}")
            for widget in self.branch_window.winfo_children():
                widget.destroy()
            self.branch_window.destroy()
        else:
            self.project_warning()

    def switch_branch(self):
        if tv.project_path_string != '':
            self.branch_list = subprocess.getoutput("git branch").split("\n")
            self.branch_window = tk.Tk()
            self.branch_window.geometry("300x100")
            self.branch_window.title("Switch Branch")
            self.selection = tk.StringVar(self.branch_window)
            current = [x for x in self.branch_list if x[0] == "*"]
            print(current[0])
            self.selection.set(current[0])
            self.branch_dropdown = tk.OptionMenu(
                self.branch_window, self.selection, *self.branch_list
            )
            self.branch_btn = tk.Button(
                self.branch_window,
                text="Switch Branch",
                command=lambda: self.checkout_branch(branch=self.selection.get()),
            )
            self.branch_dropdown.place(x=75, y=0, width=150, height=40)
            self.branch_btn.place(x=75, y=50, width=150, height=30)
        else:
            self.project_warning()

    def merge_to_current(self, branch):
        if tv.project_path_string != '':
            os.system("cls || clear")
            if "*" not in branch:
                os.system(f"git merge {branch}")
            else:
                print("Cannot merge current branch with itself.")
            for widget in self.branch_window.winfo_children():
                widget.destroy()
            self.branch_window.destroy()
            os.system("git commit")
        else:
            self.project_warning()

    def merge_branch(self, event=None):
        if tv.project_path_string != '':
            self.branch_list = subprocess.getoutput("git branch").split("\n")
            self.branch_window = tk.Tk()
            self.branch_window.geometry("300x100")
            self.branch_window.title("Merge Branch")
            self.selection = tk.StringVar(self.branch_window)
            current = [x for x in self.branch_list if x[0] == "*"]
            print(current[0])
            self.selection.set(current[0])
            self.branch_dropdown = tk.OptionMenu(
                self.branch_window, self.selection, *self.branch_list
            )
            self.branch_btn = tk.Button(
                self.branch_window,
                text="Merge Branch",
                command=lambda: self.merge_to_current(branch=self.selection.get()),
            )
            self.branch_dropdown.place(x=75, y=0, width=150, height=40)
            self.branch_btn.place(x=75, y=50, width=150, height=30)
        else:
            self.project_warning()

    def branch_commits(self):
        if tv.project_path_string != '':
            os.system("cls || clear")
            self.branch_list = subprocess.getoutput("git branch").split("\n")
            branch = [x for x in self.branch_list if x[0] == "*"]
            branch = branch[2:]
            branch_commit_history = subprocess.getoutput("git log")
            date_item = dt.datetime.now().strftime("%Y_%m_%d-%I%M%S_%p")
            os.chdir(tv.home_path)
            os.chdir("outputs\\commit_history")
            with open(f"{tv.project_title}_{branch}_{date_item}.txt", "w") as file:
                file.write(branch_commit_history)
            os.system(f"notepad {tv.project_title}_{branch}_{date_item}")
            os.chdir(tv.project_path_string)
            print("Check the output files for more information")
        else:
            self.project_warning()

    def compare_branches(self, branch1, branch2):
        if tv.project_path_string != '':
            os.system("cls || clear")
            bran_A = branch1[2:].strip()
            bran_B = branch2.strip()
            branch_log = subprocess.getoutput(f"git log {bran_B} {bran_A}")
            date_item = dt.datetime.now().strftime("%Y_%m_%d-%I%M%S_%p")
            os.chdir(tv.home_path)
            os.chdir("outputs\\compare_branch")
            file_name = f"{tv.project_title}_{bran_A}-{bran_B}_{date_item}.txt"
            with open(file_name, "w") as file:
                file.write(branch_log)
            os.system(f"notepad {file_name}")
            os.chdir(tv.project_path_string)
            print("Check the output files for more information")
            for widget in self.branch_window.winfo_children():
                widget.destroy()
            self.branch_window.destroy()
        else:
            self.project_warning()

    def branch_compare(self):
        if tv.project_path_string != '':
            self.branch_list1 = subprocess.getoutput("git branch").split("\n")
            self.branch_list2 = self.branch_list1
            self.branch_window = tk.Tk()
            self.branch_window.geometry("300x150")
            self.branch_window.title("Compare Branch")
            self.selection1 = tk.StringVar(self.branch_window)
            self.selection2 = tk.StringVar(self.branch_window)
            self.selection1.set(self.branch_list1[0])
            self.selection2.set(self.branch_list2[0])
            self.branch1_dropdown = tk.OptionMenu(
                self.branch_window, self.selection1, *self.branch_list1
            )
            self.branch2_dropdown = tk.OptionMenu(
                self.branch_window, self.selection2, *self.branch_list2
            )
            self.branch_btn = tk.Button(
                self.branch_window,
                text="Compare Branch",
                command=lambda: self.compare_branches(
                    branch1=self.selection1.get(), branch2=self.selection2.get()
                ),
            )
            self.branch1_dropdown.place(x=75, y=0, width=150, height=40)
            self.branch2_dropdown.place(x=75, y=50, width=150, height=40)
            self.branch_btn.place(x=75, y=100, width=150, height=30)
        else:
            self.project_warning()
