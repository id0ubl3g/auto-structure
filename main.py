from config.path_config import *
add_project_root_to_path()

from src.modules.create_structure import CreateStructure

if __name__ == '__main__':
    CreateStructure().execute()