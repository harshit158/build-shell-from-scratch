import sys


def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command.startswith("exit "):
            sys.exit(0)
            
        elif command.startswith("echo "):
            args = ' '.join(command.split()[1:])
            sys.stdout.write(f"{args}\n")
            
        elif command.startswith("type "):
            arg = command.split()[1]
            
            if arg in ["echo", "exit", "type"]:
                sys.stdout.write(f"{arg} is a shell builtin\n")
            else:
                sys.stdout.write(f"{arg}: not found\n")    
                
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()