import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    sys.stdout.write("$ ") # maybe we are using this to write instead of print as that appends and extra newline
    sys.stdout.flush()

    input()


if __name__ == "__main__":
    main()
