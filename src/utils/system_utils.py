from src.utils.style_outputs import print_welcome_message

from docs.usage_auto_structure import usage_auto_structure


from typing import Callable
import argparse
import sys
import os

def clear_screen() -> None:
    os.system('clear')
    
def parse_arguments() -> argparse.Namespace:
    if '--help' in sys.argv or '-h' in sys.argv:
        clear_screen()
        print(usage_auto_structure)
        sys.exit(0)

    parser = argparse.ArgumentParser(description='Create a project structure.', usage='%(prog)s -n [project_name]')
    parser.add_argument('-n', '--project_name', type=str, help='The name of the project directory')

    try:
        return parser.parse_args()
    
    except SystemExit:
        clear_screen()
        print_welcome_message()
        sys.exit(1)

def execute_before(method_to_execute: Callable[[], None]) -> Callable[[], None]:
    def decorator(func: Callable[[], None]) -> Callable[[], None]:
        def wrapper(self, *args, **kwargs) -> None:
            method_to_execute(self)
            return func(self, *args, **kwargs)
        return wrapper
    return decorator