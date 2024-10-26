from src.utils.shared.shared import shared_show_message_with_clear
from src.utils.style_outputs import *

import subprocess
import sys

def check_if_root():
    current_user = subprocess.run(["whoami"], text=True, capture_output=True, check=True)

    return current_user.stdout.strip() == 'root'

def run_sudo():
    try:
        if check_if_root():
            shared_show_message_with_clear(print_already_logged_as_root)

            return
        
        shared_show_message_with_clear(print_prompt_password_message)

        subprocess.run(["sudo","su"], check=True)

        return

    except subprocess.CalledProcessError as e:
        print_prompt_password_message()

        if e.returncode == 130:
            print_process_interrupted()
            sys.exit(0)
        
        else:
            print_password_or_error()
            sys.exit(1)