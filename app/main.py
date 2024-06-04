import sys
import os
import os.path
from os.path import isfile, isdir, join
import subprocess

def find_in_path(command):
    location = None
    for path in os.environ['PATH'].split(os.pathsep):
        if isfile(os.path.join(path, command)):
            location = os.path.join(path, command)
    return location
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    while 1:
        sys.stdout.write("$ ")  # maybe we are using this to write instead of print as that appends and extra newline
        sys.stdout.flush()

        list_of_commands = ['exit', 'echo', 'type', 'pwd', 'cd']
        statement = input()

        command = statement.split()[0]
        # if command not in list_of_commands: #and not is_command_present(command)[0]
        #                             # this part was commented because I was unable to handle the case when the
        #                             # command is present on the path but extension was not given by executer.
        #     print(command + ": command not found")
        #     continue
        if command == 'exit':
            break
        elif command == 'echo':
            print(' '.join(statement.split()[1:]))
            continue
        elif command == 'type':
            sub_command = statement.split()[1]
            if sub_command in list_of_commands:
                print(sub_command + " is a shell builtin")
                continue
            else:
                location = find_in_path(sub_command)
                if location:
                    print(sub_command + " is " + location)
                else:
                    print(sub_command + " not found")
                continue
        elif command == 'pwd':
            print(os.getcwd())
            continue
        elif command == 'cd':
            address = statement.split()[1]
            if address == '~':
                user = os.getlogin()
                address = join('', 'home', user)
                os.chdir(address)
                continue
            try:
                os.chdir(address)
            except FileNotFoundError as err:
                print(f"{address}: No such file or directory")

        else:
            try:
                subprocess.run(statement.split(' '))
            except FileNotFoundError as err:
                print(command + ": command not found")
            continue


if __name__ == "__main__":
    main()
