import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    sys.stdout.write("$ ") # maybe we are using this to write instead of print as that appends and extra newline
    sys.stdout.flush()

    list_of_commands = []
    command = input()

    if command not in list_of_commands:
        print(command + ": command not found")
        exit(1)

if __name__ == "__main__":
    main()
