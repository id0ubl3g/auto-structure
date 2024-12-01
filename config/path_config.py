import sys
import os

def add_project_root_to_path() -> None:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
