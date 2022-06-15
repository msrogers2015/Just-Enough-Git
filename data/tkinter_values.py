# Fonts
title = ("Arial", 16)
buttons = ("Arial", 14)
information = ("Arial", 12)

# Paths
project_path_string = ""
home_path = ""
project_title = ""

# App dimensions
width = 600
height = 550

# Educational prompts
init_prompt = """The 'git init' command creates an empty Git repository at \
the location specified. If the given folder already contains a .git file, \
then the folder is reinitialized rather than created (initialized). This \
should always be the first git command used when starting or continuing \
work on a project."""

clone_prompt = """This will retrive a github repo and install it locally on \
your machine at the specified path. The above code is what git
displays while retriving the repo. If the repo fails, there
will be an error message. The follow line of code was ran."""

name_prompt = """The line below changes the name attached to your commits. \
The name assoicated with this command is how you are represented when you \
push your commits to a repo."""

email_prompt = """The line below changes the email attached to your commits. \
The email assoicated with this command is how you are represented when you \
push your commits to a repo."""

status_prompt = """Look at the terminal for your output. This command give \
you a snapshot of your project, which files are ready for the commit and \
which ones still need to be added or worked on."""

add_file_prompt = """Files will be added to the staging area. These files are \
ready to be commited and pushed to the repo"""

remove_file_prompt = """Files will be removed from the staging are and will \
not be part of the commit and push to repo"""

commit_prompt = """Switch to the terminal to type your commit message. When \
you are finished, prees Ctrl+ o to save, enter to confirm and Ctrl+x to exit \
and save the commit"""

push_prompt = """Pushing your local repo means that all the changes you saved \
and commited will be put in the remote repo over on github. Go check out \
what changed!"""

pull_prompt = """"""

branch_prompt = """Check the terminal for a list of all branches for this \
project. The branch with a * by it is the current loaded branch."""

create_branch_prompt = """Creating a new branch makes a fork from the current \
project that you can work on freely. Test new features and work on bug fixes \
would benefits from creating a new branch"""


# Global Variables
name = ""
email = ""
