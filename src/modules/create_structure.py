from src.utils.style_outputs import *
from src.utils.system_utils import *
from src.utils.sudo_auth import *
from config.structures import *

from time import sleep
import subprocess
import threading
import tempfile
import shutil
import signal
import venv
import sys
import os

class CreateStructure:
    def __init__(self):
        self.root_directory: str = "projects"
        self.subdirectories: dict = {}
        self.directory_not_exists: bool = None
        self.init_files: list = ['README.md', '.gitignore', '.env', '.env.example']

    def get_current_directory(self):
        return os.getcwd()
    
    def concatenate_paths(self, project_name):
        current_directory = self.get_current_directory()
        return os.path.join(current_directory, self.root_directory, project_name)

    def check_directory_exists(self, project_name):
        self.new_directory_path = self.concatenate_paths(project_name)
        self.directory_not_exists = not os.path.exists(self.new_directory_path)
    
    def remove_directory(self):
        shutil.rmtree(self.new_directory_path)

    def create_root_directory(self):
        try:
            sleep(2)
            if self.directory_not_exists:
                os.makedirs(self.new_directory_path, exist_ok=True)
                print_create_root_directory(self.new_directory_path)
                
                return
            
            print_directory_exists(self.new_directory_path)
            sys.exit(0)
            
        except KeyboardInterrupt:
            sleep(0.5)
            print_welcome_message()
            print_interrupted_message()
            self.remove_directory()
            print_directory_removed(self.new_directory_path)
            sys.exit(1)

        except Exception:
            sleep(0.5)
            print_welcome_message()
            print_error_unexpected()

    def choice_structure(self):
        while True:
            try:
                sleep(2)
                print_project_options()
                choice_structure = input(F'{CYAN}\n[$] {RESET}')
                sleep(1)

                if choice_structure.strip():
                    choice_structure = int(choice_structure)
                    
                    return choice_structure
                
                else:
                    sleep(0.5)
                    clear_screen()
                    print_welcome_message()
                    print_invalid_value(choice_structure)

            except ValueError:
                        sleep(0.5)
                        clear_screen()
                        print_welcome_message()
                        print_invalid_value(choice_structure)

    def pull_structure(self):
        sleep(0.5)
        choice_structure = self.choice_structure()
        match choice_structure:
            case 1:
                sleep(2)
                self.subdirectories = SCALABLE_STRUCTURE
                clear_screen()
                print_welcome_message()

            case 2:
                sleep(2)
                self.subdirectories = API_CLEAN_STRUCTURE
                clear_screen()
                print_welcome_message()

            case 3:
                sleep(2)
                self.subdirectories = SITE_STRUCTURE
                clear_screen()
                print_welcome_message()
            
            case _:
                sleep(0.5)
                clear_screen()
                print_welcome_message()
                print_invalid_value(choice_structure)
                self.pull_structure()

    def create_subdirectories(self):
        for subdirectory, subsubdirs in self.subdirectories.items():
            sleep(0.5)
            subdirectory_path = os.path.join(self.new_directory_path, subdirectory)
            os.makedirs(subdirectory_path, exist_ok=True)
            print_create_subdirectory(subdirectory)
        
            for subsubdir in subsubdirs:
                sleep(0.5)
                subsubdirectory_path = os.path.join(subdirectory_path, subsubdir)
                os.makedirs(subsubdirectory_path, exist_ok=True)
                print_create_subdirectory(subsubdir)
        
    def create_files(self, project_name):
        for file in self.init_files:
            sleep(0.3)
            create_file = os.path.join(self.new_directory_path, file)
            
            print_create_file(file)

            if 'README.md' in create_file:
                with open(create_file, 'w') as file:
                    file.write(project_name)

            elif '.gitignore' in create_file:
                with open(create_file, 'w') as file:
                    file.write('__pycache__/\n\n.venv/\n.env\nschemas/*')

            else:
                with open(create_file, 'w') as file:
                    file.write('')

    def save_requirements(self):
        try:
            with open(os.path.join(self.new_directory_path, 'requirements.txt'), 'w') as file:
                subprocess.run(
                    [os.path.join(self.new_directory_path, '.venv', 'bin', 'pip'), 'freeze'],
                    stdout=file, check=True)
                
            print_requirements_saved()
            sleep(1)

        except subprocess.CalledProcessError:
            print_requirements_save_error()
            sys.exit(1)

    def install_libraries(self):
        try:
            libraries = ["requests", "flask", "flask-cors", "flasgger"]

            for library in libraries:
                subprocess.run([os.path.join(self.new_directory_path, '.venv', 'bin', 'pip'), 'install', library], 
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                print_library_installing(library)
                sleep(1)

            self.save_requirements()
            print_libraries_installed_successfully()
            sleep(2)

        except subprocess.CalledProcessError:
            print_library_installation_error()
            sys.exit(1)

    def create_virtualenv(self):
        temp_dir = tempfile.mkdtemp()
        virtualenv_path = os.path.join(self.new_directory_path, '.venv')

        try:
            subprocess.run(["python3.12", "-m", "venv", os.path.join(temp_dir, "test_env")], check=True)

        except subprocess.CalledProcessError:
            clear_screen()
            print_welcome_message()

            while True: 
                sleep(0.5)
                print_venv_not_installed()
                choice_install = str(input(f'{CYAN}\n[$] {RESET}')).lower()
                sleep(1)

                if choice_install == 'y':
                    run_sudo()
                    sleep(0.5)
                    clear_screen()
                    print_welcome_message()

                    signal.signal(signal.SIGINT, signal.SIG_IGN)
                    disable_input()

                    loading_thread = threading.Thread(target=download_bar)
                    loading_thread.start()

                    subprocess.run(["sudo", "apt", "install", "python3.12-venv", "-y"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)              

                    loading_thread.join()

                    signal.signal(signal.SIGINT, signal.default_int_handler)
                    enable_input()

                    break

                elif choice_install == 'n':
                    sleep(0.5)
                    clear_screen()
                    print_welcome_message()
                    print_venv_information()
                    sys.exit(0)

                else:
                    sleep(0.5)
                    clear_screen()
                    print_welcome_message()
                    print_invalid_value(choice_install)
        finally:    
            venv.create(virtualenv_path, with_pip=True)
            clear_screen()
            print_welcome_message()
            print_create_environment(virtualenv_path)
            shutil.rmtree(temp_dir)
            sleep(2)

            self.install_libraries()

    def execute(self):
        try:
            args = parse_arguments()
            if not args.project_name:
                clear_screen()
                print_welcome_message()
                sys.exit(0)

            self.project_name = args.project_name
            clear_screen()
            print_welcome_message()

            self.check_directory_exists(self.project_name)
            self.create_root_directory()
            self.pull_structure()
            self.create_subdirectories()
            self.create_files(self.project_name)
            self.create_virtualenv()

            clear_screen()
            print_welcome_message()
            loading_animation()

            clear_screen()
            print_welcome_message()
            print_success_message(self.new_directory_path)
        
        except KeyboardInterrupt:
            sleep(0.5)
            clear_screen()
            print_welcome_message()
            print_interrupted_message()
            
            if self.new_directory_path:
                self.remove_directory()
                print_directory_removed(self.new_directory_path)

            sys.exit(1)

        except Exception:
            sys.exit(1)