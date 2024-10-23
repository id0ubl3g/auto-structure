from src.utils.system_utils import *
from src.utils.style_outputs import *

from time import sleep
import subprocess
import sys

def check_if_root():
    current_user = subprocess.run(
        ["whoami"],
        text=True,
        capture_output=True,
        check=True
    )

    return current_user.stdout.strip() == 'root'

def run_sudo():
    try:
        if check_if_root():
            sleep(2)
            clear_screen()
            print_welcome_message()
            print_already_logged_as_root()
            sleep(2)

            return
        
        sleep(2)
        clear_screen()
        print_welcome_message()
        print_prompt_password_message()
        sleep(2)

        subprocess.run(["sudo","su"], check=True)

        return

    except subprocess.CalledProcessError as e:
        clear_screen()
        print_welcome_message()

        if e.returncode == 130:
            print_process_interrupted()
            sys.exit(0)
        
        else:
            print_password_or_error()
            sys.exit(1)