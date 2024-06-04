import sys
import os
import os.path
from os.path import isfile, isdir, join
import subprocess

def is_command_present(command, list_of_commands=[]):
    result = [False]
    for path in os.environ['PATH'].split(os.pathsep):
        if isfile(join(path, command)):
            result[0] = True
            result.append(join(path, command))
    return result
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    while 1:
        sys.stdout.write("$ ")  # maybe we are using this to write instead of print as that appends and extra newline
        sys.stdout.flush()

        list_of_commands = ['exit', 'echo', 'type']
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
                result = is_command_present(sub_command)
                found = result[0]
                if found:
                    path = result[1]
                    print(sub_command + " is " + join(path, sub_command))
                if not found:
                    print(sub_command + " not found")
                continue
        else:
            try:
                subprocess.system(statement)
            except Exception as e:
                print(command + ": command not found")
                continue

if __name__ == "__main__":
    main()
