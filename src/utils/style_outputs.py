from config.collors_config import WHITE, YELLOW, ORANGE, RED, GREEN, CYAN, RESET, BOLD

from time import sleep
import sys

def print_welcome_message() -> None:
    print(rf'''{CYAN}   ___       __           ______               __              
  / _ |__ __/ /____      / __/ /_______ ______/ /___ _________ 
 / __ / // / __/ _ \    _\ \/ __/ __/ // / __/ __/ // / __/ -_)
/_/ |_\_,_/\__/\___/   /___/\__/_/  \_,_/\__/\__/\_,_/_/  \__/ 

        {RESET}{WHITE}Flexible {RED}Flask{WHITE} API structures for any project.
            {RESET}{CYAN}
    [*]__author__: {RESET}George Victor | @id0ubl3g{CYAN}
    [*]__github__: {RESET}github.com/id0ubl3g/auto-structure{CYAN}
    [*]__usage__: {YELLOW}python3{RESET} run.py --project_name {CYAN}<project name>{RESET}
''')
    
def print_create_root_directory(directory_name: str) -> None:
    print(f'\n{GREEN}[v]{RESET} Creating root directory at: {WHITE}{directory_name}{RESET}')

def print_directory_exists(directory_name: str) -> None:
    print(f'{CYAN}[i]{RESET} Directory already exists: {WHITE}{directory_name}{RESET}')

def print_create_subdirectory(subdirectory: str) -> None:
    print(f'\n{CYAN}[+]{RESET} Creating subdirectory: {WHITE}{subdirectory}{RESET}')

def print_create_environment(virtualenv_path: str) -> None:
    print(f'\n{GREEN}[v]{RESET} Virtual environment created at: {WHITE}{virtualenv_path}{RESET}')

def print_environment_exists(virtualenv_path: str) -> None:
    print(f'\n{ORANGE}[i]{RESET} Virtual environment already exists at: {WHITE}{virtualenv_path}{RESET}')

def print_environment_error(virtualenv_path: str) -> None:
    print(f'\n{RED}[x]{RESET} Failed to create virtual environment at: {WHITE}{virtualenv_path}{RESET}')

def print_interrupted_message() -> None:
    print(f'\n{ORANGE}[!]{RESET} Operation interrupted by user. Exiting gracefully...')

def print_structure_created(directory_name: str) -> None:
    print(f'\n{CYAN}[+]{RESET} Project structure created successfully at: {WHITE}{directory_name}{RESET}')

def print_structure_exists(directory_name: str) -> None:
    print(f'\n{ORANGE}[i]{RESET} Project structure already exists at: {WHITE}{directory_name}{RESET}')

def print_invalid_value(message: str) -> None:
    print(f'\n{ORANGE}[i]{RESET} Invalid value: {WHITE}{message}{RESET}')

def print_error_unexpected() -> None:
    print(f'\n{RED}[x]{RESET} An unexpected error occurred.')

def print_project_options() -> None:
    print(f'\n{CYAN}[i]{RESET}{BOLD} Select a project structure to set up:{RESET}\n')
    print(f'{CYAN}[1]{RESET} Lightweight API: This structure is suitable for lightweight APIs, ideal for microservices')
    print(f'{CYAN}[2]{RESET} Extended API: This structure is designed for more complex APIs with PostgreSQL database integration')
    
def print_create_file(file_name: str) -> None:
    print(f'\n{CYAN}[+]{RESET} Creating file: {WHITE}{file_name}{RESET}')

def print_success_message(directory_name: str) -> None:
    activation_command = "source .venv/bin/activate"

    print(f'''
        {GREEN}[v]{RESET} Your project is ready to use and Virtual environment setup complete
        {CYAN}[i]{RESET} Ready to code! Start by activating the environment with: 
            
            {WHITE}cd {directory_name}{RESET}
            {WHITE}{activation_command}{RESET}

        {CYAN}Good luck and happy coding!{RESET}
''')

def loading_bar() -> None:
    total_steps = 40
    for i in range(total_steps + 1):
        percentage = (i / total_steps) * 100
        bar = f"[{'#' * i}{'.' * (total_steps - i)}]"
        sys.stdout.write(f'\r\tLoading {bar} {percentage:.0f}%')
        sys.stdout.flush()
        sleep(0.15)
    print(f'\r\tFinish!')
    sleep(1.5)

def print_directory_removed(directory_path: str) -> None:
    print(f'\n{RED}[x]{RESET} Directory removed at: {WHITE}{directory_path}{RESET} due to interruption')

def print_venv_information() -> None:

    install_venv = "sudo apt install python3.12-venv"

    print(f'\n{RED}[!]{RESET} Virtual environment creation failed: "venv" module is not installed.\n')
    print(f'{ORANGE}[i]{RESET} To install it, run the following command:')
    print(f'\n\t{install_venv}\n')
    print(f'{GREEN}[+]{RESET} For more information, visit: https://docs.python.org/3/library/venv.html\n')

def print_library_installing(library: str) -> None:
    print(f"\n{CYAN}[+]{RESET} Installed {WHITE}{library}{RESET}.")

def print_libraries_installed_successfully() -> None:
    print(f"\n{GREEN}[✓]{RESET} All libraries installed successfully.")

def print_library_installation_error() -> None:
    print(f"\n{RED}[x]{RESET} An error occurred while installing libraries")

def print_requirements_saved() -> None:
    print(f"\n{CYAN}[+]{RESET} Saved installed libraries to {WHITE}requirements.txt{RESET}.")

