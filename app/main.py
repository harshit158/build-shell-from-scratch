import sys


def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command.startswith("exit"):
            sys.exit(0)
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()