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
            if self.directory_not_exists:
                os.makedirs(self.new_directory_path, exist_ok=True)
                print('Created directory')
                
                return
            
            print('directory already exists')
            sys.exit(1)
            
        except KeyboardInterrupt:
            self.remove_directory()
            sys.exit(1)

        except Exception:
            pass
