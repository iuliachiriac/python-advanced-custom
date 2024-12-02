# Constants (variables that are not supposed to change) should be uppercase
# Usually defined as global variables at the beginning of the module
FILE_PATH = "results.txt"  # read filename from settings file


def do_something():
    pass


def write_results():
    # Constants can be used inside functions in READ operations
    # (because global variables are visible inside functions)
    # Changing global variables inside functions is not recommended
    with open(FILE_PATH):
        do_something()


def write_results_destination(filename):
    # This function is more general than `write_results`, because it can
    # customize its destination
    with open(filename):
        do_something()


# Global variables can also be sent as arguments
write_results_destination(FILE_PATH)
