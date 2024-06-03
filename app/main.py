import sys
import os
import os.path
from os.path import isfile, isdir, join

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    while 1:
        sys.stdout.write("$ ")  # maybe we are using this to write instead of print as that appends and extra newline
        sys.stdout.flush()

        list_of_commands = ['exit', 'echo', 'type']
        statement = input()

        command = statement.split()[0]
        if command not in list_of_commands:
            print(command + ": command not found")
            continue
        if command == 'exit':
            break
        if command == 'echo':
            print(' '.join(statement.split()[1:]))
            continue
        if command == 'type':
            sub_command = statement.split()[1]
            if sub_command in list_of_commands:
                print(sub_command + " is a shell builtin")
                continue
            else:
                found = False
                paths = os.environ['PATH'].split(os.pathsep)
                for path in paths:
                    if isfile(join(path, sub_command)):
                        print(sub_command + " is " + join(path, sub_command))
                        found = True
                        break
                if not found:
                    print(sub_command + " not found")
                continue

if __name__ == "__main__":
    main()
