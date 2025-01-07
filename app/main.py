import sys
import os
import subprocess

def get_cmd_path(args: str):
    dirs = os.environ["PATH"].split(":")
    for dir in dirs:
        if os.path.isfile(f"{dir}/{args}"):
            return f"{dir}/{args}"
    return None
    
def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        command = input()
        
        cmd, args = command.split()[0], ' '.join(command.split()[1:])
        
        if cmd == "exit":
            sys.exit(0)
            
        elif cmd == "echo":
            sys.stdout.write(f"{args}\n")
            
        elif cmd == "type":
            if args in ["echo", "exit", "type"]:
                sys.stdout.write(f"{args} is a shell builtin\n")
                continue
            
            path = get_cmd_path(args)
            if path:
                sys.stdout.write(f"{args} is {path}\n")
            else:
                sys.stdout.write(f"{args}: not found\n")
                
        else:
            path = get_cmd_path(cmd)
            if path:
                subprocess.run([path] + args.split())
            else:
                sys.stdout.write(f"{command}: command not found\n")
            


if __name__ == "__main__":
    main()