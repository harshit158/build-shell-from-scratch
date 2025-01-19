import sys
import os
import subprocess
import shlex

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

def extract_literal_chars(string: str):
    start = False
    res = ''
    for s in string:
        if s == "'":
            start = True if not start else False
            continue
        if start:
            res += s
        else:
            ...
    return res

def _get_parts(args):
    parts = shlex.split(args)
    return parts

def handle_echo(args):
    args = args[5:]
    parts = shlex.split(args)
    return " ".join(parts)
    
def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        
        cmd, args = command.split()[0], ' '.join(command.split()[1:])
        
        if cmd == "exit":
            sys.exit(0)
            
        elif command.startswith("echo "):
            output = handle_echo(command)
            sys.stdout.write(f"{output}\n")
            
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
            # Handle both single qtuoes and double quotes
            args = shlex.split(command)
            path = get_cmd_path(args[0])
            if path:
                subprocess.run(args)
            else:
                sys.stdout.write(f"{command}: command not found\n")
        
        sys.stdout.flush()
            


if __name__ == "__main__":
    main()