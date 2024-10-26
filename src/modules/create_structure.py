from src.utils.shared.shared import *
from src.utils.style_outputs import *
from src.utils.system_utils import *
from src.utils.sudo_auth import *
from config.structures import *
from config.gitignore import *

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
        self.libraries: list = []
        self.short_time =  0.5
        self.medium_time = 1
        self.long_time = 2
    
    def concatenate_paths(self, project_name):
        current_directory = shared_get_current_directory()
        return os.path.join(current_directory, self.root_directory, project_name)

    def check_directory_exists(self, project_name):
        self.new_directory_path = self.concatenate_paths(project_name)
        self.directory_not_exists = not os.path.exists(self.new_directory_path)
    
    def remove_directory(self, directory):
        shutil.rmtree(directory)

    def create_root_directory(self):
        if self.directory_not_exists:
            os.makedirs(self.new_directory_path, exist_ok=True)
            print_create_root_directory(self.new_directory_path)
            sleep(self.medium_time)
            
            return
        
        shared_show_message_with_clear(lambda: print_directory_exists(self.new_directory_path))
        sys.exit(0)

    def choice_structure(self):
        while True:
            try:
                sleep(self.medium_time)
                shared_show_message_with_clear(print_project_options, delay=0)
                choice_structure = input(F'{CYAN}\n[$] {RESET}')
                sleep(self.long_time)

                if choice_structure.strip():
                    choice_structure = int(choice_structure)
                    
                    return choice_structure
                
                else:
                    shared_show_message_with_clear(lambda: print_invalid_value(choice_structure))

            except ValueError:
                shared_show_message_with_clear(lambda: print_invalid_value(choice_structure))

    def choice_library(self):
        while True:
            try:
                sleep(self.medium_time)
                shared_show_message_with_clear(print_library_options, delay=0)
                choice_library = input(F'{CYAN}\n[$] {RESET}')
                sleep(self.long_time)

                if choice_library.strip():
                    choice_library = int(choice_library)
                    
                    return choice_library
                
                else:
                    shared_show_message_with_clear(lambda: print_invalid_value(choice_library))
                    

            except ValueError:
                shared_show_message_with_clear(lambda: print_invalid_value(choice_library))

    def pull_structure(self):
        choice_structure = self.choice_structure()

        match choice_structure:
            case 1:
                self.subdirectories = API
                while True:
                    shared_show_message_with_clear()
                    choice_library = self.choice_library()
                    match choice_library:
                        case 1:
                            self.libraries = ['flask', 'flask-cors', 'flasgger']
                            shared_show_message_with_clear()
                            
                            return
                        
                        case 2:
                            self.libraries = ['fastapi', 'uvicorn']
                            shared_show_message_with_clear()
                            
                            return
                        
                        case _:
                            print_invalid_value(choice_library)
                            
            case 2:
                self.subdirectories = FLASK
                self.libraries = ['flask', 'flask-cors', 'flasgger']
                shared_show_message_with_clear()

            case 3:
                self.subdirectories = FASTAPI
                self.libraries = ['fastapi', 'uvicorn']
                shared_show_message_with_clear()
            
            case _:
                shared_show_message_with_clear(lambda: print_invalid_value(choice_structure))
                self.pull_structure()

    def create_subdirectories(self):
        for subdirectory, subsubdirs in self.subdirectories.items():
            sleep(self.short_time)
            subdirectory_path = os.path.join(self.new_directory_path, subdirectory)
            os.makedirs(subdirectory_path, exist_ok=True)
            print_create_subdirectory(subdirectory)
        
            for subsubdir in subsubdirs:
                sleep(self.short_time)
                subsubdirectory_path = os.path.join(subdirectory_path, subsubdir)
                os.makedirs(subsubdirectory_path, exist_ok=True)
                print_create_subdirectory(subsubdir)
        
    def create_files(self, project_name):
        for file in self.init_files:
            sleep(self.short_time)
            create_file = os.path.join(self.new_directory_path, file)
            
            print_create_file(file)

            if 'README.md' in create_file:
                with open(create_file, 'w') as file:
                    file.write(project_name)

            elif '.gitignore' in create_file:
                with open(create_file, 'w') as file:
                    file.write(GIT_IGNORE)

            else:
                with open(create_file, 'w') as file:
                    file.write('')

    def save_requirements(self):
        sleep(self.short_time)
        with open(os.path.join(self.new_directory_path, 'requirements.txt'), 'w') as file:
            subprocess.run([os.path.join(self.new_directory_path, '.venv', 'bin', 'pip'), 'freeze'], stdout=file, check=True)
            
        print_requirements_saved()
        sleep(self.medium_time)

    def install_libraries(self):
        try:
            for library in self.libraries:
                sleep(self.short_time)
                
                subprocess.run([os.path.join(self.new_directory_path, '.venv', 'bin', 'pip'), 'install', library], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                print_library_installing(library)

            self.save_requirements()
            print_libraries_installed_successfully()
            sleep(self.long_time)

        except subprocess.CalledProcessError:
            shared_show_message_with_clear(print_library_installation_error)
            sys.exit(1)

    def create_virtualenv(self):
        temp_dir = tempfile.mkdtemp()
        virtualenv_path = os.path.join(self.new_directory_path, '.venv')

        try:
            subprocess.run(["python3.12", "-m", "venv", os.path.join(temp_dir, "test_env")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        except subprocess.CalledProcessError:
            while True:
                sleep(self.medium_time)
                shared_show_message_with_clear(print_venv_not_installed, delay=0)
                
                try:
                    choice_install = str(input(f'{CYAN}\n[$] {RESET}')).lower()
                
                except KeyboardInterrupt:
                    shared_show_message_with_clear(print_interrupted_message)
                    sys.exit(1)

                sleep(self.long_time)

                if choice_install == 'y':
                    run_sudo()
                    shared_show_message_with_clear()

                    signal.signal(signal.SIGINT, signal.SIG_IGN)
                    disable_input()

                    loading_thread = threading.Thread(target=download_bar)
                    loading_thread.start()
                    
                    subprocess.run(["sudo", "apt", "install", "python3.12-venv", "-y"], check=True, tdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)              

                    loading_thread.join()

                    signal.signal(signal.SIGINT, signal.default_int_handler)
                    enable_input()

                    break

                elif choice_install == 'n':
                    shared_show_message_with_clear(print_venv_information)
                    sys.exit(0)

                else:
                    shared_show_message_with_clear(lambda: print_invalid_value(choice_install))

        finally:    
            venv.create(virtualenv_path, with_pip=True)
            shared_show_message_with_clear(lambda: print_create_environment(virtualenv_path))
            self.remove_directory(temp_dir)
            self.install_libraries()

    def execute(self):
        args = parse_arguments()
        if not args.project_name:
            shared_show_message_with_clear()
            sys.exit(0)

        self.project_name = args.project_name
        shared_show_message_with_clear()

        try:
            self.check_directory_exists(self.project_name)
            self.create_root_directory()
            self.pull_structure()
            self.create_subdirectories()
            self.create_files(self.project_name)
        
        except KeyboardInterrupt:
            shared_show_message_with_clear(print_interrupted_message, lambda: print_directory_removed(self.new_directory_path))
            self.remove_directory(self.new_directory_path)
            sys.exit(1)

        except Exception:
            shared_show_message_with_clear(print_error_unexpected, lambda: print_directory_removed(self.new_directory_path))
            self.remove_directory(self.new_directory_path)
            sys.exit(1)
        
        try:
            self.create_virtualenv()
            shared_show_message_with_clear()
            loading_animation()
        

        except KeyboardInterrupt:
            shared_show_message_with_clear(print_interrupted_message)
            sys.exit(1)

        except Exception:
            shared_show_message_with_clear(print_error_unexpected)
            sys.exit(1)

        shared_show_message_with_clear(lambda: print_success_message(self.new_directory_path))