from solver_code import entropy, all_entropy,first_guesses
from base_game_code import colorize
class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\u001b[37m'
    YELLOW = '\u001b[33m'
    GREY = '\u001b[30;1m'
    TEST = '\u001b[37m\033[1m'
print (bcolors.GREY + bcolors.BOLD + 'hello' + bcolors.ENDC)
print (bcolors.GREY + 'hello')
