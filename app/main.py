import sys
import os
import subprocess

def get_cmd_path(args: str):
    dirs = os.environ["PATH"].split(":")
    for dir in dirs:
        if os.path.isfile(f"{dir}/{args}"):
            return f"{dir}/{args}"
    return None

def resolve_path(target: list[str]):
    ans = []
    for cmd in target:
        if cmd == "~":
            ans.extend(os.environ["HOME"].split("/"))
        elif cmd == ".":
            continue
        elif cmd == "..":
            ans = ans[:-1]
    
    return "/".join(ans)
    
def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        
        cmd, args = command.split()[0], ' '.join(command.split()[1:])
        
        if cmd == "exit":
            sys.exit(0)
            
        elif cmd == "echo":
            sys.stdout.write(f"{args}\n")
            
        elif cmd == "pwd":
            sys.stdout.write(f"{os.getcwd()}\n")
        
        elif cmd == "cd":
            try:
                if args.startswith("/"):
                    target = args
                elif args.startswith("~"):
                    target = os.environ["HOME"] + args[1:]
                    target = os.path.normpath(target)
                elif args.startswith("."):
                    target = os.path.join(os.getcwd(), args)
                    target = os.path.normpath(target)
                else:
                    target = None
                os.chdir(target)
            except FileNotFoundError:
                sys.stdout.write(f"cd: {args}: No such file or directory\n")
            
        elif cmd == "type":
            if args in ["echo", "exit", "type", "pwd", "cd"]:
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
                subprocess.run([cmd] + args.split())
            else:
                sys.stdout.write(f"{command}: command not found\n")
        
        sys.stdout.flush()
            


if __name__ == "__main__":
    main()