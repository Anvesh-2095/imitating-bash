import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    while 1:
        sys.stdout.write("$ ")  # maybe we are using this to write instead of print as that appends and extra newline
        sys.stdout.flush()

        list_of_commands = ['exit', 'echo']
        statement = input()

        command = statement.split()[0]
        if command not in list_of_commands:
            print(command + ": command not found")
            continue
        if command == 'exit':
            break
        if command == 'echo':
            print(''.join(statement.split()[1:]))
            continue

if __name__ == "__main__":
    main()
