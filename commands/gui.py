import tkinter as tk
from commands import setup, stage, branch
from data import tkinter_values as tv


class GUI(tk.Frame):
    def __init__(self, root=None):
        # Setting up tkinter root window for useage within this class
        super().__init__(root)
        self.root = root
        # Create main application window
        self.window()
        # Setting up commands related to stup-up features of git
        self.setup_commands = setup.Setup(
            root=self.root,
            project_label=self.project_label,
            project_path_label=self.project_path_label,
            status_information=self.status_information,
            terminal_command=self.terminal_command,
        )
        # Setting up commands related to staging features of git
        self.stage_commands = stage.Stage(
            root=self.root,
            project_label=self.project_label,
            project_path_label=self.project_path_label,
            status_information=self.status_information,
            terminal_command=self.terminal_command,
        )
        # Setting up commands related to branch features of git
        self.branch_commands = branch.Branch(
            root=self.root,
            project_label=self.project_label,
            project_path_label=self.project_path_label,
            status_information=self.status_information,
            terminal_command=self.terminal_command,
        )
        # Create application menu
        self.menu()
        # Connecting application menu to the app frame
        root.config(menu=self.menubar)

    def menu(self):
        '''Creation of command options to be attached to the main
        window of the application'''
        # Creation of window menu options
        self.menubar = tk.Menu(self.root)
        self.setupmenu = tk.Menu(self.menubar, tearoff=0)
        self.stagemenu = tk.Menu(self.menubar, tearoff=0)
        self.commitmenu = tk.Menu(self.menubar, tearoff=0)
        self.branchmenu = tk.Menu(self.menubar, tearoff=0)
        self.trackmenu = tk.Menu(self.menubar, tearoff=0)
        # Setup Menu Options
        self.setupmenu.add_command(
            label="Init Project   (Ctrl+O)",
            command=self.setup_commands.init_repo)
        self.setupmenu.add_command(
            label="Clone Project   (Ctrl+Shift+O)",
            command=self.setup_commands.clone_repo)
        self.setupmenu.add_separator()
        self.setupmenu.add_command(
            label="Change Name",
            command=self.setup_commands.update_name)
        self.setupmenu.add_command(
            label="Change Email",
            command=self.setup_commands.update_email)
        self.setupmenu.add_separator()
        self.setupmenu.add_command(
            label="Exit",
            command=self.root.quit)
        # Stage Menu Options
        self.stagemenu.add_command(
            label="Status",
            command=self.stage_commands.status)
        self.stagemenu.add_separator()
        self.stagemenu.add_command(
            label="Add File(s)",
            command=self.stage_commands.add_files)
        self.stagemenu.add_command(
            label="Remove File(s)",
            command=self.stage_commands.remove_files)
        self.stagemenu.add_separator()
        self.stagemenu.add_command(
            label="Unstaged Changes",
            command=self.stage_commands.unstaged_files)
        self.stagemenu.add_command(
            label="Staged Changes",
            command=self.stage_commands.staged_files)
        self.stagemenu.add_command(
            label="Open Changes Output   (Ctrl+c)",
            command=self.stage_commands.output_files,)
        # Commit Menu Options
        self.commitmenu.add_command(
            label="Full Commit",
            command=self.stage_commands.commit)
        self.commitmenu.add_command(
            label="Quick Commit",
            command=self.stage_commands.quick_commit)
        self.commitmenu.add_separator()
        self.commitmenu.add_command(
            label="Push   (Ctrl+P)",
            command=self.stage_commands.push)
        self.commitmenu.add_command(
            label="Pull   (Ctrl+Shift+P)",
            command=self.stage_commands.pull)
        # Branch Menu Options
        self.branchmenu.add_command(
            label="List Branches",
            command=self.branch_commands.branches)
        self.branchmenu.add_command(
            label="Switch Branch",
            command=self.branch_commands.switch_branch)
        self.branchmenu.add_command(
            label="New Branch",
            command=self.branch_commands.new_branch)
        self.branchmenu.add_separator()
        self.branchmenu.add_command(
            label="Merge Branches   (Ctrl+M)",
            command=self.branch_commands.merge_branch)
        self.branchmenu.add_separator()
        self.branchmenu.add_command(
            label="Changes on Current Branch",
            command=self.branch_commands.branch_commits,)
        self.branchmenu.add_command(
            label="Compare Branch Log",
            command=self.branch_commands.branch_compare)
        self.branchmenu.add_command(label="Compare Branch Changes")
        # Tracking Menu Options
        self.trackmenu.add_command(label="Track File")
        self.trackmenu.add_command(label="Remove File(s)")
        self.trackmenu.add_command(label="Move File(s)")
        self.trackmenu.add_separator()
        self.trackmenu.add_command(label="Show Tracking Log")
        # Adding Sub menus to main menu bar
        self.menubar.add_cascade(label="Setup", menu=self.setupmenu)
        self.menubar.add_cascade(label="Stage", menu=self.stagemenu)
        self.menubar.add_cascade(label="Commit", menu=self.commitmenu)
        self.menubar.add_cascade(label="Branch", menu=self.branchmenu)
        self.menubar.add_cascade(label="Tracking", menu=self.trackmenu)

    def window(self):
        '''Creation of the main content of the application'''
        # Labels
        self.project_label = tk.Label(
            self.root,
            text="No Project Currently Loaded",
            font=tv.title,  # Project name
            anchor="center",
        )
        self.project_path_label = tk.Label(
            self.root,
            text=tv.project_path_string,
            font=tv.information)
        self.status_label = tk.Label(
            self.root,
            text="Information output",
            font=tv.title,
            anchor="n")
        self.status_information = tk.Label(
            self.root,
            text="Welcome to GitPY!",
            font=tv.information,
            wraplength=250,
            anchor="n",)
        self.terminal_command_label = tk.Label(
            self.root,
            text="Terminal Command",
            font=tv.title,
            anchor="center",)
        self.terminal_command = tk.Label(
            self.root,
            text="",
            font=tv.information,
            wraplength=250,
            anchor="n",)

        # Placement
        self.project_label.place(
            x=25, y=10,
            width=550, height=30)
        self.project_path_label.place(
            x=25, y=50,
            width=550, height=25)
        self.status_label.place(
            x=300, y=100,
            width=275, height=25)
        self.status_information.place(
            x=300, y=130,
            width=275, height=345)
        self.terminal_command_label.place(
            x=25, y=480,
            width=550, height=25)
        self.terminal_command.place(
            x=25, y=510,
            width=550, height=25)
