import sys


def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command.startswith("exit"):
            sys.exit(0)
        elif command.startswith("echo"):
            command_args = ' '.join(command.split()[1:])
            sys.stdout.write(f"{command_args}\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()