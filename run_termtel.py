import subprocess
import os

# Path to your Termtel project folder
project_dir = r"C:\Users\User\termtelent"

# Path to the Python executable inside your venv
venv_python = os.path.join(project_dir, ".venv", "Scripts", "python.exe")

# The command to launch the program
launch_command = ["-m", "launcher.launch"]

# Change working directory to the project folder
os.chdir(project_dir)

# Run the command using the venv's Python
subprocess.run([venv_python] + launch_command)
