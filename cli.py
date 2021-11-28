from colorama import Fore as cl


def confirm(default='y', action=''):
    if action != '':
        if default == 'y':
            cnf = input(f'{cl.BLUE}::{cl.RESET} Are you sure want to {action}? [Y/n] ').lower()
            if cnf == '':
                return True
        elif default == 'n':
            cnf = input(f'{cl.BLUE}::{cl.RESET} Are you sure want to {action}? [Y/n] ').lower()
            if cnf == '':
                return False
        else:
            print(f'Unmatched value of default: {default}.')

    else:
        if default == 'y':
            cnf = input(f'{cl.BLUE}::{cl.RESET} Are you sure want to continue? [Y/n] ').lower()
            if cnf == '':
                return True
        elif default == 'n':
            cnf = input(f'{cl.BLUE}::{cl.RESET} Are you sure want to continue? [Y/n] ').lower()
            if cnf == '':
                return False
        else:
            print(f'Unmatched value of default: {default}.')

    if cnf == 'n':
        return False
    elif cnf == 'y':
        return True

def input_prompt(message):
    PROMPT = input(f'{cl.BLUE}::{cl.RESET} {message} {cl.CYAN}${cl.RESET} ')
    return PROMPT
