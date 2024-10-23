RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[37m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RED = '\033[91m'
CYAN = '\033[96m'
ORANGE = "\033[38;5;208m"
GREEN = '\033[92m'

from time import sleep
import sys

def print_welcome_message():
    print(rf'''{CYAN}

    _         _          ____  _                   _                  
   / \  _   _| |_ ___   / ___|| |_ _ __ _   _  ___| |_ _   _ _ __ ___ 
  / _ \| | | | __/ _ \  \___ \| __| '__| | | |/ __| __| | | | '__/ _ \
 / ___ \ |_| | || (_) |  ___) | |_| |  | |_| | (__| |_| |_| | | |  __/
/_/   \_\__,_|\__\___/  |____/ \__|_|   \__,_|\___|\__|\__,_|_|  \___|
            {RESET}{WHITE}Flexible Python project structures for every need.
            {RESET}{CYAN}
        [*]__author__: @id0ubl3g
        [*]__version__: 1.0 
        [*]__usage__: {YELLOW}python3{RESET} main.py -n {CYAN}[project_name]{RESET}
''')

def print_create_root_directory(directory_name):
    print(f'\n{GREEN}[v]{RESET} Creating root directory at: {WHITE}{directory_name}{RESET}')

def print_directory_exists(directory_name):
    print(f'{CYAN}[i]{RESET} Directory already exists: {WHITE}{directory_name}{RESET}')

def print_create_subdirectory(subdirectory):
    print(f'\n{CYAN}[+]{RESET} Creating subdirectory: {WHITE}{subdirectory}{RESET}')

def print_create_environment(virtualenv_path):
    print(f'\n{GREEN}[v]{RESET} Virtual environment created at: {WHITE}{virtualenv_path}{RESET}')

def print_environment_exists(virtualenv_path):
    print(f'\n{ORANGE}[i]{RESET} Virtual environment already exists at: {WHITE}{virtualenv_path}{RESET}')

def print_environment_error(virtualenv_path):
    print(f'\n{RED}[x]{RESET} Failed to create virtual environment at: {WHITE}{virtualenv_path}{RESET}')

def print_interrupted_message():
    print(f'\n{ORANGE}[!]{RESET} Operation interrupted by user. Exiting gracefully...')

def print_structure_created(directory_name):
    print(f'\n{CYAN}[+]{RESET} Project structure created successfully at: {WHITE}{directory_name}{RESET}')

def print_structure_exists(directory_name):
    print(f'\n{ORANGE}[i]{RESET} Project structure already exists at: {WHITE}{directory_name}{RESET}')

def print_invalid_value(message):
    print(f'\n{ORANGE}[i]{RESET} Invalid value: {WHITE}{message}{RESET}')

def print_error_unexpected():
    print(f'\n{RED}[x]{RESET} An unexpected error occurred.')

def print_project_options():
    print(f'\n{CYAN}[i]{RESET}{BOLD} Select a project structure to set up:{RESET}\n')
    print(f'{CYAN}[1]{RESET} Scalabre Structure: Basic scalable structure{RESET}')
    print(f'{CYAN}[2]{RESET} API Clean Structure: Clean and modular API structure{RESET}')
    print(f'{CYAN}[3]{RESET} Site Structure: Structure for web applications{RESET}')
    
def print_create_file(file_name):
    print(f'\n{CYAN}[+]{RESET} Creating file: {WHITE}{file_name}{RESET}')

def print_license_options():
    print(f'\n{CYAN}[i]{RESET}{BOLD} Select a license for your project:{RESET}\n')
    print(f'{CYAN}[1]{RESET} MIT License{RESET}')
    print(f'{CYAN}[2]{RESET} GNU General Public License{RESET}')
    print(f'{CYAN}[3]{RESET} Apache License 2.0{RESET}')

def print_create_license(license_name):
    print(f'\n{GREEN}[v]{RESET} License created: {WHITE}{license_name}{RESET}')

def print_success_message(directory_name):
    activation_command = "source .venv/bin/activate"

    print(rf'''
        {GREEN}[v]{RESET} Your project is ready to use at: {WHITE}{directory_name}{RESET}
        {GREEN}[v]{RESET} Virtual environment setup complete
        {CYAN}[i]{RESET} Ready to code! Start by activating the environment with: 
            
            {WHITE}cd {directory_name}{RESET}
            {WHITE}{activation_command}{RESET}

        {CYAN}Good luck and happy coding!{RESET}
''')

def loading_animation():
    loading_symbols = ['|', '/', '-', '\\']
    for i in range(20):
        sys.stdout.write(f'\r\t{CYAN}Loading... {loading_symbols[i % len(loading_symbols)]}{RESET}')
        sys.stdout.flush()
        sleep(0.2)
        
    print(f'\r\t{CYAN}Loading complete!{RESET}')

def print_directory_removed(directory_path):
    print(f'\n{RED}[x]{RESET} Directory removed at: {WHITE}{directory_path}{RESET} due to interruption.')

def download_bar():
    progress = 0
    bar_length = 50
    print('\n')
    while progress <= 100:
        percent = progress
        filled_length = int(bar_length * (progress / 100))
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        print(f'\r\t{CYAN}Downloading... |{bar}| {percent:.2f}%{RESET}', end='')
        sys.stdout.flush()
        sleep(0.1)
        progress += 1

    print(f'\r\t{CYAN}Download complete! {RESET}')

def print_venv_not_installed():
    print(f'\n{ORANGE}[i]{RESET} The "venv" module is not installed. Would you like to install it? (y/n)')

def print_venv_information():

    install_venv = "sudo apt install python3.12-venv"

    print(f'\n{ORANGE}[i]{RESET} Please install it manually using the following command:')
    print(f'\n\t{install_venv}')
    print(f'\n{GREEN}[+]{RESET} For more information, visit: https://docs.python.org/3/library/venv.html')

def print_prompt_password_message():
    from src.utils.shared.shared import shared_get_current_directory
    current_directory = shared_get_current_directory()
    print(f'\n{ORANGE}[i]{RESET} Please enter your password to gain root access:')
    print(f'\n{GREEN}[i]{RESET} After logging in as root@{current_directory},')
    print(f'\n\t{ORANGE}press Ctrl+D{RESET} or type {ORANGE}exit{RESET} to continue.')
    print(f'\n{CYAN}[i]{RESET} If you are already logged in as root,{RESET}')
    print(f'\n\tjust {ORANGE}press Ctrl+D{RESET} to confirm and proceed with the process.{RESET}\n')

def print_already_logged_as_root():
    print(f'\n{GREEN}[+]{RESET} You are already logged in as root.')

def print_password_or_error():
    print(f'\n{RED}[x]{RESET} Incorrect password or an unexpected error occurred.')

def print_process_interrupted():
    print(f'\n{ORANGE}[i]{RESET} Process interrupted')

def print_library_installing(library):
    print(f"\n{CYAN}[+]{RESET} Installed {WHITE}{library}{RESET}.")

def print_libraries_installed_successfully():
    print(f"\n{GREEN}[✓]{RESET} All libraries installed successfully.")

def print_library_installation_error():
    print(f"\n{RED}[x]{RESET} An error occurred while installing libraries")

def print_requirements_saved():
    print(f"\n{CYAN}[+]{RESET} Saved installed libraries to {WHITE}requirements.txt{RESET}.")

def print_requirements_save_error():
    print(f"\n{RED}[x]{RESET} An error occurred while saving {WHITE}requirements.txt{RESET}.")
