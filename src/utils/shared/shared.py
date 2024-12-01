def shared_get_current_directory() -> str:
    import os
    return os.getcwd()

def shared_show_message_with_clear(msg_func: str = None, other_msg_func: str = None, delay: float = 0.5) -> None:
    from src.utils.system_utils import clear_screen
    from src.utils.style_outputs import print_welcome_message, print_interrupted_message
    from time import sleep
    import sys
    try:
        clear_screen()
        print_welcome_message()

        if msg_func:
            msg_func()

        if other_msg_func:
            other_msg_func()  

        sleep(delay)

    except KeyboardInterrupt:
        print_interrupted_message()
        sys.exit(1)
    
