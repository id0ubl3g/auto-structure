from src.utils.style_outputs import *
from src.utils.system_utils import *
from config.structures import *
from config.licenses import *

from time import sleep
import shutil
import sys
import os

class CreateStructure:
    def __init__(self):
        self.root_directory: str = "projects"
        self.subdirectories: dict = {}
        self.directory_not_exists: bool = None
        self.init_files: list = ['README.md', '.gitignore', '.env', '.env.example', 'LICENSE']

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
            sys.exit(1)
            
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

            except Exception:
                        sleep(0.5)
                        clear_screen()
                        print_welcome_message()
                        print_invalid_value(choice_structure)

    def pull_structure(self):
        try:
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

        except Exception:
                    sleep(0.5)
                    clear_screen()
                    print_welcome_message()
                    print_invalid_value(choice_structure)

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
        sleep(0.5)
        src_schemas_path = os.path.join(self.new_directory_path, 'src', 'schemas')
        app_schemas_path = os.path.join(self.new_directory_path, 'app', 'schemas')

        if os.path.exists(src_schemas_path):
            gitkeep_path = os.path.join(src_schemas_path, '.gitkeep')
            with open(gitkeep_path, 'w') as file:
                file.write('')

            print_create_file('.gitkeep')

        if os.path.exists(app_schemas_path):
            gitkeep_path = os.path.join(app_schemas_path, '.gitkeep')
            with open(gitkeep_path, 'w') as file:
                file.write('')

            print_create_file('.gitkeep')

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

            elif 'LICENSE' in create_file:
                while True:
                    sleep(0.5)
                    clear_screen()
                    print_welcome_message()
                    print_license_options()

                    try:
                        choice_license = int(input(F'{CYAN}\n[$] {RESET}'))
                        sleep(1)

                        match choice_license:
                            case 1:
                                with open(create_file, 'w') as file:
                                    file.write(MIT)
                                print_create_license('MIT')
                                break

                            case 2:
                                with open(create_file, 'w') as file:
                                    file.write(GNU)
                                print_create_license('GNU')
                                break

                            case 3:
                                with open(create_file, 'w') as file:
                                    file.write(APACHE)
                                print_create_license('APACHE')
                                break

                            case _:
                                clear_screen()
                                print_welcome_message()
                                print_invalid_value(choice_license)
                                sleep(0.5)

                    except ValueError:
                        clear_screen()
                        print_welcome_message()
                        print_invalid_value(choice_license)
                        sleep(0.5)

            else:
                with open(create_file, 'w') as file:
                    file.write('')