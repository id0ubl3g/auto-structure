from src.utils.shared.shared import shared_get_current_directory, shared_show_message_with_clear
from src.utils.system_utils import execute_before, parse_arguments

from src.utils.style_outputs import (
    print_create_root_directory, print_directory_exists, print_project_options,
    print_invalid_value, print_create_subdirectory, print_create_file,
    print_requirements_saved, print_library_installing, print_libraries_installed_successfully,
    print_library_installation_error, print_venv_information, print_create_environment,
    print_interrupted_message, print_directory_removed, print_error_unexpected,
    loading_bar, print_success_message, print_exit_message
)

from docs.base_structures import Lightweight_API, Extended_API
from docs.write_gitignore import GIT_IGNORE

from config.colors_config import CYAN, RESET

from time import sleep
import subprocess
import tempfile
import shutil
import venv
import sys
import os

class CreateStructure:
    def __init__(self) -> None:
        self.root_directory: str = "projects"
        self.subdirectories: dict[str, list[str]] = {}
        self.directory_not_exists: bool = None
        self.init_files: list[str] = ['README.md', '.gitignore', 'run.py']
        self.libraries: list[str] = []

        self.short_time: float = 0.5
        self.medium_time: float = 1.0
        self.long_time: float = 2.0

        self.choice_structure: str = None

        self.new_directory_path: str = None
        self.project_name: str = None

        self.subsubdirectory_path: str = None
        self.subdirectory_path: str = None
    
    def concatenate_paths(self, project_name: str) -> str:
        current_directory = shared_get_current_directory()
        return os.path.join(current_directory, self.root_directory, project_name)

    def check_directory_exists(self, project_name: str) -> None:
        self.new_directory_path = self.concatenate_paths(project_name)
        self.directory_not_exists = not os.path.exists(self.new_directory_path)
    
    def remove_directory(self, directory: str) -> None:
        shutil.rmtree(directory)

    def create_root_directory(self) -> None:
        if self.directory_not_exists:
            os.makedirs(self.new_directory_path, exist_ok=True)
            print_create_root_directory(self.new_directory_path)
            sleep(self.medium_time)

            return
                    
        shared_show_message_with_clear(lambda: print_directory_exists(self.new_directory_path))
        sys.exit(0)

    def select_structure(self) -> None:
        while True:
            try:
                sleep(self.medium_time)
                shared_show_message_with_clear(print_project_options, delay=0.0)
                self.choice_structure = input(F'{CYAN}\n[$] {RESET}')
                sleep(self.long_time)

                if self.choice_structure.strip():
                    self.choice_structure = int(self.choice_structure)
                    
                    return
                
                else:
                    shared_show_message_with_clear(lambda: print_invalid_value(self.choice_structure))

            except ValueError:
                shared_show_message_with_clear(lambda: print_invalid_value(self.choice_structure))

    @execute_before(select_structure)
    def pull_structure(self) -> None:
        match self.choice_structure:
            case 1:
                self.subdirectories = Lightweight_API
                self.libraries = ['flask', 'flask-cors', 'flasgger', 'gunicorn']
                shared_show_message_with_clear()

            case 2:
                self.subdirectories = Extended_API
                self.libraries = ['flask', 'flask-cors', 'flasgger', 'gunicorn', 'psycopg2-binary', 'Flask-SQLAlchemy']
                shared_show_message_with_clear()

            case 0:
                shared_show_message_with_clear(print_exit_message)
                self.remove_directory(self.new_directory_path)
                sys.exit(0)
            
            case _:
                shared_show_message_with_clear(lambda: print_invalid_value(self.choice_structure))
                self.pull_structure()

    def create_subdirectories(self) -> None:
        for subdirectory, subsubdirs in self.subdirectories.items():
            sleep(self.short_time)
            self.subdirectory_path = os.path.join(self.new_directory_path, subdirectory)
            os.makedirs(self.subdirectory_path, exist_ok=True)
            print_create_subdirectory(subdirectory)
        
            for subsubdir in subsubdirs:
                sleep(self.short_time)
                self.subsubdirectory_path = os.path.join(self.subdirectory_path, subsubdir)
                os.makedirs(self.subsubdirectory_path, exist_ok=True)
                print_create_subdirectory(subsubdir)
        
    def create_files(self, project_name: str) -> None:
        for file in self.init_files:
            sleep(self.short_time)
            create_file = os.path.join(self.new_directory_path, file)
            
            print_create_file(file)

            if 'README.md' in create_file:
                with open(create_file, 'w') as file:
                    file.write(f'# {project_name}')

            elif '.gitignore' in create_file:
                with open(create_file, 'w') as file:
                    file.write(GIT_IGNORE)

            elif 'run.py' in create_file:
                with open(create_file, 'w') as file:
                    file.write('')

            else:
                with open(create_file, 'w') as file:
                    file.write('')
        
    def save_requirements(self) -> None:
        sleep(self.short_time)
        with open(os.path.join(self.new_directory_path, 'requirements.txt'), 'w') as file:
            subprocess.run([os.path.join(self.new_directory_path, '.venv', 'bin', 'pip'), 'freeze'], stdout=file, check=True)
            
        print_requirements_saved()
        sleep(self.medium_time)

    def install_libraries(self) -> None:
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

    def create_virtualenv(self) -> None:
        temp_dir = tempfile.mkdtemp()
        virtualenv_path = os.path.join(self.new_directory_path, '.venv')

        try:
            subprocess.run(["python3.12", "-m", "venv", os.path.join(temp_dir, "test_env")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        except subprocess.CalledProcessError:
            sleep(self.medium_time)
            shared_show_message_with_clear(print_venv_information)
            sys.exit(0)

        finally:    
            venv.create(virtualenv_path, with_pip=True)
            shared_show_message_with_clear(lambda: print_create_environment(virtualenv_path))
            self.remove_directory(temp_dir)
            self.install_libraries()

    def execute(self) -> None:
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
            loading_bar()

        except KeyboardInterrupt:
            shared_show_message_with_clear(print_interrupted_message)
            sys.exit(1)

        except Exception:
            shared_show_message_with_clear(print_error_unexpected)
            sys.exit(1)

        shared_show_message_with_clear(lambda: print_success_message(self.new_directory_path))